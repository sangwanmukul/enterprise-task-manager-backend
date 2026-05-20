# 🚀 Enterprise Team Task Manager API

A production-ready enterprise-grade Task Management Backend built using **FastAPI**, **PostgreSQL**, **JWT Authentication**, **RBAC**, **WebSockets**, **AI-powered analytics**, and deployed on **Railway**.

---

# 🌐 Live Deployment

## 🔗 Live Backend API

https://web-production-e1ede.up.railway.app

## 📘 Swagger API Docs

https://web-production-e1ede.up.railway.app/docs

---

# ✨ Features

## 🔐 Authentication & Security

* JWT Authentication
* Secure Password Hashing (bcrypt)
* OAuth2 Authentication
* Role-Based Access Control (RBAC)
* Protected APIs
* Authorization Middleware

---

## 📁 Project Management

* Create Projects
* Manage Team Members
* Assign Project Members
* Track Project Ownership

---

## ✅ Task Management

* Create Tasks
* Update Task Status
* Delete Tasks
* Task Priorities
* Due Dates
* Task Assignment
* File Attachments
* Comments System

---

## 👥 Team Collaboration

* Team Member Management
* Notifications
* Activity Logs
* Real-time WebSocket Support

---

## 🤖 AI Features

* AI Risk Prediction
* AI Task Summary
* Task Risk Analysis APIs

---

## 🏢 Enterprise Features

* Pagination
* Search & Filtering
* Soft Delete
* Audit Middleware
* Activity Tracking
* Tags & Labels
* Analytics APIs
* Admin Controls

---

# 🛠️ Tech Stack

## Backend

* FastAPI
* Python
* SQLAlchemy
* Pydantic

## Database

* PostgreSQL

## Authentication

* JWT
* Passlib
* Bcrypt

## Deployment

* Railway

## Real-Time

* WebSockets

## Infrastructure

* Redis Ready Architecture
* Alembic
* Uvicorn

---

# 📂 Project Structure

```bash
backend/
│
├── app/
│   │
│   ├── core/                          # Core application configuration and utilities
│   │   ├── __init__.py
│   │   ├── config.py                  # Environment and application settings
│   │   ├── database.py                # Database connection and session management
│   │   ├── rate_limiter.py            # API rate limiting configuration
│   │   ├── redis.py                   # Redis connection setup
│   │   ├── security.py                # JWT authentication and password hashing
│   │   └── websocket_manager.py       # WebSocket connection manager
│   │
│   ├── dependencies/                  # Dependency injection modules
│   │   ├── __init__.py
│   │   ├── auth_dependencies.py       # Authentication dependencies
│   │   └── permission_dependencies.py # Role and permission checks
│   │
│   ├── middleware/                    # Custom middleware components
│   │   ├── __init__.py
│   │   ├── audit_middleware.py        # Audit logging middleware
│   │   └── logging_middleware.py      # Request/response logging middleware
│   │
│   ├── models/                        # SQLAlchemy database models
│   │   ├── __init__.py
│   │   ├── activity_log_model.py      # Activity log model
│   │   ├── activity_model.py          # Activity model
│   │   ├── attachment_model.py        # File attachment model
│   │   ├── comment_model.py           # Comment model
│   │   ├── notification_model.py      # Notification model
│   │   ├── project_model.py           # Project model
│   │   ├── tag_model.py               # Tag model
│   │   ├── task_model.py              # Task model
│   │   ├── team_member_model.py       # Team member model
│   │   └── user_model.py              # User model
│   │
│   ├── routers/                       # API route handlers
│   │   ├── __init__.py
│   │   ├── activity_log_routes.py     # Activity log APIs
│   │   ├── admin_routes.py            # Admin management APIs
│   │   ├── ai_routes.py               # AI-powered APIs
│   │   ├── analytics_routes.py        # Analytics and reports APIs
│   │   ├── auth_routes.py             # Authentication APIs
│   │   ├── comment_routes.py          # Comment management APIs
│   │   ├── dashboard_routes.py        # Dashboard APIs
│   │   ├── notification_routes.py     # Notification APIs
│   │   ├── project_routes.py          # Project management APIs
│   │   ├── tag_routes.py              # Tag management APIs
│   │   ├── task_routes.py             # Task management APIs
│   │   ├── team_routes.py             # Team management APIs
│   │   ├── user_routes.py             # User management APIs
│   │   └── websocket_routes.py        # WebSocket endpoints
│   │
│   ├── schemas/                       # Pydantic request/response schemas
│   │   ├── __init__.py
│   │   ├── auth_schema.py             # Authentication schemas
│   │   ├── comment_schema.py          # Comment schemas
│   │   ├── dashboard_schema.py        # Dashboard schemas
│   │   ├── notification_schema.py     # Notification schemas
│   │   ├── project_schema.py          # Project schemas
│   │   ├── tag_schema.py              # Tag schemas
│   │   └── task_schema.py             # Task schemas
│   │
│   ├── services/                      # Business logic layer
│   │   ├── __init__.py
│   │   ├── activity_service.py        # Activity management logic
│   │   ├── ai_service.py              # AI service logic
│   │   ├── auth_service.py            # Authentication logic
│   │   ├── notification_service.py    # Notification service logic
│   │   ├── project_service.py         # Project service logic
│   │   └── task_service.py            # Task service logic
│   │
│   ├── utils/                         # Utility/helper functions
│   │   ├── __init__.py
│   │   ├── constants.py               # Application constants
│   │   ├── filters.py                 # Filtering utilities
│   │   ├── helpers.py                 # Common helper functions
│   │   ├── pagination.py              # Pagination utilities
│   │   ├── search.py                  # Search utilities
│   │   └── validators.py              # Custom validators
│   │
│   └── main.py                        # FastAPI application entry point
│
├── tests/                             # Unit and integration tests
│
├── venv/                              # Virtual environment (ignored in Git)
│
├── .env                               # Environment variables
├── .gitignore                         # Git ignored files
├── alembic.ini                        # Alembic migration configuration
├── Procfile                           # Deployment process file
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── runtime.txt                        # Python runtime version
└── test.db                            # SQLite test database
```

