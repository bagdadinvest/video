import subprocess
import os

def download_video(url, output_dir="media/videos"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_command = [
        "yt-dlp",
        "-o", f"{output_dir}/%(title)s.%(ext)s",
        url
    ]

    try:
        subprocess.run(ydl_command, check=True)
        return "Download successful!"
    except subprocess.CalledProcessError as e:
        return f"Error during download: {e}"

# Example usage
if __name__ == "__main__":
    url = input("Enter the video URL: ")
    result = download_video(url)
    print(result)

