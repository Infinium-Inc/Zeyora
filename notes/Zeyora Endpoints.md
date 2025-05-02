## Users
- create user (POST /users)
- view users (GET /users) [ADMIN]
- view user (GET /users/{id})
- delete user (DELETE /users/{id})
- update user (PUT /users/{id}) 
- login user (POST /login) 

## Items
- add item (POST /items) [ADMIN]
- view items (GET /items)
- view item (GET /items/{id})
- delete item (DELETE /items/{id}) [ADMIN]
- update item (PUT /items/{id}) [ADMIN]

## Orders
- place order in cart (POST /orders)
- view orders (GET /orders) [ADMIN]
- view order (GET /orders/{id})
- cancel order (DELETE /orders/{id})
- place order (PATCH /orders/{id})