# SwipeX – Swipe-Based Intelligent Job Discovery and Career Assistance Platform

SwipeX is a swipe-based job discovery and career assistance platform designed to make job searching more interactive, personalized, and convenient.

The platform combines job discovery, saved jobs, applications, recommendations, notifications, application tracking, recruiter workflows, dashboards, and cloud deployment.

## 🎯 Objectives

- Build a swipe-based job discovery platform
- Provide secure authentication
- Allow users to discover, save, and apply for jobs
- Provide personalized job recommendations
- Track application status
- Provide notifications and competition alerts
- Provide dashboards and analytics
- Provide recruiter tools for job posting and applicant management
- Deploy the platform to cloud environments

## ✨ Key Features

### Job Seeker

- Registration and login
- JWT authentication
- Job discovery
- Swipe-based job interaction
- Save jobs
- Apply for jobs
- Track applications
- Personalized recommendations
- Notifications
- Dashboard statistics
- Profile management

### Recruiter

- Recruiter dashboard
- Company profile management
- Post jobs
- Manage jobs
- Edit jobs
- View applicants
- Manage application status
- Recruitment analytics

### Notifications

- Personalized recommendation notifications
- Low-competition job alerts
- User-specific notifications
- Read/unread notification status

### Dashboard & Analytics

- Total job count
- Applied jobs
- Saved jobs
- Pending applications
- Shortlisted applications
- Interview applications
- Rejected applications
- Applicant and competition information

## 🔄 Swipe-Based Job Discovery

SwipeX uses dynamic job cards for interactive job discovery.

### Swipe Right

Express interest in a job and continue with the job workflow.

### Swipe Left

Skip the job and continue discovering other opportunities.

Job cards display:

- Job title
- Company
- Location
- Salary
- Job type
- Experience

## 🧠 Recommendation System

SwipeX provides personalized job recommendations based on the user's saved-job interests.

Advanced AI features such as resume parsing, ATS scoring, skill-gap analysis, and advanced swipe-learning recommendations are planned/future functionality.

## 📋 Application Tracking

Users can apply for jobs and track their application progress.

Application statuses include:

- Pending
- Shortlisted
- Interview
- Rejected

## 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Frontend | React.js |
| Routing | React Router |
| HTTP Client | Axios |
| Styling | Tailwind CSS |
| Backend | Python, Django |
| API | Django REST Framework |
| Database | PostgreSQL |
| Authentication | JWT |
| API Testing | Postman |
| Version Control | Git & GitHub |
| Frontend Deployment | Vercel |
| Backend Deployment | Render |
| Containerization | Docker & Docker Compose |
| IDE | Visual Studio Code |

## 🏗️ System Architecture

```text
Users
  ↓
React Frontend
  ↓
REST API
  ↓
Django REST Backend
  ↓
PostgreSQL Database


SwipeX/
│
├── accounts/
├── backend/
├── companies/
├── jobs/
├── resumes/
├── skills/
├── frontend/
│
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── report_SwipeX_Astha.pdf

🔐 Authentication

SwipeX uses JWT authentication to protect authenticated API endpoints.

Authentication is used for:

Login
Saved jobs
Applications
Recommendations
Notifications
Recruiter operations
🚀 Deployment
Frontend

Vercel is used to host the React frontend.

Backend

Render is used to host the Django REST API.

Database

PostgreSQL on Render is used for production data storage.

Source Control

GitHub is used for source code management and deployment updates.

🧪 Testing

The following areas were tested during development:

Authentication
Protected APIs
Job listing
Saving jobs
Job applications
Application tracking
Notifications
Dashboard statistics
Frontend-backend communication
Production deployment

Postman was used for API testing.

🔮 Future Scope
AI-based resume parsing
ATS compatibility scoring
Resume-job compatibility analysis
Skill-gap analysis
Improved recommendation learning
Real-time notifications
Advanced hiring analytics
GitHub Actions deployment
Improved security and monitoring
Mobile application
📄 Project Report

The detailed project report is available in this repository:

report_SwipeX_Astha.pdf

👩‍💻 Author

Astha Sharma

Branch: AI & Machine Learning