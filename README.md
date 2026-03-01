# 🛒 PutiMart – Scalable E-Commerce REST API

PutiMart is a scalable and production-ready E-commerce REST API built with Django and Django REST Framework.  
The project follows a clean layered architecture with Nested Routers, Djoser authentication, JWT security, and optimized database querying.

---

## 🚀 Features

- 🔐 JWT Authentication (Djoser + Simple JWT)
- 👤 User Registration & Login
- 🔑 Password Reset System
- 📦 Product Management (Admin)
- 🖼 Product Image Upload
- ⭐ Product Reviews (Nested Router)
- 🛒 Cart & Cart Item Management (Nested Router)
- 📑 Order Creation from Cart
- ❌ Order Cancellation
- 🔄 Order Status Update (Admin Only)
- 🛠 Service Layer Architecture
- 🧠 Optimized ORM (`select_related`, `prefetch_related`)
- 🔒 Role-Based Permissions (User / Admin)

---

## 🏗 Tech Stack

- Python 3.13  
- Django 6+  
- Django REST Framework  
- Djoser  
- Simple JWT  
- SQLite (Default DB)  
- Pillow (Image Handling)

---

## 📂 Project Structure

PutiMart/
│
├── products/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│
├── autentications/
|   ├── models.py
│   ├── serializers.py
│   ├── views.py
│
├── cart/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│
├── orders/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── service.py
│
└── manage.py

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

git clone https://github.com/awal75/PutiMart-Backend.git  
cd PutiMart-Backend  

---

### 2️⃣ Create Virtual Environment

python -m venv env  
env\Scripts\activate  (Windows)

---

### 3️⃣ Install Dependencies

pip install -r requirements.txt  

---

### 4️⃣ Apply Migrations

python manage.py migrate  

---

### 5️⃣ Create Superuser

python manage.py createsuperuser  

---

### 6️⃣ Run Server

python manage.py runserver  

Server will run at:

http://127.0.0.1:8000/

---

## 🔐 Authentication (Djoser + JWT)

### Register
POST /auth/users/

### Login
POST /auth/jwt/create/

### Refresh Token
POST /auth/jwt/refresh/

### Password Reset
POST /auth/users/reset_password/
POST /auth/users/reset_password_confirm/

Include JWT in Header:

Authorization: Bearer <access_token>

---

## 🔗 Nested Router Structure

/api/v1/products/{product_id}/reviews/
/api/v1/products/{product_id}/images/
/api/v1/carts/{cart_id}/items/

---

## 📦 API Endpoints

### 🛍 Products

GET    /api/v1/products/  
POST   /api/v1/products/ (Admin)  
GET    /api/v1/products/{id}/  
PATCH  /api/v1/products/{id}/ (Admin)  
DELETE /api/v1/products/{id}/ (Admin)  

---

### ⭐ Reviews (Nested)

GET    /api/v1/products/{product_id}/reviews/  
POST   /api/v1/products/{product_id}/reviews/  
PATCH  /api/v1/products/{product_id}/reviews/{id}/  
DELETE /api/v1/products/{product_id}/reviews/{id}/  

---

### 🛒 Cart

POST   /api/v1/v1/carts/  
GET    /api/v1/carts/{id}/  
DELETE /api/v1/carts/{id}/  

---

### 🛒 Cart Items (Nested)

POST   /api/v1/carts/{cart_id}/items/  
PATCH  /api/v1/carts/{cart_id}/items/{id}/  
DELETE /api/v1/carts/{cart_id}/items/{id}/  

---

### 📑 Orders

POST   /api/v1/orders/  
GET    /api/v1/orders/  
POST   /api/v1/orders/{id}/cancel/  
POST   /api/v1/orders/{id}/update-status/ (Admin)  

---

## 🧠 Architecture

View → Serializer → Service → Model

Example:

OrderService.create_order(user, cart_id)

---

## 🖼 Media Configuration

In settings.py:

MEDIA_ROOT = BASE_DIR / "media"  
MEDIA_URL = "/media/"

Images stored in:

media/products/images/

---

## 🔒 Permission System

### User Can:
- Manage own cart
- Create order
- Cancel own order
- Add review

### Admin Can:
- CRUD Products
- Update Order Status
- View all orders

---

## 📌 Future Improvements

- Payment Gateway Integration
- Order State Machine
- Wishlist
- Docker Support
- Redis + Celery
- CI/CD Pipeline

---

## 👨‍💻 Author

**Awal Islam**  
*Backend Developer | Django | DRF*

---

## 📜 License

This project is open-source