from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Listen for BAYC Transfer Events"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("Listening for events")
        )