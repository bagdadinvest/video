import subprocess

def execute_scripts():
    try:
        print("\nRunning detection script...")
        subprocess.run(["python3", "scripts/detect_platform.py"], check=True)

        print("\nRunning download script...")
        subprocess.run(["python3", "scripts/download_videos.py"], check=True)

        print("\nRunning logging script...")
        subprocess.run(["python3", "scripts/log_metadata.py"], check=True)

        print("\nAll scripts executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    execute_scripts()
