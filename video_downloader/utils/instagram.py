import os
from yt_dlp import YoutubeDL

def download_instagram_video(video_url, output_dir):
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'quiet': False,
        'cookiefile': 'igcookies_netscape.txt'  # Updated to use Netscape format
    }

    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(video_url, download=True)
        return result['requested_downloads'][0]['filepath']
