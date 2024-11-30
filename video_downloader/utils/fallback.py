import os
import hashlib
from urllib.parse import urlparse
from .facebook import download_facebook_video
from .instagram import download_instagram_reel
from .tiktok import download_tiktok_video
from .twitter import download_x_video
import yt_dlp

# Path to cookies file
COOKIES_FILE = "cookies.txt"  # Ensure this file is in the same directory if needed


def download_video(url):
    output_dir = r"C:\Users\Ymir\Desktop\Github\Instagram-Reels-Scraper\Functions\V2\V3\downloads"

    def identify_platform(url):
        domain = urlparse(url).netloc
        if 'facebook.com' in domain or 'fb.com' in domain:
            return 'facebook'
        elif 'instagram.com' in domain:
            return 'instagram'
        elif 'tiktok.com' in domain:
            return 'tiktok'
        elif 'twitter.com' in domain or 'x.com' in domain:
            return 'x'
        else:
            return None

    def fallback_download(url, output_dir):
        """Fallback using yt-dlp with unique hash filenames"""
        """Fallback using yt-dlp with unique hash filenames"""
        # Generate a unique hash from the URL
        url_hash = hashlib.md5(url.encode()).hexdigest()  # Full hash for uniqueness
        fallback_output_template = os.path.join(output_dir, f"{url_hash}.%(ext)s")
    
        ydl_opts = {
            'outtmpl': fallback_output_template,
            'format': 'bestvideo+bestaudio/best',  # Best quality video + audio
        }

        # Include cookies if the file exists
        if os.path.exists(COOKIES_FILE):
            ydl_opts['cookiefile'] = COOKIES_FILE

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                # Get the actual file extension from the downloaded video
                downloaded_extension = info.get('ext', 'unknown')  # 'unknown' as fallback if ext is not available
                downloaded_file = os.path.join(output_dir, f"{url_hash}.{downloaded_extension}")
                return f"Downloaded using fallback: {downloaded_file}"
        except Exception as e:
            return f"Fallback failed: {str(e)}"

    platform = identify_platform(url)

    try:
        if platform == 'facebook':
            result = download_facebook_video(url, output_dir)
            if not result:
                raise Exception("Facebook function failed")
            return result
        elif platform == 'instagram':
            result = download_instagram_reel(url, output_dir)
            if not result:
                raise Exception("Instagram function failed")
            return result
        elif platform == 'tiktok':
            result = download_tiktok_video(url, output_dir)
            if not result:
                raise Exception("TikTok function failed")
            return result
        elif platform == 'x':
            result = download_x_video(url, output_dir)
            if not result:
                raise Exception("X function failed")
            return result
        else:
            raise ValueError("Unsupported platform or unidentified URL")
    except Exception as e:
        print(f"Error with {platform} function: {str(e)}")
        print("Attempting fallback...")
        return fallback_download(url, output_dir)


# Test URLs for different platforms
urls_to_test = [
    "https://www.youtube.com/watch?v=Uqn1X6GNW3I",
    # Add more test URLs here
]

# Test each URL
for url in urls_to_test:
    result = download_video(url)
    print(f"URL: {url}")
    print(f"Result: {result}")
    print("-" * 50)
