# Sample Output: Production Bug

## Orient

Login timeout likely comes from token refresh state drifting between middleware and session storage. Risk is broad because every protected route depends on this path.

## Plan

1. Reproduce timeout with expired and near-expired tokens.
2. Inspect middleware expiry comparison.
3. Patch refresh retry and cookie update.
4. Add regression tests for token boundary cases.
5. Verify protected and public routes.

## Execute

Patch only auth middleware and session helpers. Keep route behavior unchanged except for correct refresh handling.

## Verify

- Expired token redirects to login.
- Near-expired token refreshes once.
- Valid token continues without refresh.
- Failed refresh clears session.
