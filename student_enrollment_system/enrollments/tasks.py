from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings

from .models import Student

@shared_task
def send_welcome_email(student_id):
    """
    Send a welcome email to the student
    Parameters: student_id: The id of the student to send the email to
    """
    student = Student.objects.get(id=student_id)
    email_subject = 'Thank you for joining'
    email_body = f"Hey {student.first_name}! Thanks for joining the platform , we look forward to helping you."

    email = EmailMessage(
        email_subject, email_body,
        settings.EMAIL_HOST_USER, [student.email],
    )
    email.send(fail_silently=False)