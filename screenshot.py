import os
from datetime import datetime
from PIL import ImageGrab
from config import screenshot_folder

def take_screenshot():
    """Takes a screenshot and saves it to the screenshots folder with a timestamp."""
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_path = os.path.join(screenshot_folder, f"screenshot_{timestamp}.png")
    screenshot = ImageGrab.grab()
    screenshot.save(screenshot_path)
    return screenshot_path
