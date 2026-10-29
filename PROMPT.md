# PROMPT: Build an Enterprise-Grade Django Personal Portfolio Web App

## 1. Project Overview & Objective
Act as a Principal Full-Stack Python/Django Architect and UI/UX Designer. Build a modern, high-performance, and responsive personal portfolio web application in **Django 5.x** showcasing the career, expertise, and projects of **Arvin Roman Agramon**, an enterprise Senior Software Engineer with over 15 years of industry experience.

The web app must feature clean code architecture, a dynamic database-backed structure (Django ORM + SQLite/PostgreSQL), a Django admin for content management, a seeding script containing all data from Arvin's CV, and a modern, polished frontend (Tailwind CSS via CDN, Lucide Icons, and Alpine.js for lightweight reactivity).

---

## 2. Technical Stack
- **Backend**: Python 3.11+, Django 5.x
- **Database**: SQLite (default for development) / PostgreSQL-ready
- **Frontend / Styling**: Modern Django Templates (`DTL`), Tailwind CSS (CDN or Tailwind CLI), Alpine.js, Lucide Icons
- **Key Modules**:
  - `django.contrib.admin` (customized with custom filters and search)
  - `django.core.mail` or mock handler for the contact form
  - Database seeding management command (`python manage.py seed_cv`)
  - Dynamic PDF or clean print stylesheet for CV export

---

## 3. Candidate Profile Data (Exact CV Details)

### Personal Information
- **Full Name**: Arvin Roman Agramon
- **Title**: Senior Software Engineer | Full-Stack & Cloud Integration Specialist
- **Email**: aragramon@gmail.com
- **Phone**: +639278414288
- **Location**: Philippines
- **Key Tags**: `#NetCore`, `#Fullstack`, `#AgileDelivery`, `#EnterpriseArchitecture`, `#AIRAG`
- **Education**: Bachelor of Science in Computer Science — STI College, Philippines (Graduated: 2009)

### Executive Summary
> "Senior .NET & Full-Stack Software Engineer with extensive experience developing enterprise APIs, database-driven applications, and system integrations. Skilled in C#, ASP.NET Core, Entity Framework Core, Dapper, SQL Server, MySQL, Sybase ASE, with strong experience integrating SAP services and Microsoft Entra ID / Azure B2C. Experienced in modernizing legacy applications and reporting platforms, implementing AI/RAG solutions, troubleshooting complex production issues, and delivering secure, scalable backend services across enterprise environments."

### Core Competencies Matrix
- **Backend & Frameworks**: C#, ASP.NET Core, ASP.NET MVC, VB.NET, Entity Framework Core, Dapper, NPoco, Python (Django), RESTful APIs, SOAP Web Services
- **AI & Integrations**: OpenAI API, Retrieval-Augmented Generation (RAG), Vector Embeddings, SAP RFC/SOAP Services, Microsoft Entra ID / Azure B2C, Adyen Payments, PayPal API, SendGrid, Google Maps Directions API
- **Databases & Storage**: SQL Server, PostgreSQL, MySQL, Sybase ASE, Supabase, SQLite, Query Optimization, Stored Procedures
- **Cloud & DevOps**: AWS (ECS, ECR, CodePipeline), Microsoft Azure (Functions, App Services, Entra), Docker, Git, Azure DevOps, GitHub Actions, TFS
- **Frontend**: HTML5, CSS3/Tailwind, JavaScript, jQuery, React.js, AngularJS, Blazor (Server & WebAssembly), Bootstrap
- **Practices & Architecture**: SOLID Principles, Microservices & Cloud-Native Patterns, TDD (NUnit), OWASP Top 10 Security, Performance Tuning, Agile/Scrum

### Professional Experience Records
1. **Visy Industries** | *Senior Application Developer* (Sep 2025 – Sep 2026)
   - *Context*: Major Australian packaging, recycling, and resource recovery leader.
   - *Key Deliverables*:
     - Modernized legacy reporting systems (Crystal Reports to modern .NET Web APIs and Vue.js-compatible solutions).
     - Integrated SAP services using SOAP/XML request/response construction, RFC-style interfaces, and secure HTTP authentication.
     - Configured Microsoft Entra ID / Azure B2C custom policies and Microsoft Graph user lookup.
     - Optimized EF Core view mapping, Dapper queries, complex joins, and Sybase ASE/SQL Server migrations.
   - *Stack*: C#, ASP.NET Core, EF Core, Dapper, SQL Server, MySQL, Sybase ASE, SAP, AWS ECS/ECR, Docker.

