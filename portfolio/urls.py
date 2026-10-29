from django.urls import path
from .views import HomeView, ResumeView, project_detail_api

app_name = "portfolio"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("resume/", ResumeView.as_view(), name="resume"),
    path("api/projects/<slug:slug>/", project_detail_api, name="project_detail_api"),
]
