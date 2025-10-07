from django.core.management.base import BaseCommand
from news.tasks import fetch_all_sources

class Command(BaseCommand):
    help = 'Fetch RSS feeds'
    
    def handle(self, *args, **options):
        fetch_all_sources.delay()
        result = fetch_all_sources.apply()
        self.stdout.write(f"Created {result.result} articles.")