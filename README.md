# Patreon donator checker api

Create api take simple information from patreon to know status of your patreons

Demo: https://patreon-donator-checker-api.herokuapp.com/docs

# What is set?

Currently have a configuration that show in the response the following cases

- User Active -> More than 300cents and not decline and not pause
- User Inactive -> Less than 300cents and not decline and not pause
- User Inactive -> Decline or pause

### Pending
- Fetch specific users
- Create cache/database to fetch on the same 5 minutes
  