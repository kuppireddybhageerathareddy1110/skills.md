---
name: code-review-architect
description: |-
  Performs comprehensive, multi-dimensional code reviews covering security, performance, maintainability, testing, and architecture. Use this skill whenever the user shares code and asks for a review, audit, analysis, or feedback — even casual asks like "what do you think of this code?" or "any issues here?". Also triggers for: "check this for vulnerabilities", "is this production-ready?", "review my PR", "audit this file", "find bugs in this", or any request involving uploaded code files. Always use this skill before giving code feedback.
---

# Skill: code-review-architect

## Purpose
Performs structured code reviews across five dimensions: Security, Performance, Maintainability, Testing, and Architecture. Returns prioritized findings with concrete fixes.

## Supported Languages
Python, JavaScript/TypeScript, Java, Go, Rust, SQL, Bash, and most others.

## Input Forms
- Pasted code snippet
- Uploaded file(s)
- Git diff / PR description
- Directory structure description

---

## Review Process

### Step 1: Orient
Identify: language, framework, what the code does, entry points, external dependencies.

### Step 2: Run All Five Checks

#### 1. SECURITY (highest priority)
Always scan for:
- **SQL injection**: string interpolation in queries → flag, show parameterized fix
- **Hardcoded secrets**: API keys, passwords, tokens in source → flag as CRITICAL
- **Unvalidated input**: user input passed to shell, eval, exec, subprocess → CRITICAL
- **Insecure deserialization**: pickle, yaml.load without Loader, JSON from untrusted sources
- **Missing auth checks**: endpoints without authentication/authorization guards
- **CORS/CSRF**: missing protections on state-changing endpoints
- **Path traversal**: user-controlled file paths
- **Dependency risks**: obviously outdated or known-vulnerable imports (if version visible)

#### 2. PERFORMANCE
Scan for:
- **N+1 queries**: SELECT inside a loop → recommend JOIN or batch fetch
- **O(n²) or worse**: nested loops over same collection → flag with complexity estimate
- **Blocking I/O in async context**: sync calls inside async functions
- **Unbounded caches/lists**: appending without eviction or size cap
- **Missing indexes**: queries filtering on non-indexed columns (if schema visible)
- **Repeated expensive calls**: same computation in a loop → hoist outside

#### 3. MAINTAINABILITY
Scan for:
- **Functions > 50 lines**: recommend extraction, suggest split points
- **Cyclomatic complexity > 10**: too many branches → recommend simplification
- **Magic numbers/strings**: literals without named constants
- **Dead code**: unreachable branches, unused imports/variables
- **Missing docstrings**: public functions/classes without documentation
- **Inconsistent naming**: mixed conventions (camelCase + snake_case in same scope)

#### 4. TESTING
Scan for:
- **Untested critical paths**: business logic, error handling, auth flows with no tests
- **Missing edge case coverage**: empty input, None/null, boundary values
- **Mocking abuse**: unit tests that mock everything → recommend integration tests
- **No test files**: new modules with zero test coverage

#### 5. ARCHITECTURE
Scan for:
- **Circular imports**: A imports B imports A
- **God objects**: classes/modules with > 5 unrelated responsibilities
- **Missing abstraction**: repeated logic that should be a shared utility
- **Tight coupling**: direct instantiation instead of dependency injection
- **Separation of concerns violations**: business logic mixed into controllers/views

---

### Step 3: Assign Severity

| Level | Meaning |
|-------|---------|
| CRITICAL | Security hole, data loss risk, exploit vector |
| HIGH | Performance bug, architectural debt with real user impact |
| MEDIUM | Maintainability issue, missing tests for important paths |
| LOW | Style, naming, minor documentation gaps |

### Step 4: Output the Review

Use this structure:

---

## 📋 Code Review: `[filename or "snippet"]`
**Language**: X | **Lines**: N | **Score**: X/10

### Summary
N critical · N high · N medium · N low

### Findings

**[SEVERITY] [CATEGORY] — Line N (or "general")**
> _Issue_: One-sentence description.
> _Why_: Brief explanation of impact.
> _Fix_:
```language
// concrete corrected code here
```

_(repeat for each finding)_

### Architecture Notes
Brief paragraph on overall structure, coupling, testability.

### Top 3 Actions (prioritized)
1. [Most urgent fix] — ~Xmin effort
2. [Second priority] — ~Xmin effort
3. [Third priority] — ~Xmin effort

---

## What NOT to Flag
- Style preferences already handled by linters (indentation, trailing spaces)
- Framework-specific conventions that are intentional (Django signals, Rails magic)
- Documented intentional technical debt
- Third-party/vendored library code

## Scoring Rubric
Start at 10. Deduct:
- CRITICAL: −2 each
- HIGH: −1 each
- MEDIUM: −0.5 each
- LOW: −0.1 each
Minimum score: 1.

## Tone
Be direct and specific. Every finding must have a concrete fix. Do not pad with generic advice. If code is good, say so briefly and move on.
