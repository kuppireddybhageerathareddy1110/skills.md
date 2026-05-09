---
name: api-contract-generator
description: |-
  Generates API contracts (OpenAPI 3.1 specs), type-safe schemas (Zod for TypeScript, Pydantic for Python), and integration tests from source code or descriptions. Use this skill whenever the user wants to document an API, generate schemas, create type-safe clients, ensure frontend-backend contract consistency, or asks "generate OpenAPI", "create Zod schema", "make Pydantic models", "write API docs", or shares endpoint code and wants contracts or tests generated from it.
---

# Skill: api-contract-generator

## Purpose
Extracts API contracts from code or descriptions and generates: OpenAPI 3.1 specs, Zod validators (TypeScript), Pydantic models (Python), and contract test skeletons.

## Supported Input Forms
- FastAPI / Flask / Express / Spring Boot route code
- Plain English description of endpoints
- Existing partial OpenAPI spec to complete
- TypeScript interface or Python dataclass to convert

---

## Generation Process

### Step 1: Extract Endpoints
For each endpoint identify:
- HTTP method + path (e.g., `POST /users/{id}/orders`)
- Path parameters + types
- Query parameters (required/optional, types, constraints)
- Request body schema (all fields, types, required/optional, validation rules)
- Response schemas per status code (200, 201, 400, 401, 404, 422, 500)
- Authentication method (Bearer JWT, API key, OAuth scope)
- Rate limit headers if mentioned

### Step 2: Extract Field Rules
For every request/response field:
| Property | Extract |
|----------|---------|
| Type | string, number, boolean, array, object |
| Format | email, uuid, date-time, url, uri |
| Required | yes/no |
| Constraints | minLength, maxLength, minimum, maximum, pattern, enum |
| Example | realistic sample value |
| Description | human-readable purpose |

### Step 3: Generate Artifacts

#### A. OpenAPI 3.1 YAML
```yaml
openapi: 3.1.0
info:
  title: {API Name}
  version: 1.0.0
paths:
  /resource/{id}:
    get:
      summary: Get resource by ID
      security:
        - bearerAuth: []
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Resource'
        '404':
          $ref: '#/components/responses/NotFound'
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
  schemas:
    Resource:
      type: object
      required: [id, name, createdAt]
      properties:
        id:
          type: string
          format: uuid
          example: "550e8400-e29b-41d4-a716-446655440000"
        name:
          type: string
          minLength: 1
          maxLength: 255
        createdAt:
          type: string
          format: date-time
```

#### B. Zod Schema (TypeScript)
```typescript
import { z } from 'zod';

export const ResourceSchema = z.object({
  id: z.string().uuid(),
  name: z.string().min(1).max(255),
  email: z.string().email().optional(),
  role: z.enum(['admin', 'user', 'guest']),
  createdAt: z.string().datetime(),
});

export type Resource = z.infer<typeof ResourceSchema>;

export const CreateResourceSchema = ResourceSchema.omit({ id: true, createdAt: true });
export type CreateResource = z.infer<typeof CreateResourceSchema>;
```

#### C. Pydantic Model (Python)
```python
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal
from datetime import datetime
from uuid import UUID

class Resource(BaseModel):
    id: UUID
    name: str = Field(..., min_length=1, max_length=255)
    email: Optional[EmailStr] = None
    role: Literal['admin', 'user', 'guest']
    created_at: datetime

    class Config:
        json_encoders = {datetime: lambda v: v.isoformat()}

class CreateResource(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    email: Optional[EmailStr] = None
    role: Literal['admin', 'user', 'guest'] = 'user'
```

#### D. Contract Test Skeleton
```typescript
// resource.contract.test.ts
describe('GET /resources/:id', () => {
  it('returns 200 with valid Resource schema for existing ID', async () => {
    const res = await api.get(`/resources/${validId}`);
    expect(res.status).toBe(200);
    expect(ResourceSchema.safeParse(res.data).success).toBe(true);
  });

  it('returns 404 for non-existent ID', async () => {
    const res = await api.get('/resources/00000000-0000-0000-0000-000000000000');
    expect(res.status).toBe(404);
  });

  it('returns 401 without auth token', async () => {
    const res = await unauthenticatedApi.get(`/resources/${validId}`);
    expect(res.status).toBe(401);
  });
});
```

---

## Output Format

Always produce in this order:

### 📄 API Contract: `{API Name}`

**Endpoints found**: N
**Auth**: Bearer JWT / API Key / None

#### Endpoint Summary Table
| Method | Path | Auth | Request Body | Response |
|--------|------|------|-------------|----------|
| GET | /users/{id} | ✓ | — | User |
| POST | /users | ✓ | CreateUser | User |

---

Then for each artifact requested (or all if unspecified):

**OpenAPI 3.1 YAML** — full spec in code block
**Zod Schemas** — TypeScript code block
**Pydantic Models** — Python code block
**Contract Tests** — TypeScript/Python test skeleton

---

### ⚠️ Gaps & Assumptions
List any fields where types were assumed, constraints inferred, or information was missing.

---

## Rules
- NEVER invent endpoints not present in the source
- ALWAYS include error response schemas (400, 401, 404, 422, 500)
- Mark every assumption explicitly in the Gaps section
- Use realistic example values, not "string" or "example"
- If input is ambiguous, generate the most reasonable interpretation and note it
