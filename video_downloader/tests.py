from django.test import TestCase
from video_downloader.utils.instagram import download_instagram_video
from video_downloader.utils.facebook import download_facebook_video
import os

class InstagramDownloaderTestCase(TestCase):
    def setUp(self):
        self.test_url = "https://www.instagram.com/p/DCmALG5sHEJ/"
        self.output_dir = "media/videos/"
        os.makedirs(self.output_dir, exist_ok=True)

    def test_download_instagram_video(self):
        try:
            result = download_instagram_video(self.test_url, self.output_dir)
            self.assertTrue(os.path.exists(result), "yt_dlp failed, falling back...")
        except Exception as e:
            self.assertTrue(os.path.exists(result), f"Test failed with exception: {e}")

    def tearDown(self):
        for file in os.listdir(self.output_dir):
            os.remove(os.path.join(self.output_dir, file))

class FacebookDownloaderTestCase(TestCase):
    def setUp(self):
        self.test_url = "https://www.facebook.com/watch?v=1605604903328504"
        self.output_dir = "media/videos/"
        os.makedirs(self.output_dir, exist_ok=True)

    def test_download_facebook_video(self):
        try:
            result = download_facebook_video(self.test_url, self.output_dir)
            self.assertTrue(os.path.exists(result), "yt_dlp failed, falling back...")
        except Exception as e:
            self.assertTrue(os.path.exists(result), f"Test failed with exception: {e}")

    def tearDown(self):
        for file in os.listdir(self.output_dir):
            os.remove(os.path.join(self.output_dir, file))
