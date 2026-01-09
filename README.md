# 🛒 Django & Vue.js WebShop

A full-stack e-commerce application demonstrating a complete shopping flow from product selection to payment processing. Built with a **Django REST Framework** backend and a **Vue.js 3** frontend, fully containerized with **Docker**.

## 🚀 Tech Stack

- **Backend:** Python 3.11, Django 5, Django REST Framework
- **Frontend:** Vue.js 3, Vue Router, Axios (Node.js 22)
- **Payment Gateway:** CloudIPSP (Fondy) Integration
- **Database:** SQLite (Default for Dev/Docker)
- **Containerization:** Docker & Docker Compose

## 🌟 Key Features

- **Product Management:** RESTful API endpoints for product data.
- **Dynamic Cart:** Client-side state management for the shopping basket.
- **Checkout Flow:** Form validation and order persistence using Serializers.
- **Payment Integration:** Secure redirection to Fondy payment gateway.
- **Clean Code:** Separation of concerns between frontend and backend.

---

## 🐳 Quick Start with Docker (Recommended)

The easiest way to run the application is using Docker. You don't need to install Python or Node.js manually.

### 1. Prerequisites
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).

### 2. Run the application
Open a terminal in the project root and run:
```bash
docker-compose up --build
```

3. Access the App
Frontend (Shop): http://localhost:5173

Backend (Admin): http://localhost:8000/admin

4. First Run Setup
Since the database is fresh inside the container, apply migrations and create an admin user:

```bash

# Open a new terminal while Docker is running:
docker exec -it webshop_backend python manage.py migrate
docker exec -it webshop_backend python manage.py createsuperuser
```
🛠️ Manual Local Setup (Without Docker)
If you prefer running it directly on your machine without containers:

1. Backend Setup
Navigate to the root directory:

```bash
# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start Server
python manage.py runserver
```
API runs at: http://127.0.0.1:8000/

2. Frontend Setup
Navigate to the frontend folder (e.g., public):

```bash

cd public
npm install
npm run dev
```
App runs at: http://localhost:5173/ 
