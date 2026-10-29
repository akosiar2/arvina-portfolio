import os
import re
import shutil
from pathlib import Path
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.test import Client


class Command(BaseCommand):
    help = "Exports the Django portfolio as a static site into the docs/ folder for GitHub Pages."

    def add_arguments(self, parser):
        parser.add_argument(
            "--output-dir",
            default="docs",
            help="Target output directory for the static site (default: docs/)",
        )

    def handle(self, *args, **options):
        output_dir = Path(settings.BASE_DIR) / options["output_dir"]
        self.stdout.write(self.style.NOTICE(f"Exporting portfolio for GitHub Pages into: {output_dir}..."))

        # 1. Ensure database is populated
        call_command("seed_cv")

        # 2. Collect static files
        call_command("collectstatic", interactive=False, verbosity=0)

        # 3. Clean and prepare output directory
        if output_dir.exists():
            shutil.rmtree(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # 4. Copy static files into docs/static/
        staticfiles_src = Path(settings.STATIC_ROOT)
        staticfiles_dest = output_dir / "static"
        if staticfiles_src.exists():
            shutil.copytree(staticfiles_src, staticfiles_dest)
            self.stdout.write(self.style.SUCCESS("Copied static assets to docs/static/"))

        # Also copy from static/ if any uncollected
        local_static = Path(settings.BASE_DIR) / "static"
        if local_static.exists():
            for item in local_static.iterdir():
                dest_item = staticfiles_dest / item.name
                if item.is_dir() and not dest_item.exists():
                    shutil.copytree(item, dest_item)
                elif item.is_file() and not dest_item.exists():
                    shutil.copy2(item, dest_item)

        client = Client()

        # 5. Render and export Home Page (docs/index.html)
        home_res = client.get("/")
        if home_res.status_code != 200:
            self.stderr.write(self.style.ERROR(f"Failed to render home page: {home_res.status_code}"))
            return

        home_html = home_res.content.decode("utf-8")
        # Replace absolute paths with relative paths for GitHub Pages subfolder compatibility
        home_html = home_html.replace('href="/static/', 'href="static/')
        home_html = home_html.replace('src="/static/', 'src="static/')
        home_html = home_html.replace('href="/resume/"', 'href="resume/"')
        home_html = home_html.replace('href="/#', 'href="#')
        home_html = home_html.replace('href="/"', 'href="./"')
        # Point contact form to mailto / static handler on GitHub Pages
        home_html = home_html.replace(
            'action="/#contact"',
            'action="mailto:aragramon@gmail.com" method="get" enctype="text/plain"'
        )

        with open(output_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(home_html)
        self.stdout.write(self.style.SUCCESS("Generated docs/index.html"))

        # 6. Render and export Resume Page (docs/resume/index.html)
        resume_dir = output_dir / "resume"
        resume_dir.mkdir(parents=True, exist_ok=True)

        resume_res = client.get("/resume/")
        if resume_res.status_code != 200:
            self.stderr.write(self.style.ERROR(f"Failed to render resume page: {resume_res.status_code}"))
            return

        resume_html = resume_res.content.decode("utf-8")
        # Replace paths relative to resume/
        resume_html = resume_html.replace('href="/static/', 'href="../static/')
        resume_html = resume_html.replace('src="/static/', 'src="../static/')
        resume_html = resume_html.replace('href="/"', 'href="../"')
        resume_html = resume_html.replace('href="/#', 'href="../#')

        with open(resume_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(resume_html)
        self.stdout.write(self.style.SUCCESS("Generated docs/resume/index.html"))

        # 7. Add .nojekyll so GitHub Pages does not filter out any underscore folders
        with open(output_dir / ".nojekyll", "w", encoding="utf-8") as f:
            f.write("")

        self.stdout.write(self.style.SUCCESS(
            "\nGitHub Pages static export complete! You can now serve directly from the docs/ folder."
        ))
