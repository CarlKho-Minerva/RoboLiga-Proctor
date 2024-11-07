import os

# Configuration
screenshot_interval = 3  # in seconds, adjust as needed
log_file = "activity_log.txt"
screenshot_folder = "screenshots"

# Ensure screenshot folder exists
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)
