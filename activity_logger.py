from datetime import datetime
from screenshot import take_screenshot
from active_window import get_active_window
from config import log_file

def log_activity():
    """Logs the active window and screenshot path with a timestamp."""
    with open(log_file, "a") as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        active_window = get_active_window()
        screenshot_path = take_screenshot()
        log_entry = f"{timestamp} | Active Window: {active_window} | Screenshot: {screenshot_path}\n"
        f.write(log_entry)
        print(log_entry.strip())  # Optional: Print to console
