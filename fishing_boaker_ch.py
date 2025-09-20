import undetected_chromedriver as uc
import time
import os

PROFILE_DIR = os.path.abspath("user_data/fishingbooker_profile")

if __name__ == "__main__":
    opts = uc.ChromeOptions()
    opts.add_argument("--start-maximized")
    # persist entire Chrome session in this profile folder
    opts.add_argument(f"--user-data-dir={PROFILE_DIR}")
    opts.add_argument("--profile-directory=Default")  # optional, creates "Default" profile inside dir

    driver = uc.Chrome(options=opts, version_main=138)

    driver.get("https://fishingbooker.com/manage/profile")

    # if already logged in, it will restore session automatically
    # if not, login once and next runs will keep you logged in
    time.sleep(300)

    driver.quit()
