from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

# Home Page View
def home(request):
    return render(request, 'main/home.html')

# About Page View
def about(request):
    return render(request, 'main/about.html')

# Projects Page View
def project(request):
    return render(request, 'main/project.html')

# Success Page View
def success_view(request):
    return render(request, 'main/success.html')

# Hobbies Page View
def hobbies(request):
    return render(request, 'main/hobbies.html')

# Contact Form View
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the form data to the database

            # Send an email after saving the form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f"New message from {name}"
            body = f"Email: {email}\n\nMessage:\n{message}"

            send_mail(
                subject,
                body,
                email,
                ['johnreymartviernes@gmail.com'],  # Replace with your own email
            )

            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'main/form.html', {'form': form})
