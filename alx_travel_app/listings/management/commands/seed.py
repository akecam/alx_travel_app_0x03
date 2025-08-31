from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random


class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        if not User.objects.exists():
            self.stdout.write(self.style.WARNING('No users found. Please create at least one user.'))
            return

        user = User.objects.first()
        for i in range(10):
            listing = Listing.objects.create(
                title=f'Sample Listing {i+1}',
                description='This is a sample property listing.',
                price_per_night=random.randint(50, 300),
                host=user,
            )
            self.stdout.write(self.style.SUCCESS(f'Created listing: {listing.title}'))
