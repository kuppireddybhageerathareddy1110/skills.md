# Compression Examples

| Before | After |
| --- | --- |
| The authentication middleware is probably failing because the token is expired. | Auth middleware fail. Token expired. |
| You should consider adding an index to improve query performance. | Add index. Query faster. |
| This function is doing too many things and should be split into smaller functions. | Function too broad. Split. |
| The API response needs validation before the data is passed into the UI. | Validate API res before UI. |
| There is a race condition between the save request and the navigation event. | Save/nav race. Await save first. |
| The component rerenders because the callback changes on every render. | Callback new each render. Causes rerender. |
| This environment variable is missing from the deployment configuration. | Env var missing in deploy config. |
| The database migration is not reversible, so rollback will be risky. | Migration not reversible. Rollback risky. |
| The test only checks the happy path and misses the error case. | Test covers happy path only. Add error case. |
| This dependency is unnecessary because the platform already provides the feature. | Dependency redundant. Platform has feature. |
| The request body should be parsed with a schema validator. | Parse req body with schema. |
| This logic belongs on the server because it uses secret credentials. | Server only. Uses secrets. |
| The UI layout shifts because the image has no fixed dimensions. | Image lacks size. Layout shifts. |
| The cache key is too broad and causes stale data across users. | Cache key too broad. Stale cross-user data. |
| The webhook handler must be idempotent because providers can retry events. | Webhook needs idempotency. Providers retry. |
| The error message is technically correct but not useful to the user. | Error accurate, not useful. Rewrite. |
| This abstraction adds complexity without reducing duplication. | Abstraction adds cost. No duplication win. |
| The upload flow needs a file size limit before storage writes begin. | Add size limit before storage write. |
| The route should return 401 for unauthenticated users and 403 for unauthorized users. | Return 401 unauth, 403 forbidden. |
| The build fails because the import path casing differs from the file name. | Build fail. Import case mismatch. |
