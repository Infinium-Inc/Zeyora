## Endpoints
These are the planned endpoints for the Zeyora backend API.

### Users `/users`
The `/users` endpoint is for creating, viewing, and deleting users.

#### `POST` `/`
To create a user, send a `POST` request to `/users` with a body like:
```json
{
	"name": "string",
	"email": "sample@example.com",
	"password": "string_123",
}
```

The response will be like shown below with a _status code_ of `201`.
```json
{
	"name": "string",
	"email": "sample@example.com",
	"created_at": "yyyy-mm-dd_hh:mm:ss.msmsms+hh:mm",
	"id": 123
}
```

#### `GET` `/{id}`
To create a user, send a `GET` request to `/users/{id}` and replace `{id}` by the `id` of the user.

The response will be like shown below with a _status code_ of `200`.
```json
{
	"name": "string",
	"email": "sample@example.com",
	"created_at": "yyyy-mm-dd_hh:mm:ss.msmsms+hh:mm",
	"id": 123
}
```

#### `PUT` `/{id}`
To update a user's _email_, _name_ or _password_, send a `PUT` request to `/users/{id}`, and replace `{id}` by the `id` of the user, with a body like:
```json
{
	"name": "string",
	"email": "sample@example.com",
	"password": "string_123",
}
```
> NOTE: The _password_ is not necessary, it is only needed when you want to update the password.

The response will be like shown below with a _status code_ of `202`.
```json
{
	"name": "string",
	"email": "sample@example.com",
	"created_at": "yyyy-mm-dd_hh:mm:ss.msmsms+hh:mm",
	"id": 123
}
```

#### `DELETE` `/{id}`
To delete a user, send a `DELETE` request to `/users/{id}` and replace `{id}` by the `id` of the user.

There will be no response with a _status code_ of `204`.