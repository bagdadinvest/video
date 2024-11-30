from django.urls import path
from . import views

app_name = 'video_downloader'

urlpatterns = [
    path('', views.index, name='index'),
    path('download/', views.download_video, name='download_video'),
    path('history/', views.history, name='history'),
]
