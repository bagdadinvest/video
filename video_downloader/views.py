from django.http import JsonResponse
from .utils.tiktok import download_tiktok_video

def download_video_view(request):
    """
    A view to trigger the video download (example implementation).
    """
    video_url = request.GET.get("url")
    output_dir = "media/videos/"
    if video_url:
        video_path = download_tiktok_video(video_url, output_dir)
        return JsonResponse({"status": "success", "video_path": video_path})
    return JsonResponse({"status": "error", "message": "No URL provided"})

from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime

# Mock history data
history_data = []

def index(request):
    if request.method == "POST":
        url = request.POST.get("url")
        platform = "unknown"  # Replace with actual platform detection logic
        title = "Example Video"  # Replace with actual video title
        status = "success"  # Replace with actual status
        downloaded_at = datetime.now()

        # Add record to history
        history_data.append({
            "url": url,
            "platform": platform,
            "title": title,
            "status": status,
            "downloaded_at": downloaded_at.strftime("%Y-%m-%d %H:%M:%S"),
        })

        message = "Video downloaded successfully!"
        return render(request, "video_downloader/index.html", {"message": message})

    return render(request, "video_downloader/index.html")


def history(request):
    return render(request, "video_downloader/history.html", {"history": history_data})


def download_video(request):
    return JsonResponse({"message": "Not implemented yet"})