2. **MissionLens** | *Full Stack .NET Developer* (Oct 2025 – Feb 2026)
   - *Context*: AI chat agents & automation solutions for non-profits.
   - *Key Deliverables*:
     - Built modular Blazor-based UI components.
     - Implemented Retrieval-Augmented Generation (RAG) with vector knowledge bases for policy-compliant chatbot answers.
     - Integrated conversational AI help desk ticketing with multi-channel chat, SMS, and email notifications.
     - Implemented RBAC and secure token-based authentication.
   - *Stack*: Web API, C#, Blazor, OpenAI API, RAG, Supabase, AWS, Windows Server 2022, Bootstrap.

3. **Equity Transport Group (OnBoard Outsourcing)** | *Full Stack .NET Developer* (Jun 2024 – May 2025)
   - *Context*: Australian freight, logistics, and transportation provider.
   - *Key Deliverables*:
     - Developed web booking portals integrated with Google Maps Directions API for dynamic route and pricing calculations.
     - Built Blazor Server project management tool for fleet/job scheduling.
     - Integrated Adyen Payment System (cards and alternative payment methods).
     - Prototyped ChatGPT conversational workflows for customer service.
   - *Stack*: ASP.NET MVC, C#, EF Core, Blazor, Google Maps API, Adyen, Azure, Entra ID, GitHub Copilot.

4. **Zywave** | *Software Engineer* (Jan 2024 – Jun 2024)
   - *Context*: Leading InsurTech SaaS provider for insurance brokers and carriers.
   - *Key Deliverables*:
     - Built SOLID C# class libraries and versioned RESTful & SOAP APIs for policy quoting and rating.
     - Designed XML/JSON transformation schemas for automotive/home insurance workflows.
   - *Stack*: C#, ASP.NET, REST APIs, SOAP, XML/JSON, Windows Server.

5. **EMAPTA (Springboard Research Ltd.)** | *Senior ASP.Net Developer* (Jun 2022 – Jan 2024)
   - *Context*: Footfall analytics & retail intelligence platform.
   - *Key Deliverables*:
     - Enhanced retail analytics dashboards, drill-down filters, and datatable performance.
     - Implemented TDD using NUnit and enforced OWASP security practices (XSS, auth validation).
     - Tuned database stored procedures, NPoco, and EF queries for massive datasets.
   - *Stack*: ASP.NET, Entity Framework, NPoco, NUnit, AngularJS, jQuery, NodeJS, SQL Server.

6. **CoDev** | *C# .NET Developer* (Mar 2021 – Sep 2022)
   - *Context*: Global offshore tech staffing platform.
   - *Key Deliverables*:
     - Built HRIS portal features across internal and customer portals (`internal.codev.com`, `customer.codev.com`).
     - Led IdentityServer setup for centralized token-based SSO.
     - Integrated SendGrid transactional emails and wrote comprehensive unit tests.
   - *Stack*: ASP.NET Core, C#, IdentityServer, React.js, Azure, SendGrid.

7. **iLucent Outsource Solutions** | *Senior Software Developer* (Sep 2020 – Jan 2021)
   - *Context*: Healthcare business services & custom software.
   - *Key Deliverables*:
     - Delivered billing and claims workflows for MBH Healthcare Software.
     - Migrated on-premise Windows Server environments to Microsoft Azure and Azure Functions.
   - *Stack*: ASP.NET, C#, Azure Functions, Dynamics 365, Azure DevOps, TFS.

8. **LemonTech IT Solutions** | *Senior Software Developer* (May 2020 – Aug 2020)
   - *Context*: Digital solutions & enterprise consulting.
   - *Key Deliverables*:
     - Created dynamic settings CRUD engine and integrated Google Maps geospatial data with React.js dashboards.
   - *Stack*: .NET Core, C#, React.js, MSSQL, Google Maps API, Tableau.

