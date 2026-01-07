# 🛒 Django & Vue.js WebShop

A full-stack e-commerce application demonstrating a complete shopping flow from product selection to payment processing. Built with a **Django REST Framework** backend and a **Vue.js 3** frontend.

## 🚀 Tech Stack

- **Backend:** Python 3.11, Django 5, Django REST Framework
- **Frontend:** Vue.js 3, Vue Router, Axios
- **Payment Gateway:** CloudIPSP (Fondy) Integration
- **Database:** SQLite (Dev) / PostgreSQL (Prod ready)

## 🌟 Key Features

- **Product Management:** RESTful API endpoints for product data.
- **Dynamic Cart:** Client-side state management for the shopping basket.
- **Checkout Flow:** Form validation and order persistence using Serializers.
- **Payment Integration:** Secure redirection to Fondy payment gateway.
- **Clean Code:** Separation of concerns between frontend and backend.

## 🛠️ How to Run Locally

### 1. Backend Setup
Navigate to the root directory:
```bash
# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install cloudipsp

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start Server
python manage.py runserver

API runs at: http://127.0.0.1:8000/

2. Frontend Setup
Navigate to the frontend folder (e.g., public or root):

npm install
npm run dev

App runs at: http://localhost:5173/