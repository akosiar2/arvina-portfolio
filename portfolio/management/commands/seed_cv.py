from django.core.management.base import BaseCommand
from portfolio.models import (
    CandidateProfile,
    SkillCategory,
    Skill,
    Experience,
    Project,
)


class Command(BaseCommand):
    help = "Seeds candidate profile, core competencies, professional experience, and architectural projects from Arvin Roman Agramon's CV."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Beginning CV database seeding..."))

        # 1. Candidate Profile
        profile_data = {
            "name": "Arvin Roman Agramon",
            "title": "Senior Software Engineer | Full-Stack & Cloud Integration Specialist",
            "summary": (
                "Senior .NET & Full-Stack Software Engineer with extensive experience developing enterprise APIs, "
                "database-driven applications, and system integrations. Skilled in C#, ASP.NET Core, Entity Framework Core, "
                "Dapper, SQL Server, MySQL, Sybase ASE, with strong experience integrating SAP services and Microsoft Entra ID / "
                "Azure B2C. Experienced in modernizing legacy applications and reporting platforms, implementing AI/RAG solutions, "
                "troubleshooting complex production issues, and delivering secure, scalable backend services across enterprise environments."
            ),
            "email": "aragramon@gmail.com",
            "phone": "+639278414288",
            "location": "Philippines",
            "key_tags": "#NetCore, #Fullstack, #AgileDelivery, #EnterpriseArchitecture, #AIRAG",
            "education_degree": "Bachelor of Science in Computer Science",
            "education_school": "STI College, Philippines",
            "education_year": "Graduated: 2009",
            "years_of_experience": 15,
            "github": "https://github.com/akosiar2",
            "linkedin": "https://linkedin.com/in/arvin-agramon",
            "avatar_url": "",
        }

        profile, created = CandidateProfile.objects.update_or_create(
            email=profile_data["email"],
            defaults=profile_data,
        )
        self.stdout.write(self.style.SUCCESS(f"Candidate profile synced: {profile.name}"))

        # 2. Skill Categories and Core Competencies Matrix
        categories_data = [
            {
                "name": "Backend & Frameworks",
                "slug": "backend-frameworks",
                "order": 1,
                "icon_name": "server",
                "skills": [
                    {"name": "C#", "proficiency_percentage": 96, "is_primary": True, "is_featured": True},
                    {"name": "ASP.NET Core", "proficiency_percentage": 95, "is_primary": True, "is_featured": True},
                    {"name": "Entity Framework Core", "proficiency_percentage": 94, "is_primary": True, "is_featured": True},
                    {"name": "Dapper", "proficiency_percentage": 92, "is_primary": True, "is_featured": False},
                    {"name": "ASP.NET MVC", "proficiency_percentage": 92, "is_primary": True, "is_featured": False},
                    {"name": "Python / Django", "proficiency_percentage": 88, "is_primary": True, "is_featured": True},
                    {"name": "RESTful Web APIs", "proficiency_percentage": 95, "is_primary": True, "is_featured": True},
                    {"name": "SOAP Web Services", "proficiency_percentage": 90, "is_primary": False, "is_featured": False},
                    {"name": "NPoco", "proficiency_percentage": 88, "is_primary": False, "is_featured": False},
                    {"name": "VB.NET", "proficiency_percentage": 85, "is_primary": False, "is_featured": False},
                ],
            },
            {
                "name": "AI & Integrations",
                "slug": "ai-integrations",
                "order": 2,
                "icon_name": "bot",
                "skills": [
                    {"name": "OpenAI API & LLM Agents", "proficiency_percentage": 92, "is_primary": True, "is_featured": True},
                    {"name": "Retrieval-Augmented Generation (RAG)", "proficiency_percentage": 90, "is_primary": True, "is_featured": True},
                    {"name": "Vector Embeddings & Knowledge Bases", "proficiency_percentage": 88, "is_primary": True, "is_featured": False},
                    {"name": "SAP RFC / SOAP Services", "proficiency_percentage": 92, "is_primary": True, "is_featured": True},
                    {"name": "Microsoft Entra ID / Azure B2C", "proficiency_percentage": 90, "is_primary": True, "is_featured": True},
                    {"name": "Adyen Payments", "proficiency_percentage": 88, "is_primary": True, "is_featured": False},
                    {"name": "SendGrid Transactional Email", "proficiency_percentage": 90, "is_primary": False, "is_featured": False},
                    {"name": "Google Maps Directions API", "proficiency_percentage": 88, "is_primary": False, "is_featured": False},
                    {"name": "PayPal API", "proficiency_percentage": 85, "is_primary": False, "is_featured": False},
                ],
            },
            {
                "name": "Databases & Storage",
                "slug": "databases-storage",
                "order": 3,
                "icon_name": "database",
                "skills": [
                    {"name": "SQL Server / T-SQL", "proficiency_percentage": 95, "is_primary": True, "is_featured": True},
                    {"name": "Query Optimization & Profiling", "proficiency_percentage": 94, "is_primary": True, "is_featured": True},
                    {"name": "PostgreSQL", "proficiency_percentage": 90, "is_primary": True, "is_featured": False},
                    {"name": "MySQL", "proficiency_percentage": 90, "is_primary": True, "is_featured": False},
                    {"name": "Sybase ASE", "proficiency_percentage": 86, "is_primary": False, "is_featured": False},
                    {"name": "Supabase (pgvector)", "proficiency_percentage": 88, "is_primary": True, "is_featured": False},
                    {"name": "SQLite", "proficiency_percentage": 90, "is_primary": False, "is_featured": False},
                    {"name": "Complex Stored Procedures", "proficiency_percentage": 92, "is_primary": True, "is_featured": False},
                ],
            },
            {
                "name": "Cloud & DevOps",
                "slug": "cloud-devops",
                "order": 4,
                "icon_name": "cloud",
                "skills": [
                    {"name": "Microsoft Azure (App Services, Functions)", "proficiency_percentage": 92, "is_primary": True, "is_featured": True},
                    {"name": "AWS (ECS, ECR, CodePipeline)", "proficiency_percentage": 88, "is_primary": True, "is_featured": True},
                    {"name": "Docker & Containerization", "proficiency_percentage": 90, "is_primary": True, "is_featured": True},
                    {"name": "Git & GitHub Actions CI/CD", "proficiency_percentage": 92, "is_primary": True, "is_featured": False},
                    {"name": "Azure DevOps / TFS", "proficiency_percentage": 90, "is_primary": True, "is_featured": False},
                    {"name": "Windows Server & IIS", "proficiency_percentage": 92, "is_primary": False, "is_featured": False},
                ],
            },
            {
                "name": "Frontend & UI",
                "slug": "frontend-ui",
                "order": 5,
                "icon_name": "layout",
                "skills": [
                    {"name": "Blazor (Server & WebAssembly)", "proficiency_percentage": 92, "is_primary": True, "is_featured": True},
                    {"name": "HTML5 / CSS3 / Tailwind CSS", "proficiency_percentage": 90, "is_primary": True, "is_featured": True},
                    {"name": "JavaScript (ES6+) & TypeScript", "proficiency_percentage": 90, "is_primary": True, "is_featured": False},
                    {"name": "React.js", "proficiency_percentage": 86, "is_primary": True, "is_featured": False},
                    {"name": "Bootstrap", "proficiency_percentage": 90, "is_primary": False, "is_featured": False},
                    {"name": "jQuery", "proficiency_percentage": 92, "is_primary": False, "is_featured": False},
                    {"name": "AngularJS", "proficiency_percentage": 85, "is_primary": False, "is_featured": False},
                ],
            },
            {
                "name": "Practices & Architecture",
                "slug": "practices-architecture",
                "order": 6,
                "icon_name": "shield-check",
                "skills": [
                    {"name": "SOLID Principles & Clean Architecture", "proficiency_percentage": 96, "is_primary": True, "is_featured": True},
                    {"name": "Microservices & Cloud-Native Patterns", "proficiency_percentage": 92, "is_primary": True, "is_featured": True},
                    {"name": "Test-Driven Development (NUnit)", "proficiency_percentage": 90, "is_primary": True, "is_featured": False},
                    {"name": "OWASP Top 10 Security & RBAC", "proficiency_percentage": 92, "is_primary": True, "is_featured": True},
                    {"name": "High-Volume Performance Tuning", "proficiency_percentage": 94, "is_primary": True, "is_featured": False},
                    {"name": "Agile / Scrum Delivery", "proficiency_percentage": 95, "is_primary": True, "is_featured": False},
                ],
            },
        ]

        for cat_data in categories_data:
            skills = cat_data.pop("skills")
            cat_obj, _ = SkillCategory.objects.update_or_create(
                slug=cat_data["slug"],
                defaults=cat_data,
            )
            for idx, skill_info in enumerate(skills, start=1):
                Skill.objects.update_or_create(
                    category=cat_obj,
                    name=skill_info["name"],
                    defaults={
                        "proficiency_percentage": skill_info["proficiency_percentage"],
                        "is_primary": skill_info["is_primary"],
                        "is_featured": skill_info["is_featured"],
                        "order": idx,
                    },
                )
        self.stdout.write(self.style.SUCCESS("Skill categories and competencies synced."))

        # 3. Professional Experience Records
        experiences_data = [
            {
                "company": "Visy Industries",
                "role": "Senior Application Developer",
                "location": "Melbourne, Australia (Remote)",
                "start_date": "Sep 2025",
                "end_date": "Sep 2026",
                "is_current": True,
                "is_earlier": False,
                "order": 1,
                "category_tag": "Enterprise & SAP",
                "context": "Major Australian packaging, recycling, and resource recovery leader operating across Australasia.",
                "description": "Led backend modernization initiatives, SAP enterprise connectivity, and complex multi-database reporting transformations.",
                "bullet_points": [
                    "Modernized legacy reporting systems by transitioning mission-critical Crystal Reports workloads to high-throughput .NET Web APIs and Vue.js-compatible endpoints.",
                    "Engineered deep SAP integrations using custom SOAP/XML request/response construction, RFC-style interfaces, and secure HTTP authentication protocols.",
                    "Configured Microsoft Entra ID / Azure B2C custom user flows and Microsoft Graph API integrations for federated identity and user lookup across corporate services.",
                    "Optimized high-volume database operations across Sybase ASE, SQL Server, and MySQL through EF Core view mapping, Dapper raw queries, and query execution plan tuning.",
                    "Containerized microservices utilizing Docker and deployed robust pipelines to AWS ECS/ECR."
                ],
                "tech_stack": "VueJS, Typescript, C#, ASP.NET Core, EF Core, Dapper, SQL Server, MySQL, Sybase ASE, SAP RFC, AWS ECS/ECR, Docker",
                "company_url": "https://www.visy.com.au",
            },
            {
                "company": "MissionLens",
                "role": "Full Stack .NET Developer",
                "location": "Remote",
                "start_date": "Oct 2025",
                "end_date": "Feb 2026",
                "is_current": False,
                "is_earlier": False,
                "order": 2,
                "category_tag": "AI & RAG",
                "context": "AI chat agents & automation solutions provider empowering non-profit and enterprise organizations.",
                "description": "Architected conversational AI pipelines, vector database integrations, and interactive Blazor administrative portals.",
                "bullet_points": [
                    "Engineered enterprise Retrieval-Augmented Generation (RAG) pipelines leveraging OpenAI API embeddings and Supabase pgvector for compliant knowledge base Q&A.",
                    "Developed responsive, modular Blazor components and administrative interfaces for monitoring AI agent conversations and confidence metrics.",
                    "Architected unified multi-channel conversational help desk ticketing, dispatching automated notifications via SMS, email, and live web chat.",
                    "Enforced enterprise security policies with Role-Based Access Control (RBAC), JWT token lifecycle management, and OWASP-compliant endpoints."
                ],
                "tech_stack": "ASP.NET Web API, C#, Blazor, Entity Framework, OpenAI API, RAG, Supabase (pgvector), PostgreSQL, AWS, Windows Server 2022, Bootstrap",
                "company_url": "https://missionlens.org",
            },
            {
                "company": "OnBoard Outsourcing (Equity Transport Group)",
                "role": "Full Stack .NET Developer",
                "location": "Melbourne, Australia / Philippines (Remote)",
                "start_date": "Jun 2024",
                "end_date": "May 2025",
                "is_current": False,
                "is_earlier": False,
                "order": 3,
                "category_tag": "Full-Stack",
                "context": "Leading Australian corporate freight, logistics, and executive transportation provider.",
                "description": "Developed dynamic fleet routing engines, real-time dispatch systems, and international payment orchestration.",
                "bullet_points": [
                    "Built customer-facing booking portals integrating Google Maps Directions & Distance Matrix APIs for real-time route calculation and dynamic tiered pricing.",
                    "Engineered an interactive Blazor Server fleet scheduling and driver job management portal used by 24/7 operations teams.",
                    "Integrated Adyen Payment gateway supporting credit cards, digital wallets, and alternative regional payment mechanisms with webhook idempotency.",
                    "Prototyped ChatGPT conversational dispatch workflows to streamline customer booking modifications and automated status updates."
                ],
                "tech_stack": "ASP.NET MVC, C#, EF Core, Blazor Server, Google Maps API, Adyen Payments, Azure, Entra ID, GitHub Copilot",
                "company_url": "https://equitytransport.com.au",
            },
            {
                "company": "Zywave",
                "role": "Software Engineer",
                "location": "Remote",
                "start_date": "Jan 2024",
                "end_date": "Jun 2024",
                "is_current": False,
                "is_earlier": False,
                "order": 4,
                "category_tag": "Enterprise & SAP",
                "context": "Premier US InsurTech SaaS provider serving over 15,000 insurance brokerages, agencies, and carriers.",
                "description": "Engineered high-reliability rating engine microservices and standardized insurance schema transformation layers.",
                "bullet_points": [
                    "Constructed SOLID C# class libraries and versioned RESTful & SOAP Web Services for complex commercial policy quoting and risk rating.",
                    "Designed and maintained bi-directional XML/JSON transformation schemas for automotive and property casualty insurance workflows.",
                    "Collaborated in Agile sprints to eliminate performance bottlenecks in rating calculations, adhering to strict enterprise SLAs."
                ],
                "tech_stack": "C#, ASP.NET, REST APIs, SOAP, XML/JSON Schemas, Windows Server, NUnit",
                "company_url": "https://www.zywave.com",
            },
            {
                "company": "EMAPTA (Springboard Research Ltd.)",
                "role": "Senior ASP.Net Developer",
                "location": "Philippines / Global Offshore",
                "start_date": "Jun 2022",
                "end_date": "Jan 2024",
                "is_current": False,
                "is_earlier": False,
                "order": 5,
                "category_tag": "Enterprise & SAP",
                "context": "High-volume retail intelligence and IoT footfall analytics platform tracking millions of daily consumer visits.",
                "description": "Supervised data visualization dashboards, micro-ORM performance optimization, and rigorous security audits.",
                "bullet_points": [
                    "Enhanced retail analytics dashboards with complex multi-tenant drill-down filters, improving large datatable rendering speeds by over 40%.",
                    "Adopted Test-Driven Development (TDD) using NUnit and enforced OWASP security defenses against cross-site scripting (XSS) and injection vulnerabilities.",
                    "Tuned SQL Server stored procedures, indexes, and NPoco/EF micro-ORM queries handling hundreds of millions of raw sensor timestamps."
                ],
                "tech_stack": "ASP.NET, Entity Framework, NPoco, NUnit, AngularJS, jQuery, NodeJS, SQL Server",
                "company_url": "https://emapta.com",
            },
            {
                "company": "CoDev",
                "role": "C# .NET Developer",
                "location": "Cebu, Philippines",
                "start_date": "Mar 2021",
                "end_date": "Sep 2022",
                "is_current": False,
                "is_earlier": False,
                "order": 6,
                "category_tag": "Cloud & Migration",
                "context": "Global tech talent offshore staffing platform connecting US startups with senior engineering teams.",
                "description": "Built core enterprise portals and implemented centralized Single Sign-On (SSO) architecture.",
                "bullet_points": [
                    "Engineered HRIS features across internal and external portals (internal.codev.com and customer.codev.com) serving thousands of staff.",
                    "Spearheaded IdentityServer implementation providing centralized OAuth2/OIDC token-based Single Sign-On across all corporate applications.",
                    "Configured SendGrid automated transactional workflows and wrote extensive automated test coverage ensuring regression-free bi-weekly releases."
                ],
                "tech_stack": "ASP.NET Core, C#, IdentityServer, React.js, Azure Cloud, SendGrid API",
                "company_url": "https://www.codev.com",
            },
            {
                "company": "iLucent Outsource Solutions",
                "role": "Senior Software Developer",
                "location": "Philippines",
                "start_date": "Sep 2020",
                "end_date": "Jan 2021",
                "is_current": False,
                "is_earlier": False,
                "order": 7,
                "category_tag": "Cloud & Migration",
                "context": "Specialized US healthcare business process and medical software development provider.",
                "description": "Engineered electronic healthcare claims processing and cloud serverless migrations.",
                "bullet_points": [
                    "Delivered mission-critical medical billing and claims adjudication workflows for the MBH Healthcare Software suite.",
                    "Led the lift-and-shift migration of on-premise Windows Server environments to Microsoft Azure and Azure Serverless Functions.",
                    "Maintained automated build and release pipelines utilizing Azure DevOps and TFS."
                ],
                "tech_stack": "ASP.NET, C#, Azure Functions, Dynamics 365, Azure DevOps, TFS",
                "company_url": "",
            },
            {
                "company": "LemonTech IT Solutions",
                "role": "Senior Software Developer",
                "location": "Philippines",
                "start_date": "May 2020",
                "end_date": "Aug 2020",
                "is_current": False,
                "is_earlier": False,
                "order": 8,
                "category_tag": "Full-Stack",
                "context": "Enterprise consulting and bespoke digital transformation agency.",
                "description": "Architected dynamic settings management system and geospatial visualization tools.",
                "bullet_points": [
                    "Created an extensible dynamic settings CRUD metadata engine supporting runtime configuration without application restarts.",
                    "Integrated Google Maps geospatial coordinates with interactive React.js telemetry dashboards."
                ],
                "tech_stack": ".NET Core, C#, React.js, Microsoft SQL Server, Google Maps API, Tableau",
                "company_url": "",
            },
            # Earlier Career Experience Records (2009–2020)
            {
                "company": "C9 Creative Digital Solutions",
                "role": "Software Support Engineer",
                "location": "Philippines",
                "start_date": "Dec 2019",
                "end_date": "May 2020",
                "is_current": False,
                "is_earlier": True,
                "order": 9,
                "category_tag": "Enterprise & SAP",
                "context": "Support & feature maintenance for YouLend UK fintech portal.",
                "description": "Maintained multi-tenant financial application code built upon ASP.NET Boilerplate / ASP.NET Zero.",
                "bullet_points": [
                    "Resolved high-priority production escalations for YouLend merchant lending platform.",
                    "Extended ASP.NET Zero modular authorization and tenant management services."
                ],
                "tech_stack": "ASP.NET Boilerplate, ASP.NET Zero, C#, Angular, SQL Server",
                "company_url": "",
            },
            {
                "company": "Sourcecloud Ltd",
                "role": "Software Engineer",
                "location": "UK / Remote",
                "start_date": "Dec 2016",
                "end_date": "Jan 2020",
                "is_current": False,
                "is_earlier": True,
                "order": 10,
                "category_tag": "Cloud & Migration",
                "context": "UK cloud software consultancy behind HR4UK SaaS management platform.",
                "description": "Built core SaaS reporting services and document automation tools deployed on AWS.",
                "bullet_points": [
                    "Engineered cloud document generation pipelines and reporting engines on AWS.",
                    "Maintained client payroll and employment compliance portals."
                ],
                "tech_stack": "C#, ASP.NET, MVC, Javascript, JQuery, AWS EC2/S3, SQL Server, HTML5/CSS3",
                "company_url": "",
            },
            {
                "company": "Syslogix Inc.",
                "role": "Software Engineer",
                "location": "Philippines",
                "start_date": "Oct 2013",
                "end_date": "Jul 2019",
                "is_current": False,
                "is_earlier": True,
                "order": 11,
                "category_tag": "Enterprise & SAP",
                "context": "Enterprise desktop, client-server, and web application solutions provider.",
                "description": "Developed ERP modules, database stored procedures, and financial transaction software.",
                "bullet_points": [
                    "Designed robust relational databases and transaction procedures in Microsoft SQL Server.",
                    "Delivered desktop and web accounting and inventory management software."
                ],
                "tech_stack": "C#, VB.NET, ASP.NET, WinForms, SQL Server, Crystal Reports",
                "company_url": "",
            },
            {
                "company": "Westkerbel LLC",
                "role": "Web Developer",
                "location": "Remote / USA",
                "start_date": "Jan 2012",
                "end_date": "Dec 2013",
                "is_current": False,
                "is_earlier": True,
                "order": 12,
                "category_tag": "Full-Stack",
                "context": "Digital media and dynamic web agency.",
                "description": "Built custom content management systems and dynamic database interfaces.",
                "bullet_points": [
                    "Implemented responsive web templates and backend database integrations.",
                    "Configured web hosting and payment processing forms."
                ],
                "tech_stack": "PHP, MySQL, JavaScript, HTML5, CSS3",
                "company_url": "",
            },
            {
                "company": "Hubport Interactive Inc.",
                "role": "Web Developer",
                "location": "Philippines",
                "start_date": "Jun 2009",
                "end_date": "Jan 2012",
                "is_current": False,
                "is_earlier": True,
                "order": 13,
                "category_tag": "Full-Stack",
                "context": "Web and interactive media production company.",
                "description": "Commenced professional career building e-commerce and interactive web portals.",
                "bullet_points": [
                    "Engineered full-stack websites from PSD mockups to relational database backends.",
                    "Created interactive UI modules with jQuery, CSS, and cross-browser standards."
                ],
                "tech_stack": "PHP, MySQL, JavaScript, jQuery, HTML/CSS, Apache",
                "company_url": "",
            },
        ]

        for exp_data in experiences_data:
            Experience.objects.update_or_create(
                company=exp_data["company"],
                role=exp_data["role"],
                start_date=exp_data["start_date"],
                defaults=exp_data,
            )
        self.stdout.write(self.style.SUCCESS(f"Synced {len(experiences_data)} professional experience records."))

        # 4. Featured Projects / Architectural Case Studies
        projects_data = [
            {
                "title": "AI Support Automation & RAG Knowledge Engine",
                "subtitle": "Enterprise Conversational AI with Vector Search & Multi-Channel Dispatch",
                "slug": "ai-support-automation-rag-knowledge-engine",
                "company_name": "MissionLens",
                "category": "AI & RAG",
                "problem_statement": (
                    "Non-profit and community enterprises were overwhelmed by voluminous repetitive support queries, "
                    "leading to multi-day resolution backlogs and compliance hazards when providing unverified policy advice."
                ),
                "solution_summary": (
                    "Architected a secure Retrieval-Augmented Generation (RAG) platform that indexes proprietary policy manuals "
                    "into Supabase pgvector and queries OpenAI LLMs with strict grounding prompts, preventing hallucinations and ensuring "
                    "strict compliance."
                ),
                "architecture_highlights": (
                    "• Token-chunking strategy with OpenAI text-embedding-3-small.\n"
                    "• Similarity search thresholding via pgvector cosine distance.\n"
                    "• Decoupled background queue for multi-channel SMS and email dispatch.\n"
                    "• Dynamic Blazor front-end for human-in-the-loop audit logs."
                ),
                "key_features": [
                    "Semantic search across hundreds of organizational policy documents.",
                    "Deterministic citation generation alongside AI responses.",
                    "Multi-channel webhook routing for SMS (Twilio), email, and web chat.",
                    "Full audit logging and confidence scoring for regulatory compliance."
                ],
                "tech_stack": "ASP.NET Web API, C#, Blazor, Entity Framework, OpenAI API, RAG, Supabase (pgvector), PostgreSQL, AWS, Windows Server 2022, Bootstrap",
                "metrics": "99.2% Policy Accuracy | 70% Ticket Deflection Rate",
                "is_featured": True,
                "order": 1,
            },
            {
                "title": "SAP Integration & Legacy Reporting Modernization",
                "subtitle": "High-Throughput Enterprise API Gateway & Crystal Reports Migration",
                "slug": "sap-integration-legacy-reporting-modernization",
                "company_name": "Visy Industries",
                "category": "Enterprise Architecture",
                "problem_statement": (
                    "Legacy Crystal Reports and scattered Sybase ASE databases were creating catastrophic bottlenecks "
                    "for operations teams requiring real-time inventory, production runs, and recycling telemetry."
                ),
                "solution_summary": (
                    "Re-architected reporting services into modular .NET 8 Web APIs with Dapper and EF Core view mapping. "
                    "Engineered resilient SOAP/XML connectors to SAP ERP with secure RFC handling and automated Microsoft Entra ID authentication."
                ),
                "architecture_highlights": (
                    "• Bi-directional XML/SOAP envelope parser with automated retry circuits.\n"
                    "• Database abstraction supporting Sybase ASE, MySQL, and Microsoft SQL Server concurrently.\n"
                    "• Distributed caching for recurring query execution plans.\n"
                    "• Microsoft Graph user lookup with Azure B2C federated policies."
                ),
                "key_features": [
                    "Sub-second report generation replacing 2-minute Crystal Reports locks.",
                    "Direct SAP ERP inventory query connector with XML schema validation.",
                    "Seamless Azure B2C SSO across all internal factory floor tools.",
                    "Containerized deployments on AWS ECS with zero downtime."
                ],
                "tech_stack": "VueJS, Typescript, C#, ASP.NET Core, EF Core, Dapper, SQL Server, MySQL, Sybase ASE, SAP RFC, AWS ECS/ECR, Docker",
                "metrics": "85% Query Latency Reduction | 100% Uptime Cutover",
                "is_featured": True,
                "order": 2,
            },
            {
                "title": "Logistics Booking Engine & Payment Orchestration",
                "subtitle": "Real-Time Fleet Dispatch with Google Maps Routing & Adyen Gateway",
                "slug": "logistics-booking-engine-payment-orchestration",
                "company_name": "Equity Transport Group",
                "category": "Systems Integration",
                "problem_statement": (
                    "Dispatchers spent excessive manual hours quoting multi-stop trips, calculating toll surcharges, "
                    "and reconciling phone-in credit card payments without secure card storage."
                ),
                "solution_summary": (
                    "Constructed an automated customer booking and pricing engine integrated directly with Google Maps Directions API, "
                    "paired with an Adyen Payment orchestration layer ensuring PCI-DSS compliance and webhook reconciliation."
                ),
                "architecture_highlights": (
                    "• Real-time distance matrix & route optimization factoring dynamic toll rates.\n"
                    "• Blazor Server administrative dashboard with real-time SignalR fleet updates.\n"
                    "• Idempotent webhook receiver for Adyen asynchronous payment authorization.\n"
                    "• ChatGPT conversational bot prototype for automated booking reschedule flows."
                ),
                "key_features": [
                    "Instant accurate fare calculation based on traffic, vehicle type, and tolls.",
                    "Global multi-currency Adyen payment processing with 3D Secure 2.",
                    "Operations dashboard managing hundreds of active vehicles and drivers.",
                    "Automated customer SMS alerts and driver manifest generation."
                ],
                "tech_stack": "ASP.NET MVC, C#, EF Core, Blazor Server, Google Maps API, Adyen API, Azure",
                "metrics": "Instant Pricing Calculations | Zero Payment Discrepancies",
                "is_featured": True,
                "order": 3,
            },
            {
                "title": "Centralized IdentityServer SSO Portal",
                "subtitle": "Enterprise OAuth2/OIDC Federated Authentication across Multi-Tenant Platforms",
                "slug": "centralized-identityserver-sso-portal",
                "company_name": "CoDev",
                "category": "Cloud & Security",
                "problem_statement": (
                    "Employees and external clients were forced to manage fragmented credentials across disjointed "
                    "internal management portals, creating severe administrative friction and security exposure."
                ),
                "solution_summary": (
                    "Designed and deployed an IdentityServer-powered OAuth2/OpenID Connect central identity provider. "
                    "Unified authentication for internal staff and external customer portals with secure token issuance."
                ),
                "architecture_highlights": (
                    "• Token-based SSO with JSON Web Tokens (JWT) and refresh token rotation.\n"
                    "• Role-based granular claim mapping across differing portal scopes.\n"
                    "• SendGrid transactional integration for 2FA and passwordless login.\n"
                    "• Automated NUnit test suites verifying token validation and authorization scopes."
                ),
                "key_features": [
                    "Single credential login spanning internal.codev.com and customer.codev.com.",
                    "Centralized session invalidation and audit compliance logging.",
                    "Seamless React.js SPA token refresh interceptors.",
                    "Automated onboarding and email confirmation pipelines."
                ],
                "tech_stack": "ASP.NET Core, C#, IdentityServer, React.js, Azure Cloud, SendGrid",
                "metrics": "10,000+ Active Users Unified | 99.9% Authentication Reliability",
                "is_featured": True,
                "order": 4,
            },
            {
                "title": "On-Prem to Azure Cloud Modernization",
                "subtitle": "Serverless Healthcare Claims Processing & Windows Server Cloud Migration",
                "slug": "on-prem-to-azure-cloud-modernization",
                "company_name": "iLucent / MBH Healthcare",
                "category": "Cloud Modernization",
                "problem_statement": (
                    "Legacy healthcare billing software running on aging on-premise Windows hardware suffered from "
                    "scalability constraints, licensing overhead, and high risks of hardware failure."
                ),
                "solution_summary": (
                    "Migrated core medical billing workflows to Microsoft Azure App Services and Azure Functions. "
                    "Refactored batch claim processing into event-driven serverless consumers with Azure DevOps CI/CD."
                ),
                "architecture_highlights": (
                    "• Event-driven serverless processing for EDI 837 medical claims.\n"
                    "• Secure connection to Dynamics 365 CRM for customer record synchronization.\n"
                    "• Automated release pipelines via Azure DevOps and TFS.\n"
                    "• Encryption at rest and in transit satisfying strict HIPAA standards."
                ),
                "key_features": [
                    "Serverless scalability scaling to peak billing day spikes automatically.",
                    "Automated insurance claim validation engine with error reporting.",
                    "Zero-downtime blue/green deployment slots on Azure App Services.",
                    "Disaster recovery and automated cloud backup policies."
                ],
                "tech_stack": "ASP.NET, C#, Azure Functions, Azure App Services, Dynamics 365, Azure DevOps",
                "metrics": "40% Infrastructure Cost Reduction | 99.95% Availability",
                "is_featured": True,
                "order": 5,
            },
        ]

        for proj_data in projects_data:
            Project.objects.update_or_create(
                slug=proj_data["slug"],
                defaults=proj_data,
            )
        self.stdout.write(self.style.SUCCESS(f"Synced {len(projects_data)} featured architectural case studies."))

        self.stdout.write(self.style.SUCCESS("\nDatabase successfully seeded with Arvin Roman Agramon's complete CV!"))