9. **Earlier Career Experience**:
   - **C9 Creative Digital Solutions** (Dec 2019 – May 2020) – Software Support Engineer (YouLend fintech portal, ASP.NET Zero, Boilerplate).
   - **Sourcecloud Ltd** (Dec 2016 – Jan 2020) – Software Engineer (HR4UK on AWS, SaaS reporting).
   - **Syslogix Inc.** (Oct 2013 – Jul 2019) – Software Engineer.
   - **Westkerbel LLC** (Jan 2012 – Dec 2013) – Web Developer.
   - **Hubport Interactive Inc.** (Jun 2009 – Jan 2012) – Web Developer.

---

## 4. Required Features & Pages

1. **Header / Navbar**:
   - Brand logo/initials (`ARA`), navigation anchors (About, Experience, Skills, Projects, Contact), Dark/Light mode toggle, and a prominent **"Download Resume"** button.

2. **Hero Section**:
   - Compelling headline: *"Senior Software Engineer & Enterprise Architect"*.
   - Subheading highlighting 15+ years of experience bridging enterprise backend systems (.NET / C# / Python), cloud scale (Azure & AWS), and modern AI (RAG & LLM agents).
   - Quick Metrics / Stats cards: `15+ Years Experience`, `10+ Enterprise Systems Delivered`, `SAP & Cloud Certified Integrations`.
   - CTAs: "Explore Experience", "Get In Touch".

3. **Skills & Tech Matrix**:
   - Interactive category tabs (Backend & APIs, Cloud & DevOps, AI & Integrations, Databases, Frontend).
   - Skill chips with visual badges showing primary vs. secondary proficiencies.

4. **Experience Timeline (Interactive)**:
   - Filterable timeline (filter by keywords: e.g. "All", "AI & RAG", "Cloud & Migration", "Enterprise & SAP").
   - Detailed job cards with company, dates, role, bullet points, and tech stack tags.
   - Expandable details for earlier experience (2009–2020).

5. **Featured Projects / Case Studies Showcase**:
   - Cards highlighting top architectural accomplishments:
     1. *AI Support Automation & RAG Knowledge Engine* (MissionLens)
     2. *SAP Integration & Legacy Reporting Modernization* (Visy Industries)
     3. *Logistics Booking Engine & Payment Orchestration* (Equity Transport / Adyen)
     4. *Centralized IdentityServer SSO Portal* (CoDev)
     5. *On-Prem to Azure Cloud Modernization* (iLucent / MBH)
   - Modal popup or expandable drawer displaying Architecture Highlights, Challenges, Solution, and Stack.

6. **Interactive Contact Section**:
   - Working Django form with CSRF validation, email/honeypot spam check, and success flash message.
   - Direct contact links: Email, Phone, and LinkedIn/GitHub placeholders.

7. **Resume Printable View (`/resume/`)**:
   - A dedicated clean, print-optimized HTML view formatted for ATS or 1-click browser printing/PDF export.

---

## 5. Django Data Models Architecture

Design models in `portfolio/models.py` including:
- `CandidateProfile`: Name, title, summary, email, phone, location, github, linkedin, resume_file.
- `SkillCategory`: Name, order (e.g., Backend, Frontend, Cloud & DevOps, AI & Integrations).
- `Skill`: Name, category (FK), proficiency_percentage, is_featured, icon_name.
- `Experience`: Company, role, location, start_date, end_date, is_current, description, bullet_points (JSON or text), tech_stack (comma-separated or M2M), company_url.
- `Project`: Title, subtitle, slug, problem_statement, solution_summary, key_features (JSON), tech_stack, external_url, is_featured.
- `ContactMessage`: Name, email, subject, message, created_at, is_resolved.

---

## 6. Implementation Instructions
1. Provide the complete project structure.
2. Provide all code for `settings.py`, `models.py`, `views.py`, `forms.py`, `admin.py`, and `urls.py`.
3. Provide the custom management command `management/commands/seed_cv.py` containing **all** exact details from Arvin's CV so the portfolio is immediately populated with realistic data upon running `python manage.py seed_cv`.
4. Provide the complete HTML templates (`base.html`, `index.html`, `resume.html`) styled with Tailwind CSS, supporting dark/light mode and mobile responsiveness.
5. Provide setup and execution commands (`venv`, `pip install`, `migrate`, `seed_cv`, `runserver`).
