from playwright.sync_api import sync_playwright
import os

def download_tiktok_video_with_playwright(video_url, output_dir):
    """
    Download a TikTok video using Playwright.

    :param video_url: The URL of the TikTok video.
    :param output_dir: The directory where the video will be saved.
    :return: The path to the downloaded video.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the TikTok video page
        page.goto(video_url)
        print("Navigated to TikTok page...")

        # Wait for the video element to load
        video_element = page.wait_for_selector("video", timeout=15000)
        if not video_element:
            raise ValueError("Failed to locate video element on the page.")

        # Extract the video URL
        video_src = video_element.get_attribute("src")
        if not video_src:
            raise ValueError("Failed to extract video URL from the page.")
        print(f"Extracted video URL: {video_src}")

        # Download the video
        video_id = video_url.split("/")[-1]
        video_path = os.path.join(output_dir, f"tiktok_video_{video_id}.mp4")

        # Save video to the output directory
        with open(video_path, "wb") as f:
            video_content = page.evaluate(f"fetch('{video_src}').then(res => res.arrayBuffer())")
            f.write(bytes(video_content))

        print(f"Video downloaded successfully: {video_path}")
        browser.close()

        return video_path
