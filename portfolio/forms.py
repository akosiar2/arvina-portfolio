from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
    Enterprise contact form with built-in bot honeypot protection
    and Tailwind-ready widget rendering.
    """
    # Honeypot field: invisible to real users via CSS; if filled, bot is detected
    verification_code = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "tabindex": "-1",
            "autocomplete": "off",
            "class": "hidden",
            "aria-hidden": "true",
            "style": "display:none !important;"
        })
    )

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 bg-slate-50 dark:bg-slate-800/80 border border-slate-300 dark:border-slate-700 rounded-lg text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition duration-200 text-sm",
                "placeholder": "Your Full Name or Organization",
                "required": True,
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full px-4 py-3 bg-slate-50 dark:bg-slate-800/80 border border-slate-300 dark:border-slate-700 rounded-lg text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition duration-200 text-sm",
                "placeholder": "you@company.com",
                "required": True,
            }),
            "subject": forms.TextInput(attrs={
                "class": "w-full px-4 py-3 bg-slate-50 dark:bg-slate-800/80 border border-slate-300 dark:border-slate-700 rounded-lg text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition duration-200 text-sm",
                "placeholder": "Project Consultation, Full-Stack Opportunity, Technical Advisory...",
                "required": True,
            }),
            "message": forms.Textarea(attrs={
                "class": "w-full px-4 py-3 bg-slate-50 dark:bg-slate-800/80 border border-slate-300 dark:border-slate-700 rounded-lg text-slate-900 dark:text-slate-100 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-transparent transition duration-200 text-sm",
                "placeholder": "Describe your architectural challenge, technical requirements, or schedule an exploratory interview...",
                "rows": 5,
                "required": True,
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        honeypot = cleaned_data.get("verification_code")
        if honeypot:
            # Bot trap triggered!
            raise forms.ValidationError("Automated submission detected.")
        return cleaned_data
