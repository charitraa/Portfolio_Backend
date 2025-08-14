# Portfolio Backend

A RESTful API backend for managing a portfolio website.  
Built with **Django** and **Django REST Framework (DRF)**, this project provides CRUD operations for portfolio projects, supports CORS for frontend integration, and includes JWT authentication for secure access.

---

## Features

- Create, Read, Update, Delete (CRUD) portfolio projects
- RESTful API endpoints using Django REST Framework
- JWT authentication for secure API access
- CORS support for frontend applications
- Swagger/OpenAPI documentation
- Filtering and search for projects

---

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** SQLite (default), can be switched to PostgreSQL
- **Authentication:** JWT (djangorestframework-simplejwt)
- **CORS:** django-cors-headers
- **API Documentation:** drf-yasg (Swagger/OpenAPI)

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/charitraa/portfolio_backend.git
cd portfolio_backend
```
2. Create a virtual environment:
```bash
Create a virtual environment:
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Apply migrations:
```bash
python manage.py migrate

```
5. Run the development server:
```bash
python manage.py migrate

```
