import time
import logging
import os
import json
import hashlib
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def download_x_video(video_url, output_dir):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("user-data-dir=C:/Users/Ymir/AppData/Local/Google/Chrome/User Data")
    options.add_argument("profile-directory=Profile 5")
    options.add_argument('--headless')
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        video_urls, audio_urls = extract_stream_urls(driver, video_url)
        
        if video_urls and audio_urls:
            video_url = video_urls[0]
            audio_url = audio_urls[0]
            
            unique_name = hashlib.md5(video_url.encode()).hexdigest() + ".mp4"
            output_file = os.path.join(output_dir, unique_name)
            
            download_and_merge(video_url, audio_url, output_file)
            
            return output_file
        else:
            return None
    finally:
        driver.quit()

def extract_stream_urls(driver, post_url):
    driver.get(post_url)
    time.sleep(5)  # Wait for the page to load
    logs = driver.get_log('performance')
    
    video_urls, audio_urls = [], []
    for log in logs:
        message = json.loads(log['message'])['message']
        if message['method'] == 'Network.requestWillBeSent':
            request_url = message['params']['request']['url']
            if '.m3u8' in request_url:
                if 'mp4a' in request_url:
                    audio_urls.append(request_url)
                elif 'avc1' in request_url:
                    video_urls.append(request_url)
    return video_urls[:1], audio_urls[:1]

def download_and_merge(video_url, audio_url, output_file):
    try:
        command = [
            'ffmpeg', 
            '-i', video_url, 
            '-i', audio_url, 
            '-c:v', 'copy',
            '-c:a', 'aac',
            '-strict', 'experimental',
            output_file
        ]
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        return None

