# 📌 Django-Cric-Info

## 📖 Overview
This is a **Django-based Cricketer Management System** that allows users to register, log in, and manage a collection of cricketers. It includes features like **searching, filtering, pagination, authentication, file uploads, and email notifications**. The system uses **MySQL as the database** and integrates **Google and GitHub authentication**.

---

## 🚀 Features
- **User Authentication**
  - Register/Login with Django authentication
  - Social authentication (Google & GitHub)
  - Secure password hashing and validation
- **Cricketer Management**
  - Add, update, and delete cricketer profiles
  - Search and filter cricketers based on name, age, and country
  - Pagination for better data handling
- **File Upload & Gallery**
  - Users can upload and view images of cricketers
- **Caching for Performance Optimization**
  - Implements Django file-based caching
  - Clear cache functionality for admins
- **Email Notifications**
  - Send emails with attachments using SMTP
  - Configurable email settings
- **Database Integration**
  - Uses **MySQL** with `.env` file for secure credentials
- **Secure & Scalable**
  - Implements middleware for security and caching
  - Uses environment variables to store sensitive information

---

## 📂 Project Structure
```bash
models/
│-- core/
│   │-- migrations/      # Database migrations
│   │-- templates/       # HTML templates
│   │-- static/          # Static files (CSS, JS, images)
│   │-- views.py         # Application logic
│   │-- models.py        # Database models
│   │-- forms.py         # Django forms
│   │-- urls.py          # URL routing
│-- models/
│   │-- settings.py      # Django settings
│   │-- urls.py          # Project URL configurations
│   │-- wsgi.py          # Web Server Gateway Interface
│-- media/               # Uploaded media files
│-- django_cache/        # Cached data for performance
│-- .env                 # Environment variables (hidden from Git)
│-- requirements.txt     # Python dependencies
│-- manage.py            # Django management script
```

---

## 🔧 Setup Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/jatin7425/Django-Cric-Info.git
cd Django-Cric-Info
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` File
```bash
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=3306
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your_google_key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your_google_secret
SOCIAL_AUTH_GITHUB_KEY=your_github_key
SOCIAL_AUTH_GITHUB_SECRET=your_github_secret
```

### 5️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create a Superuser
```bash
python manage.py createsuperuser
```

### 7️⃣ Run the Server
```bash
python manage.py runserver
```

Your project is now running at **http://127.0.0.1:8000/** 🎉

---

## 🛠 Usage Guide
- **Access the homepage:** `http://127.0.0.1:8000/`
- **Login/Register:** `http://127.0.0.1:8000/loginform/`
- **Manage cricketers:** `http://127.0.0.1:8000/cricketers/`
- **Upload files:** `http://127.0.0.1:8000/upload/`
- **Send emails:** `http://127.0.0.1:8000/send_email/`
- **Clear cache:** `http://127.0.0.1:8000/clear_cache/`

---

## 📌 API Endpoints (Optional if API is implemented)
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/cricketers/` | GET | Get all cricketers |
| `/api/cricketers/<id>/` | GET | Get a single cricketer |
| `/api/cricketers/` | POST | Add a new cricketer |
| `/api/cricketers/<id>/update/` | PUT | Update cricketer details |
| `/api/cricketers/<id>/delete/` | DELETE | Delete a cricketer |

---

