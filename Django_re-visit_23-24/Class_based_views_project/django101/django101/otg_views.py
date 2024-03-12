from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.generic import View


class EmailSendView(View):
    def post(self, request):
        # Extract form data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        # subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Construct the email message
        subject = "New contact form submission"
        message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        # Send email using Django's send_mail() function
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,  # Sender's email address
            recipient_list=['recipient@example.com'],  # List of recipient email addresses
        )

        # Optionally, return a JSON response indicating success
        return JsonResponse({'message': 'Email sent successfully'})