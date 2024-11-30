import re

def detect_platform(url):
    platform_patterns = {
        'facebook': r'(facebook\.com)',
        'instagram': r'(instagram\.com)',
        'tiktok': r'(tiktok\.com)',
        'twitter': r'(twitter\.com)'
    }

    for platform, pattern in platform_patterns.items():
        if re.search(pattern, url):
            return platform
    return "unknown"

# Example usage
if __name__ == "__main__":
    url = input("Enter the video URL: ")
    platform = detect_platform(url)
    print(f"Detected platform: {platform}")