---

# 📡 API Modules

## 🔐 Authentication APIs

* Signup
* Login
* JWT Token Generation

## 👤 User APIs

* Get Users
* Update User
* Delete User

## 📁 Project APIs

* Create Project
* Get Projects
* Add Team Members

## ✅ Task APIs

* Create Task
* Update Task
* Delete Task
* Upload Attachments

## 🤖 AI APIs

* Predict Task Risk
* AI Summary

## 📊 Dashboard APIs

* Analytics
* Project Statistics
* Completion Tracking

## 🛡️ Admin APIs

* Manage Users
* Update Roles

---

# ⚙️ Local Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/sangwanmukul/enterprise-task-manager-backend.git

cd enterprise-task-manager-backend
```

---

## 2️⃣ Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create Environment Variables

Create `.env` file:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/task_manager

SECRET_KEY=supersecretkey

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

REFRESH_TOKEN_EXPIRE_DAYS=7

REDIS_URL=redis://localhost:6379

UPLOAD_DIR=uploads
```

---

## 5️⃣ Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

# 📘 Open API Docs

```bash
http://127.0.0.1:8000/docs
```

---

# 🚀 Railway Deployment

## Push Code to GitHub

```bash
git init

git add .

git commit -m "initial commit"

git push origin main
```

---

## Deploy on Railway

1. Create Railway Project
2. Connect GitHub Repository
3. Add PostgreSQL Service
4. Add Environment Variables
5. Deploy Automatically

---

# 🔑 Railway Environment Variables

```env
DATABASE_URL=<railway_postgres_url>

SECRET_KEY=supersecretkey

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

REFRESH_TOKEN_EXPIRE_DAYS=7

REDIS_URL=redis://localhost:6379

UPLOAD_DIR=uploads
```

---

# 🔐 Authentication Flow

## Signup Request

```json
{
  "name": "Mukul",
  "email": "mukul@gmail.com",
  "password": "mukul",
  "role": "admin"
}
```

---

## Login Request

Use OAuth2 form data:

```text
username: mukul@gmail.com

password: mukul
```

---

## Swagger Authorization

```text
Bearer YOUR_ACCESS_TOKEN
```

---

# 📁 Example Project Creation

```json
{
  "name": "Enterprise AI Project",
  "description": "Advanced task manager system"
}
```

---

# ✅ Example Task Creation

```json
{
  "title": "Build FastAPI Backend",
  "description": "Develop enterprise backend",
  "priority": "high",
  "status": "pending",
  "project_id": 1
}
```

---

# 🔒 Security Features

* JWT Authentication
* Password Hashing
* OAuth2 Password Flow
* Protected Routes
* RBAC Authorization
* Middleware Logging

---

# 🤖 AI Features

## AI Risk Prediction

Predicts task risk levels based on:

* Priority
* Deadlines
* Status
* Task Metadata

## AI Summary

Provides project analytics and summaries.

---

# ⚡ WebSocket Support

Supports:

* Real-time Notifications
* Live Updates
* Event Broadcasting

---

# 🚀 Future Improvements

* Docker Production Setup
* Kubernetes Deployment
* CI/CD Pipeline
* Unit Testing
* Email Notifications
* Advanced AI Analytics
* Mobile App Integration
* Microservices Architecture
* Celery Background Tasks
* Redis Caching

---

# 👨‍💻 Author

## Mukul Sangwan

Third-year Engineering Student | Backend Developer | AI & Cloud Enthusiast

### GitHub Repository

https://github.com/sangwanmukul/enterprise-task-manager-backend

---

# 📄 License

This project is licensed under the MIT License.

---

# 🎯 Conclusion

This project demonstrates:

* Enterprise Backend Development
* REST API Design
* Authentication & Authorization
* PostgreSQL Integration
* Railway Deployment
* AI Feature Integration
* Production-ready Architecture
* Real-time System Design
