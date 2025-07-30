# 💰 Debt Manager API

A simple and powerful RESTful API built with Django and Django REST Framework to manage debts between users. Ideal for tracking loans, repayments, and shared debts.

## 📌 Features

- ✅ User registration and authentication
- ✅ Create and manage personal debts
- ✅ Assign debts to other users
- ✅ Track repayment status
- ✅ Support for co-signers / guarantors / joint debtors
- ✅ JWT-based login and secure API access
- ✅ Admin panel for superusers
- ✅ Swagger (OpenAPI) documentation

## ⚙️ Tech Stack

- Python 3.11+
- Django 4.x
- Django REST Framework (DRF)
- PostgreSQL
- drf-yasg (Swagger docs)
- Simple JWT (Authentication)
- Docker (optional)

## 🧩 Project Structure



## 🚀 Getting Started

### 1. Clone the repository


```bash

# Clone the repository
git clone git@github.com:yourusername/debt-manager.git
cd debt-manager
```


```bash

### 2. Set up a virtual environment and install dependencies
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

```


```python

### Configure your environment variables and database connection
### in settings.py:

SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=postgres://user:password@localhost:5432/debt_db

```


```bash

### 3. Set up the database
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

```

```bash

### 4. Run the development server
python manage.py runserver

```

