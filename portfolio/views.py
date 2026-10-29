import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse, Http404

from .models import (
    CandidateProfile,
    SkillCategory,
    Skill,
    Experience,
    Project,
    ContactMessage
)
from .forms import ContactForm


def get_client_ip(request):
    """Safely obtain the client's IP address behind potential proxies."""
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


class HomeView(View):
    """
    Main portfolio landing page view.
    Renders Hero, Skills Matrix, Interactive Timeline, Featured Projects,
    and Contact Form.
    """
    def get_context_data(self, **kwargs):
        profile = CandidateProfile.objects.first()
        if not profile:
            # Fallback placeholder if seed_cv hasn't run yet
            profile = CandidateProfile(
                name="Arvin Roman Agramon",
                title="Senior Software Engineer | Full-Stack & Cloud Integration Specialist",
                summary="Senior .NET & Full-Stack Software Engineer with over 15 years of industry experience.",
                email="aragramon@gmail.com",
                phone="+639278414288",
                location="Philippines",
                years_of_experience=15
            )

        categories = SkillCategory.objects.prefetch_related("skills").all()
        
        # Primary experience entries
        recent_experiences = Experience.objects.filter(is_earlier=False).order_by("order", "-id")
        earlier_experiences = Experience.objects.filter(is_earlier=True).order_by("order", "-id")
        
        # Extract unique category filter tags for the interactive timeline
        filter_tags = list(
            Experience.objects.exclude(category_tag="")
            .values_list("category_tag", flat=True)
            .distinct()
        )
        # Ensure popular filters exist in standard order if present
        ordered_tags = ["All"]
        for tag in ["AI & RAG", "Enterprise & SAP", "Cloud & Migration", "Full-Stack"]:
            if tag in filter_tags and tag not in ordered_tags:
                ordered_tags.append(tag)
        for tag in filter_tags:
            if tag not in ordered_tags:
                ordered_tags.append(tag)

        # Featured Projects
        featured_projects = Project.objects.filter(is_featured=True).order_by("order", "id")
        all_projects = Project.objects.all().order_by("order", "id")

        # Serialized projects for Alpine.js modal / drawer
        projects_payload = []
        for p in all_projects:
            projects_payload.append({
                "id": p.id,
                "title": p.title,
                "subtitle": p.subtitle,
                "company_name": p.company_name,
                "category": p.category,
                "problem_statement": p.problem_statement,
                "solution_summary": p.solution_summary,
                "architecture_highlights": p.architecture_highlights,
                "key_features": p.get_key_features_list(),
                "tech_stack": p.get_tech_stack_list(),
                "metrics": p.metrics,
                "external_url": p.external_url,
            })

        context = {
            "profile": profile,
            "skill_categories": categories,
            "recent_experiences": recent_experiences,
            "earlier_experiences": earlier_experiences,
            "filter_tags": ordered_tags,
            "featured_projects": featured_projects,
            "all_projects_json": json.dumps(projects_payload),
            "contact_form": kwargs.get("contact_form") or ContactForm(),
            "stats": {
                "years_experience": profile.years_of_experience,
                "systems_delivered": "10+",
                "specialization": ".NET, Cloud & AI",
                "availability": "Open to Enterprise / Consulting Roles"
            }
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, "portfolio/index.html", context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save(commit=False)
            contact_msg.ip_address = get_client_ip(request)
            contact_msg.save()

            # Optional email dispatch via django.core.mail
            try:
                profile = CandidateProfile.objects.first()
                recipient = profile.email if profile and profile.email else "aragramon@gmail.com"
                send_mail(
                    subject=f"[Portfolio Inquiry] {contact_msg.subject or 'New message from ' + contact_msg.name}",
                    message=f"Name: {contact_msg.name}\nEmail: {contact_msg.email}\nIP: {contact_msg.ip_address}\n\nMessage:\n{contact_msg.message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[recipient],
                    fail_silently=True,
                )
            except Exception:
                # Silently catch mail failure if SMTP is not configured in local environment
                pass

            messages.success(
                request, 
                "Thank you for reaching out! Your inquiry has been received. Arvin will review it and respond promptly."
            )
            return redirect("/#contact")
        else:
            messages.error(
                request, 
                "There was an issue submitting your message. Please check the fields below."
            )
            context = self.get_context_data(contact_form=form)
            return render(request, "portfolio/index.html", context)


class ResumeView(TemplateView):
    """
    Dedicated ATS-friendly and print-optimized Curriculum Vitae view.
    Formats exact experience, technologies, and academic records.
    """
    template_name = "portfolio/resume.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = CandidateProfile.objects.first()
        if not profile:
            profile = CandidateProfile(
                name="Arvin Roman Agramon",
                title="Senior Software Engineer | Full-Stack & Cloud Integration Specialist",
                summary="Senior .NET & Full-Stack Software Engineer with over 15 years of industry experience.",
                email="aragramon@gmail.com",
                phone="+639278414288",
                location="Philippines",
                years_of_experience=15
            )
        
        context["profile"] = profile
        context["skill_categories"] = SkillCategory.objects.prefetch_related("skills").all()
        context["recent_experiences"] = Experience.objects.filter(is_earlier=False).order_by("order", "-id")
        context["earlier_experiences"] = Experience.objects.filter(is_earlier=True).order_by("order", "-id")
        context["featured_projects"] = Project.objects.filter(is_featured=True).order_by("order", "id")
        return context


def project_detail_api(request, slug):
    """
    JSON API endpoint for asynchronous project drawer/modal hydration.
    """
    project = get_object_or_404(Project, slug=slug)
    data = {
        "id": project.id,
        "title": project.title,
        "subtitle": project.subtitle,
        "slug": project.slug,
        "company_name": project.company_name,
        "category": project.category,
        "problem_statement": project.problem_statement,
        "solution_summary": project.solution_summary,
        "architecture_highlights": project.architecture_highlights,
        "key_features": project.get_key_features_list(),
        "tech_stack": project.get_tech_stack_list(),
        "external_url": project.external_url,
        "metrics": project.metrics,
    }
    return JsonResponse(data)
