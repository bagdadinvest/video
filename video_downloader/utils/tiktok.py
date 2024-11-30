from .PyHack import download_tiktok_video_with_playwright

def download_tiktok_video(video_url, output_dir):
    """
    Wrapper for downloading a TikTok video using Playwright.
    """
    return download_tiktok_video_with_playwright(video_url, output_dir)
