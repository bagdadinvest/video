from celery import shared_task
from .utils.fallback import fallback_download

@shared_task
def sample_task():
    return "Celery is working!"

@shared_task
def download_task(url):
    return fallback_download(url, 'media/videos/')
