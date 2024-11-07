import os
from datetime import datetime
from PIL import ImageGrab
from config import screenshot_folder

def sanitize_filename(filename):
    """Sanitize the filename by removing or replacing invalid characters."""
    return "".join(c if c.isalnum() or c in (' ', '.', '_') else '_' for c in filename)

def capture_screenshot(window_title):
    """Takes a screenshot and saves it to the screenshots folder with a timestamp."""
    try:
        timestamp = datetime.now().strftime("%H-%M-%S")
        sanitized_title = sanitize_filename(window_title)
        screenshot_filename = f"{timestamp}_{sanitized_title}.png"
        screenshot_path = os.path.join(screenshot_folder, screenshot_filename)
        screenshot = ImageGrab.grab()
        screenshot.save(screenshot_path)
        return screenshot_path
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return None
