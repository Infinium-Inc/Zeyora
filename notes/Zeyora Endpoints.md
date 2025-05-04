## Users
- create user (POST /users)
- view user (GET /users/{id})
- delete user (DELETE /users/{id})
- update user (PUT /users/{id}) 
- login user (POST /login) 

## Items
- view items (GET /items)
- view item (GET /items/{id})

## Orders
- place order in cart (POST /orders)
- view order (GET /orders/{id})
- cancel order (DELETE /orders/{id})
- place order (PATCH /orders/{id})

# Admin Endpoints
## Users
- view users (GET /admin/users) [ADMIN]
- view user history (GET /admin/users/history) [ADMIN]

## Items
- add item (POST /admin/items) [ADMIN]
- delete item (DELETE /admin/items/{id}) [ADMIN]
- update item (PUT /admin/items/{id}) [ADMIN]

## Orders
- view orders (GET /admin/orders) [ADMIN]
- update order (PATCH /admin/orders/{id}) [ADMIN]
