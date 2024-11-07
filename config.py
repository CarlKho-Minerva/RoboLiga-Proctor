import os

# Configuration
screenshot_interval = 3  # Interval in seconds between screenshots
log_file = "activity_log.txt"  # Path to the log file
screenshot_folder = "screenshots"  # Folder to save screenshots

# Ensure screenshot folder exists
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)
