from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.core.database import (
    Base,
    engine
)

from app.middleware.audit_middleware import (
    AuditMiddleware
)

# AUTH ROUTES

from app.routers.auth_routes import (
    router as auth_router
)

# PROJECT ROUTES

from app.routers.project_routes import (
    router as project_router
)

# TASK ROUTES

from app.routers.task_routes import (
    router as task_router
)

# DASHBOARD ROUTES

from app.routers.dashboard_routes import (
    router as dashboard_router
)

# NOTIFICATION ROUTES

from app.routers.notification_routes import (
    router as notification_router
)

# COMMENT ROUTES

from app.routers.comment_routes import (
    router as comment_router
)

# WEBSOCKET ROUTES

from app.routers.websocket_routes import (
    router as websocket_router
)

# USER ROUTES

from app.routers.user_routes import (
    router as user_router
)

# ADMIN ROUTES

from app.routers.admin_routes import (
    router as admin_router
)

# TAG ROUTES

from app.routers.tag_routes import (
    router as tag_router
)

# ACTIVITY LOG ROUTES

from app.routers.activity_log_routes import (
    router as activity_log_router
)

# TEAM ROUTES

from app.routers.team_routes import (
    router as team_router
)

# ANALYTICS ROUTES

from app.routers.analytics_routes import (
    router as analytics_router
)

# AI ROUTES

from app.routers.ai_routes import (
    router as ai_router
)

# IMPORT ALL MODELS

from app.models.user_model import User

from app.models.project_model import Project

from app.models.task_model import Task

from app.models.team_member_model import TeamMember

from app.models.notification_model import Notification

from app.models.activity_log_model import ActivityLog

from app.models.comment_model import Comment

from app.models.attachment_model import Attachment

from app.models.tag_model import Tag

# CREATE DATABASE TABLES

Base.metadata.create_all(
    bind=engine
)

# FASTAPI APP

app = FastAPI(

    title="Enterprise Team Task Manager API",

    version="1.0.0",

    description="""
Professional enterprise-grade task management system.

Features:

- JWT Authentication
- RBAC Authorization
- Project Management
- Task Tracking
- Dashboard Analytics
- Activity Logging
- Pagination
- Search & Filtering
- WebSockets
- Notifications
- AI Risk Scoring
- File Attachments
- Comments System
- Soft Delete
- PostgreSQL
- Redis Ready
- Team Management
- Admin Controls
- AI Analytics
"""
)

# CORS

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

# AUDIT MIDDLEWARE

app.add_middleware(
    AuditMiddleware
)

# REGISTER ROUTERS

app.include_router(auth_router)

app.include_router(project_router)

app.include_router(task_router)

app.include_router(dashboard_router)

app.include_router(notification_router)

app.include_router(comment_router)

app.include_router(websocket_router)

app.include_router(user_router)

app.include_router(admin_router)

app.include_router(tag_router)

app.include_router(activity_log_router)

app.include_router(team_router)

app.include_router(analytics_router)

app.include_router(ai_router)

# ROOT ROUTE

@app.get("/")
def home():

    return {

        "message": "Enterprise Team Task Manager API Running",

        "status": "healthy"
    }

# HEALTH CHECK

@app.get("/health")
def health_check():

    return {

        "status": "healthy",

        "database": "connected",

        "api": "running"
    }