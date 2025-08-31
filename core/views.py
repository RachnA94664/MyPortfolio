from django.shortcuts import render
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

            # Temporary workaround for free PythonAnywhere account
            # Print the message instead of sending email
            print(f"Contact form submitted by {name} <{email}>: {message}")
            success = True

            form = ContactForm()  # Clear form after "sending"
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
