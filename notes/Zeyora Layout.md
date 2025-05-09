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