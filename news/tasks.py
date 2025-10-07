import feedparser
from django.utils import timezone
from time import mktime
from .models import Source, Article
from celery import shared_task
from datatime import datetime


def _entry_published(entry):
    struct = entry.get('published_parsed') or entry.get('updated_parsed')
    if struct:
        return timezone.make_aware(datetime.fromtimestamp(mktime(struct)))
    return timezone.now()

def save_source(source:Source):
    d = feedparser.parse(source.rss_url)
    created = 0
    for entry in d.entries:
        link = entry.get('link')
        if not link:
            continue
        if Article.objects.filter(link=link).exists():
            continue
        title = entry.get('title', '')[:400]
        summary = entry.get('summary_detail', '')
        published = _entry_published(entry)
        Article.objects.create(
            source=source,
            title=title,
            link=link,
            published=published,
            summary=summary
        )
        created += 1
    return created

@shared_task
def fetch_all_sources(self):
    total = 0
    for source in Source.objects.filter(active=True):
        try:
            created = save_source(source)
            total += created
        except Exception as exs:
            self.retry(exc=exs, countdown=60, max_retries=3)
    return total

        