from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

from django.shortcuts import render

def about(request):
    return render(request, 'main/about.html')

from .forms import ContactForm

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail

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
                subject,         # Subject of the email
                body,            # Body content of the email
                email,           # Sender's email address (user's email)
                ['yourgmail@gmail.com'],  # Replace with your email to receive messages
            )

            return redirect('success')  # Redirect to the success page after form submission
    else:
        form = ContactForm()  # If it's a GET request, show an empty form

    return render(request, 'main/form.html', {'form': form})

from django.shortcuts import render

def project(request):
    return render(request, 'main/project.html')

def success_view(request):
    return render(request, 'main/success.html')

def hobbies(request):
    return render(request, 'main/hobbies.html')