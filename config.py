import os

# Configuration
screenshot_interval = 3  # Interval in seconds between screenshots
log_file = "log_results/activity_log.txt"  # Path to the log file
screenshot_folder = "log_results/screenshots"  # Folder to save screenshots

# Ensure log_results folder exists
log_results_folder = "log_results"
if not os.path.exists(log_results_folder):
    os.makedirs(log_results_folder)

# Ensure screenshot folder exists
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)
