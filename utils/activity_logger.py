import os
from datetime import datetime
from utils.screenshot import capture_screenshot
from utils.active_window import get_current_window_titles
from config import log_file
import subprocess

last_logged_date = None
screenshot_directory_logged = False

def log_user_activity(window_titles, active_window_title):
    """Logs the current active windows and screenshot path with a timestamp."""
    global last_logged_date, screenshot_directory_logged
    try:
        current_date = datetime.now().strftime("%B %d, %Y")
        timestamp = datetime.now().strftime("%H:%M:%S")
        screenshot_path = capture_screenshot(active_window_title)
        screenshot_filename = os.path.basename(screenshot_path)
        screenshot_link = f'"file://{os.path.abspath(screenshot_path)}"'
        log_entry = f"{timestamp} | Active: {active_window_title} | All: {', '.join(window_titles)} | {screenshot_filename}\n"
        with open(log_file, "a") as f:
            if last_logged_date != current_date:
                f.write(f"Date: {current_date}\n\n")
                last_logged_date = current_date
                screenshot_directory_logged = False
            if not screenshot_directory_logged:
                f.write(f"Screenshot Directory: {os.path.dirname(screenshot_path)}\n\n")
                screenshot_directory_logged = True
            f.write(log_entry)
        if last_logged_date != current_date:
            print(f"Date: {current_date}")  # Print date to console
        if not screenshot_directory_logged:
            print(
                f"Screenshot Directory: {os.path.dirname(screenshot_path)}"
            )  # Print screenshot directory to console
        print(log_entry.strip())  # Optional: Print to console
    except Exception as e:
        print(f"Error logging user activity: {e}")

def get_current_window_title():
    """Gets the title of the currently active window."""
    window_title = "Unknown"
    if os.name == "nt":
        try:
            import pygetwindow as gw

            active_window = gw.getActiveWindow()
            if active_window:
                window_title = active_window.title
        except ImportError as e:
            print(f"Error importing pygetwindow: {e}")
        except Exception as e:
            print(f"Error getting active window title on Windows: {e}")
    elif os.name == "posix":
        try:
            script = 'tell application "System Events" to get name of (processes where frontmost is true)'
            window_title = (
                subprocess.check_output(["osascript", "-e", script]).decode().strip()
            )
        except subprocess.CalledProcessError as e:
            print(f"Error executing AppleScript: {e}")
        except Exception as e:
            print(f"Error getting active window title on macOS: {e}")

    return window_title
