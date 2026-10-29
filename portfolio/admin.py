from django.contrib import admin
from django.utils.html import format_html
from .models import (
    CandidateProfile,
    SkillCategory,
    Skill,
    Experience,
    Project,
    ContactMessage
)


@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "email", "phone", "location", "years_of_experience")
    fieldsets = (
        ("Personal Information", {
            "fields": ("name", "title", "summary", "avatar_url", "years_of_experience")
        }),
        ("Contact & Social", {
            "fields": ("email", "phone", "location", "github", "linkedin", "resume_file")
        }),
        ("Education & Tags", {
            "fields": ("education_degree", "education_school", "education_year", "key_tags")
        }),
    )

    def has_add_permission(self, request):
        # Enforce singleton pattern in admin if a profile already exists
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ("name", "proficiency_percentage", "is_primary", "is_featured", "order")


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "icon_name", "order", "skill_count")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [SkillInline]

    def skill_count(self, obj):
        return obj.skills.count()
    skill_count.short_description = "Skills Count"


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency_percentage", "is_primary", "is_featured", "order")
    list_filter = ("category", "is_primary", "is_featured")
    search_fields = ("name", "category__name")
    list_editable = ("proficiency_percentage", "is_primary", "is_featured", "order")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "start_date", "end_date", "category_tag", "is_current", "is_earlier", "order")
    list_filter = ("is_current", "is_earlier", "category_tag")
    search_fields = ("role", "company", "description", "tech_stack")
    list_editable = ("order", "is_current", "is_earlier", "category_tag")
    fieldsets = (
        ("Role Details", {
            "fields": ("role", "company", "company_url", "location", "category_tag")
        }),
        ("Timeline", {
            "fields": ("start_date", "end_date", "is_current", "is_earlier", "order")
        }),
        ("Content & Architecture", {
            "fields": ("context", "description", "bullet_points", "tech_stack")
        }),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "company_name", "category", "is_featured", "order")
    list_filter = ("is_featured", "category")
    search_fields = ("title", "company_name", "problem_statement", "solution_summary", "tech_stack")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("is_featured", "order")
    fieldsets = (
        ("Project Overview", {
            "fields": ("title", "subtitle", "slug", "company_name", "category", "external_url", "metrics", "is_featured", "order")
        }),
        ("Technical Deep Dive", {
            "fields": ("problem_statement", "solution_summary", "architecture_highlights", "key_features", "tech_stack")
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "is_resolved", "ip_address")
    list_filter = ("is_resolved", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("name", "email", "subject", "message", "created_at", "ip_address")
    actions = ["mark_as_resolved", "mark_as_unresolved"]

    def mark_as_resolved(self, request, queryset):
        queryset.update(is_resolved=True)
    mark_as_resolved.short_description = "Mark selected inquiries as resolved"

    def mark_as_unresolved(self, request, queryset):
        queryset.update(is_resolved=False)
    mark_as_unresolved.short_description = "Mark selected inquiries as pending"
