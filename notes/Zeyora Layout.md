## Endpoints
These are the planned endpoints for the Zeyora backend API.

### Users `/users`
The `/users` endpoint is for creating, viewing, and deleting users.

#### `POST` `/`
To create a user, send a `POST` request to `/users` with a body like:
```json
{
	"name": string,
	"email": email_string = null,
	"mobile": string = null,
	"password": string,
}
```
> **NOTE**: One of the two, the _email_ or the _mobile_ must be provided.

The response will be like shown below with a _status code_ of `201`.
```json
{
	"name": string,
	"email": email_string = null,
	"mobile": string = null,
	"created_at": time_format(yyyy-mm-dd_hh:mm:ss.msmsms+hh:mm),
	"id": integer
}
```