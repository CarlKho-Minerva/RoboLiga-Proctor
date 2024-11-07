import time
from activity_logger import log_activity
from config import screenshot_interval

# Main monitoring loop
try:
    print("Starting activity monitoring...")
    while True:
        log_activity()
        time.sleep(screenshot_interval)
except KeyboardInterrupt:
    print("Monitoring stopped.")
except Exception as e:
    print(f"Error occurred: {e}")
