from django.test import TestCase, Client
from django.urls import reverse
from django.core.management import call_command

from .models import (
    CandidateProfile,
    SkillCategory,
    Skill,
    Experience,
    Project,
    ContactMessage,
)
from .forms import ContactForm


class PortfolioEnterpriseTests(TestCase):
    """
    Test suite covering model behavior, seeding, views, and contact validation.
    """

    def setUp(self):
        # Run seeding command so test database has real CV data
        call_command("seed_cv")
        self.client = Client()

    def test_seed_cv_populates_candidate_profile(self):
        """Verify candidate profile is seeded accurately."""
        profile = CandidateProfile.objects.first()
        self.assertIsNotNone(profile)
        self.assertEqual(profile.name, "Arvin Roman Agramon")
        self.assertEqual(profile.email, "aragramon@gmail.com")
        self.assertEqual(profile.phone, "+639278414288")
        self.assertEqual(profile.years_of_experience, 15)
        self.assertIn("STI College", profile.education_school)
        self.assertIn("#NetCore", profile.key_tags)

    def test_seed_cv_populates_skills_and_categories(self):
        """Verify core competencies taxonomy."""
        categories = SkillCategory.objects.all()
        self.assertGreaterEqual(categories.count(), 6)

        backend_cat = SkillCategory.objects.filter(slug="backend-frameworks").first()
        self.assertIsNotNone(backend_cat)
        csharp_skill = backend_cat.skills.filter(name="C#").first()
        self.assertIsNotNone(csharp_skill)
        self.assertTrue(csharp_skill.is_primary)

        ai_cat = SkillCategory.objects.filter(slug="ai-integrations").first()
        self.assertIsNotNone(ai_cat)
        rag_skill = ai_cat.skills.filter(name__icontains="Retrieval-Augmented").first()
        self.assertIsNotNone(rag_skill)

    def test_seed_cv_populates_experiences(self):
        """Verify professional experiences timeline."""
        visy = Experience.objects.filter(company="Visy Industries").first()
        self.assertIsNotNone(visy)
        self.assertEqual(visy.role, "Senior Application Developer")
        self.assertEqual(visy.category_tag, "Enterprise & SAP")
        self.assertGreaterEqual(len(visy.get_bullet_points_list()), 4)

        missionlens = Experience.objects.filter(company="MissionLens").first()
        self.assertIsNotNone(missionlens)
        self.assertEqual(missionlens.category_tag, "AI & RAG")

        earlier_exps = Experience.objects.filter(is_earlier=True)
        self.assertEqual(earlier_exps.count(), 5)

    def test_seed_cv_populates_projects(self):
        """Verify featured architectural projects."""
        projects = Project.objects.filter(is_featured=True)
        self.assertEqual(projects.count(), 5)

        rag_project = Project.objects.filter(slug="ai-support-automation-rag-knowledge-engine").first()
        self.assertIsNotNone(rag_project)
        self.assertEqual(rag_project.company_name, "MissionLens")

    def test_home_view_status_code_and_content(self):
        """Verify main portfolio landing page renders with expected context."""
        response = self.client.get(reverse("portfolio:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Arvin Roman Agramon")
        self.assertContains(response, "Senior Software Engineer")
        self.assertContains(response, "Visy Industries")
        self.assertContains(response, "MissionLens")
        self.assertContains(response, "Equity Transport Group")

    def test_resume_view_status_code_and_print_structure(self):
        """Verify ATS printable CV view renders."""
        response = self.client.get(reverse("portfolio:resume"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Curriculum Vitae")
        self.assertContains(response, "aragramon@gmail.com")
        self.assertContains(response, "STI College")
        self.assertContains(response, "Core Competencies Matrix")

    def test_project_detail_api(self):
        """Verify JSON API endpoint for dynamic modal hydration."""
        rag_project = Project.objects.first()
        response = self.client.get(
            reverse("portfolio:project_detail_api", kwargs={"slug": rag_project.slug})
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["slug"], rag_project.slug)
        self.assertEqual(data["title"], rag_project.title)

    def test_contact_form_valid_submission(self):
        """Verify human inquiry submission persists message and redirects."""
        payload = {
            "name": "Jane Enterprise Recruiter",
            "email": "jane@techcorp.com",
            "subject": "Principal .NET Architect Opportunity",
            "message": "We have an executive role and would love to connect with Arvin.",
            "verification_code": "",  # Empty honeypot
        }
        response = self.client.post(reverse("portfolio:home"), data=payload, follow=True)
        self.assertEqual(response.status_code, 200)

        # Check that message was created in database
        saved_msg = ContactMessage.objects.filter(email="jane@techcorp.com").first()
        self.assertIsNotNone(saved_msg)
        self.assertEqual(saved_msg.name, "Jane Enterprise Recruiter")
        self.assertFalse(saved_msg.is_resolved)

    def test_contact_form_honeypot_bot_rejection(self):
        """Verify spam bots that fill honeypot field get rejected."""
        payload = {
            "name": "Spam Bot",
            "email": "bot@spamcorp.com",
            "subject": "Spam Promotion",
            "message": "Click here to buy stuff",
            "verification_code": "I am a malicious bot",
        }
        response = self.client.post(reverse("portfolio:home"), data=payload)
        self.assertEqual(response.status_code, 200)

        # Verify bot submission was blocked from database
        self.assertFalse(ContactMessage.objects.filter(email="bot@spamcorp.com").exists())
