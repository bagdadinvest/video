import csv
import os
from datetime import datetime

metadata_file = 'media/download_metadata.csv'

def log_metadata(metadata):
    is_new_file = not os.path.exists(metadata_file)
    if not os.path.exists(os.path.dirname(metadata_file)):
        os.makedirs(os.path.dirname(metadata_file))

    with open(metadata_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=metadata.keys())
        if is_new_file:
            writer.writeheader()
        writer.writerow(metadata)

# Example usage
if __name__ == "__main__":
    metadata = {
        'url': "https://www.facebook.com/watch?v=1605604903328504",
        'platform': 'facebook',
        'status': 'success',
        'title': 'Example Video',
        'file_path': 'media/videos/facebook_example.mp4',
        'downloaded_at': datetime.now().isoformat(),
    }
    log_metadata(metadata)
    print(f"Logged metadata: {metadata}")

