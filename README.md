# Patreon donator checker api

Create api take simple information from patreon to know status of your patreons

Demo: https://patreon-donator-checker-api.onrender.com/docs

# What is set?

Currently, have a configuration that show in the response the following cases

- User Active -> More than 300cents and not decline and not pause
- User Inactive -> Less than 300cents and not decline and not pause
- User Inactive -> Decline or pause

You can change defining the logic on **get_patreon_list**

## Example:

```json
[
  {
    "id": "1234568",
    "username": "dummy1",
    "mail": "dummy1@test.com",
    "status": "INACTIVE",
    "tier": null
  },
    {
    "id": "1234568",
    "username": "dummy1",
    "mail": "dummy1@test.com",
    "status": "ACTIVE",
    "tier": "Tier 2"
  }
  
]
```

# What environment variables I need?

- ACCESS_TOKEN: Access token provide by Patreon
- X-API-Key-Valid: Internal key use to validate request from know resources

### Pending
- Fetch specific users
- ~~Create cache/database to fetch on the same 1 minutes~~
  