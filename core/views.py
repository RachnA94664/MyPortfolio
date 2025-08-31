from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Project, Skill, Certification, Profile


def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    certifications = Certification.objects.all()
    profile = Profile.objects.first()

    success = None

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject=f"Portfolio Contact from {name}",
                message=f"Message from: {name} <{email}>\n\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            form = ContactForm()  # Clear form after sending
            success = True
        else:
            success = False
    else:
        form = ContactForm()

    return render(request, "home.html", {
        "projects": projects,
        "skills": skills,
        "certifications": certifications,
        "profile": profile,
        "form": form,
        "success": success,
    })
