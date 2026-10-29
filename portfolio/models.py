from django.db import models
from django.utils.text import slugify


class CandidateProfile(models.Model):
    """
    Candidate profile representing the personal and professional bio
    of Arvin Roman Agramon.
    """
    name = models.CharField(max_length=150, default="Arvin Roman Agramon")
    title = models.CharField(
        max_length=255, 
        default="Senior Software Engineer | Full-Stack & Cloud Integration Specialist"
    )
    summary = models.TextField(
        help_text="Executive summary highlighting core background and philosophy"
    )
    email = models.EmailField(default="aragramon@gmail.com")
    phone = models.CharField(max_length=50, default="+639278414288")
    location = models.CharField(max_length=100, default="Philippines")
    key_tags = models.CharField(
        max_length=255, 
        blank=True, 
        default="#NetCore, #Fullstack, #AgileDelivery, #EnterpriseArchitecture, #AIRAG",
        help_text="Comma-separated hashtag badges"
    )
    education_degree = models.CharField(
        max_length=255, 
        default="Bachelor of Science in Computer Science"
    )
    education_school = models.CharField(
        max_length=255, 
        default="STI College, Philippines"
    )
    education_year = models.CharField(max_length=50, default="Graduated: 2009")
    years_of_experience = models.PositiveIntegerField(default=15)
    github = models.URLField(blank=True, default="https://github.com/akosiar2")
    linkedin = models.URLField(blank=True, default="https://linkedin.com/in/arvin-agramon")
    resume_file = models.FileField(upload_to="resumes/", blank=True, null=True)
    avatar_url = models.CharField(
        max_length=500, 
        blank=True, 
        help_text="External URL or path to professional headshot image"
    )

    class Meta:
        verbose_name = "Candidate Profile"
        verbose_name_plural = "Candidate Profile"

    def __str__(self):
        return f"{self.name} - {self.title}"

    def get_tags_list(self):
        if not self.key_tags:
            return []
        return [tag.strip() for tag in self.key_tags.split(",") if tag.strip()]

    def get_initials(self):
        parts = self.name.split()
        if len(parts) >= 3:
            return f"{parts[0][0]}{parts[1][0]}{parts[2][0]}".upper()
        elif len(parts) == 2:
            return f"{parts[0][0]}{parts[1][0]}".upper()
        return self.name[:2].upper()


class SkillCategory(models.Model):
    """
    Skill category such as:
    - Backend & Frameworks
    - AI & Integrations
    - Databases & Storage
    - Cloud & DevOps
    - Frontend
    - Practices & Architecture
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    icon_name = models.CharField(
        max_length=50, 
        default="code", 
        help_text="Lucide icon identifier (e.g. server, cpu, database, cloud, layout, shield-check)"
    )

    class Meta:
        ordering = ["order", "name"]
        verbose_name_plural = "Skill Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Skill(models.Model):
    """
    Individual technical skill with proficiency level and category association.
    """
    category = models.ForeignKey(
        SkillCategory, 
        on_delete=models.CASCADE, 
        related_name="skills"
    )
    name = models.CharField(max_length=100)
    proficiency_percentage = models.PositiveIntegerField(
        default=90, 
        help_text="Estimated proficiency from 1 to 100"
    )
    is_primary = models.BooleanField(
        default=True, 
        help_text="Primary core competency vs secondary proficiency"
    )
    is_featured = models.BooleanField(
        default=False, 
        help_text="Display prominently on hero/overview badges"
    )
    icon_name = models.CharField(
        max_length=50, 
        blank=True, 
        help_text="Lucide icon name (optional)"
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-proficiency_percentage", "name"]

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Experience(models.Model):
    """
    Professional career timeline entry.
    """
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True, default="Remote / Hybrid")
    start_date = models.CharField(max_length=50, help_text="e.g. Sep 2025")
    end_date = models.CharField(
        max_length=50, 
        blank=True, 
        default="Present", 
        help_text="e.g. Sep 2026 or Present"
    )
    is_current = models.BooleanField(default=False)
    is_earlier = models.BooleanField(
        default=False, 
        help_text="Mark True for grouped earlier career records (2009-2020)"
    )
    context = models.TextField(
        blank=True, 
        help_text="Industry/domain context (e.g. Australian packaging leader, InsurTech SaaS)"
    )
    description = models.TextField(blank=True)
    bullet_points = models.JSONField(
        default=list, 
        blank=True, 
        help_text="List of key architectural deliverable bullet points"
    )
    tech_stack = models.CharField(
        max_length=500, 
        blank=True, 
        help_text="Comma-separated technologies utilized"
    )
    category_tag = models.CharField(
        max_length=100, 
        default="Enterprise", 
        help_text="Filter tag: 'AI & RAG', 'Cloud & Migration', 'Enterprise & SAP', 'Full-Stack'"
    )
    company_url = models.URLField(blank=True)
    order = models.IntegerField(
        default=0, 
        help_text="Sorting order (lower numbers display first)"
    )

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self):
        return f"{self.role} at {self.company} ({self.start_date} - {self.end_date})"

    def get_tech_stack_list(self):
        if not self.tech_stack:
            return []
        return [t.strip() for t in self.tech_stack.split(",") if t.strip()]

    def get_bullet_points_list(self):
        if isinstance(self.bullet_points, list):
            return self.bullet_points
        return []


class Project(models.Model):
    """
    Featured enterprise project and architectural case study.
    """
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    company_name = models.CharField(
        max_length=200, 
        blank=True, 
        help_text="Company or client associated with project"
    )
    category = models.CharField(
        max_length=100, 
        default="Enterprise Architecture", 
        help_text="e.g. AI & RAG, Cloud Modernization, Systems Integration"
    )
    problem_statement = models.TextField(
        help_text="Business challenge and architectural bottlenecks faced"
    )
    solution_summary = models.TextField(
        help_text="Engineered solution, technical approach, and design decisions"
    )
    architecture_highlights = models.TextField(
        blank=True, 
        help_text="Key architecture points (SOLID, microservices, async workflows)"
    )
    key_features = models.JSONField(
        default=list, 
        blank=True, 
        help_text="List of notable deliverables and feature highlights"
    )
    tech_stack = models.CharField(
        max_length=500, 
        help_text="Comma-separated list of technologies"
    )
    external_url = models.URLField(blank=True)
    metrics = models.CharField(
        max_length=255, 
        blank=True, 
        help_text="Impact summary (e.g. 'Reduced latency by 45%', 'Zero-downtime cutover')"
    )
    is_featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.company_name})"

    def get_tech_stack_list(self):
        if not self.tech_stack:
            return []
        return [t.strip() for t in self.tech_stack.split(",") if t.strip()]

    def get_key_features_list(self):
        if isinstance(self.key_features, list):
            return self.key_features
        return []


class ContactMessage(models.Model):
    """
    Inbound messages received via the contact form.
    """
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Inquiry"
        verbose_name_plural = "Contact Inquiries"

    def __str__(self):
        return f"Message from {self.name} <{self.email}> at {self.created_at:%Y-%m-%d %H:%M}"
