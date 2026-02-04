LittleLemon Backend API - Quick Test Guide

Notes:
- Use a REST client like Insomnia.
- Include token for all endpoints requiring authentication.
- Menu GET endpoints are public for easy testing.

Base URL: http://127.0.0.1:8000/

1. Signup (create user)
POST /signup/
Body: { "username": "your_username", "password": "your_password" }

2. Login (get token)
POST /api-token-auth/
Body: { "username": "your_username", "password": "your_password" }
Response: { "token": "<your_token>" }

3. List Menu Items
GET /menu-items/
Public GET, no token required

4. Retrieve Single Menu Item
GET /menu/<id>/
Public GET

5. Create / Update / Delete Menu Item
POST /menu-items/ (create)
PUT /menu/<id>/ (update)
DELETE /menu/<id>/ (delete)
Requires token:
Authorization: Token <your_token>

6. List Bookings
GET /bookings/
Requires token

7. Create Booking
POST /bookings/
Body: { "name": "John Doe", "no_of_guests": 4, "booking_date": "2026-02-05T19:00:00Z" }
Requires token
Authorization: Token <your_token>
