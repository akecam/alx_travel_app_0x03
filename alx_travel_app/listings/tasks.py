from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(booking_id, user_email, listing_title):
    """
    Sends a booking confirmation email to the user.
    """
    subject = f"Booking Confirmation for {listing_title}"
    message = f"Dear user,\n\nYour booking for '{listing_title}' (Booking ID: {booking_id}) has been confirmed.\n\nThank you!"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
    print(f"Booking confirmation email sent to {user_email} for listing {listing_title}")
