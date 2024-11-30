import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def save_cookies_to_netscape_format(driver, output_file):
    cookies = driver.get_cookies()
    with open(output_file, 'w') as f:
        f.write("# Netscape HTTP Cookie File\n")
        for cookie in cookies:
            domain = cookie.get("domain")
            secure = "TRUE" if cookie.get("secure") else "FALSE"
            path = cookie.get("path", "/")
            expiration = str(int(cookie["expiry"])) if "expiry" in cookie else "0"
            name = cookie["name"]
            value = cookie["value"]
            f.write(f"{domain}\tTRUE\t{path}\t{secure}\t{expiration}\t{name}\t{value}\n")


def save_instagram_cookies():
    # Define Chrome options to use your existing user data
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=C:\\Users\\Ymir\\AppData\\Local\\Google\\Chrome\\User Data")
    chrome_options.add_argument("profile-directory=Profile 9")  # Replace with the correct profile if needed

    # Set up the Chrome driver
  # Replace with your chromedriver path
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open Instagram login page
        driver.get("https://www.youtube.com/login/")
        time.sleep(20)  # Wait for the page to load completely

        # Check if logged in by looking for the user profile or home page
        if "accounts/login" not in driver.current_url:
            print("You are logged in. Saving cookies...")
            save_cookies_to_netscape_format(driver, "yt_cookies.txt")
            print("Cookies saved to cookies.txt")
        else:
            print("You are not logged in. Please log in manually and try again.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    save_instagram_cookies()
