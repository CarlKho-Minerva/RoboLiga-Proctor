import os
from datetime import datetime
from screenshot import capture_screenshot
from active_window import get_current_window_title
from config import log_file
import subprocess


def log_user_activity(window_title):
    """Logs the current active window and screenshot path with a timestamp."""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        screenshot_path = capture_screenshot(window_title)
        log_entry = (
            f"At {timestamp}, you were using: {window_title}. "
            f"A screenshot was saved at: {screenshot_path}\n"
        )
        with open(log_file, "a") as f:
            f.write(log_entry)
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
