# Enterprise-Grade Django Personal Portfolio Web App
### Architected for **Arvin Roman Agramon** | Senior Software Engineer & Enterprise Architect

An enterprise-ready personal portfolio web application built with **Django 5.x**, **Tailwind CSS**, **Alpine.js**, and **Lucide Icons**. Showcases the 15+ year career, core competencies, and architectural achievements of **Arvin Roman Agramon**, an enterprise Senior Software Engineer specializing in .NET Core, Cloud Microservices (AWS & Azure), Systems Integration (SAP, Entra ID, Payments), and AI/RAG Solutions.

---

## 🌟 Key Features

1. **Clean Architecture & Dynamic ORM Backend**:
   - Built on Django ORM with models for `CandidateProfile`, `SkillCategory`, `Skill`, `Experience`, `Project`, and `ContactMessage`.
   - SQLite development by default, ready for PostgreSQL in production via environment configuration.
2. **Deterministic CV Seeding (`python manage.py seed_cv`)**:
   - Comprehensive management command that synchronizes Arvin's complete CV data into the database in seconds.
3. **Executive UI/UX Design**:
   - Modern Tailwind CSS design system with Dark and Light mode toggles persisted in `localStorage`.
   - Polished responsive layouts, subtle glowing accents, and crisp typography (`Inter` + `JetBrains Mono`).
4. **Interactive Competencies & Tech Matrix**:
   - Tabbed taxonomy (Backend & Frameworks, AI & Integrations, Databases & Storage, Cloud & DevOps, Frontend, Practices & Architecture) with proficiency bars and core badges.
5. **Filterable Experience Timeline**:
   - Keyword filtering (All, AI & RAG, Enterprise & SAP, Cloud & Migration, Full-Stack) and expandable accordion for earlier career history (2009–2020).
6. **Architectural Case Studies Drawer / Modal**:
   - Deep-dive popups displaying problem statements, engineered solutions, architecture highlights, metrics, and technology stacks.
7. **Print-Optimized / ATS Resume View (`/resume/`)**:
   - Dedicated clean view formatted for ATS readers and 1-click browser printing/PDF export via `@media print`.
8. **Interactive Contact Form with Honeypot Bot Defense**:
   - CSRF protected, validated contact form with invisible honeypot trap to eliminate spam without captcha friction.

---

## 📂 Project Structure

```text
django made portfolio/
├── config/                         # Django project core configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                 # Environment-aware settings (PostgreSQL/SQLite, SMTP)
│   ├── urls.py                     # Root routing & admin branding
│   └── wsgi.py
├── portfolio/                      # Main portfolio application
│   ├── management/
│   │   └── commands/
│   │       ├── __init__.py
│   │       └── seed_cv.py          # Custom management command populating full CV data
│   ├── migrations/                 # Database schema migrations
│   ├── admin.py                    # Custom Django Admin with filters & inlines
│   ├── apps.py
│   ├── forms.py                    # Contact form with honeypot validation
│   ├── models.py                   # Data models (Profile, Skill, Experience, Project, Inquiries)
│   ├── tests.py                    # Unit & integration test suite (9 tests, 100% passing)
│   ├── urls.py                     # App routing
│   └── views.py                    # Views (HomeView, ResumeView, project_detail_api)
├── static/
│   ├── css/
│   │   └── custom.css              # Custom scrollbars, glassmorphism, @media print
│   ├── js/
│   │   └── main.js                 # Theme toggler, Lucide icons, toast auto-dismiss
│   └── img/
├── templates/
│   ├── base.html                   # Master layout with navbar, theme switch, footer
│   └── portfolio/
│       ├── index.html              # Main landing page (Hero, Skills, Timeline, Projects, Contact)
│       └── resume.html             # ATS-compliant printable CV view
├── .env.example                    # Sample environment variables
├── .gitignore                      # Git ignore rules
├── manage.py                       # Django CLI entrypoint
├── PROMPT.md                       # Single source of truth prompt specifications
├── requirements.txt                # Python project dependencies
└── README.md                       # Project documentation
```

---

## 🚀 Quickstart Guide

### 1. Prerequisites
- Python 3.9+ (or Python 3.11+)
- Virtual environment tool (`venv`)

### 2. Setup Virtual Environment & Install Dependencies
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# Linux / macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Initialize Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Seed Arvin Roman Agramon's CV
```bash
python manage.py seed_cv
```
*Output:*
```text
Beginning CV database seeding...
Candidate profile synced: Arvin Roman Agramon
Skill categories and competencies synced.
Synced 13 professional experience records.
Synced 5 featured architectural case studies.

Database successfully seeded with Arvin Roman Agramon's complete CV!
```

### 5. Create Superuser (Optional for Django Admin)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

Open your browser to:
- **Portfolio Web Application**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Printable ATS Resume View**: [http://127.0.0.1:8000/resume/](http://127.0.0.1:8000/resume/)
- **Admin Control Center**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🧪 Running Automated Tests

Run the test suite covering models, seeding idempotency, views, JSON APIs, and contact form security:
```bash
python manage.py test
```

---

## 📄 License & Attribution
Architected and configured for **Arvin Roman Agramon** | Senior Software Engineer & Enterprise Architect.
Built with Django 5.x, Tailwind CSS, Alpine.js, and Lucide.
