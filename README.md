# Endpoint

The endpoint data json request goes as follow:

## DONE:
23/11/2023 00:44
1. Added Private Key and Public Key.

## TODO:
1. Add 


# Method Type: "user"

```json
{
    "method": "user/login",
    "data": {
        "username": "admin",
        "password": "password123"
    }
}
```

```json
{
    "method": "user/register",
    "data": {
        "username": "admin",
        "password": "password123"
    }
}
```

```json
{
    "method": "user/change_password",
    "data": {
        "oldpassword": "password123",
        "newpassword": "password1234",
        "sessionid": ""
    }
}
```
```json
{
    "method": "user/logout_everywhere",
    "data": {
        "sessionid": ""
    }
}
```
```json
{
    "method": "action/main",
    "data": {
        "sessionid": ""
    }
}
```

