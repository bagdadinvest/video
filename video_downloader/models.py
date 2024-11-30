from django.db import models

# Create your models here.
from django.db import models

class DownloadRecord(models.Model):
    platform = models.CharField(max_length=50)
    video_url = models.URLField()
    file_path = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, default='Pending')
    error_message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
