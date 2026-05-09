# Caveman Intensity Examples

Base paragraph:

> The API endpoint is returning stale data because the cache key does not include the current user's organization identifier. Add the organization ID to the cache key and invalidate affected entries when membership changes.

| Mode | Output |
| --- | --- |
| lite | API endpoint returns stale data because cache key misses current user's organization ID. Add org ID to cache key and invalidate entries when membership changes. |
| full | API returns stale data. Cache key misses user org ID. Add org ID. Invalidate on membership change. |
| ultra | Stale API data. Cache key lacks orgId. Add orgId. Invalidate on membership change. |
| wenyan-lite | API 得旧数，因 cache key 缺用户 orgId。加 orgId，membership 变则 invalidate。 |
| wenyan-full | cache key 无 orgId，故 API 旧。加之；membership 变则清。 |
| wenyan-ultra | 无 orgId -> 旧数。加；变则清。 |

Second paragraph:

> The component rerenders more often than necessary because the filter options object is recreated on each render. Move the object into useMemo or define it outside the component when it does not depend on props or state.

| Mode | Output |
| --- | --- |
| lite | Component rerenders too often because filter options object is recreated each render. Move it into `useMemo` or define it outside the component if static. |
| full | Component rerenders too much. Filter options object new each render. Use `useMemo` or define outside if static. |
| ultra | Extra rerenders. Filter opts obj new/render. `useMemo` or move outside. |
| wenyan-lite | 組件多重繪，因 filter options 每 render 新生。用 `useMemo`，若 static 則置外。 |
| wenyan-full | options 每繪新，致多重繪。`useMemo`；static 則外置。 |
| wenyan-ultra | options 新 -> 重繪。memo/外置。 |
