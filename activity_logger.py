import os
from datetime import datetime
from screenshot import take_screenshot
from active_window import get_active_window_title
from config import log_file
import subprocess


def log_activity(active_window):
    """Logs the active window and screenshot path with a timestamp."""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        screenshot_path = take_screenshot()
        log_entry = (
            f"{timestamp} | Active Window: {active_window} | "
            f"Screenshot: {screenshot_path}\n"
        )
        with open(log_file, "a") as f:
            f.write(log_entry)
        print(log_entry.strip())  # Optional: Print to console
    except Exception as e:
        print(f"Error logging activity: {e}")


def get_active_window_title():
    active_window_title = "Unknown"
    if os.name == "nt":
        import pygetwindow as gw
        active_window = gw.getActiveWindow()
        if active_window:
            active_window_title = active_window.title
    elif os.name == "posix":
        try:
            script = 'tell application "System Events" to get name of (processes where frontmost is true)'
            active_window_title = (
                subprocess.check_output(["osascript", "-e", script]).decode().strip()
            )
        except Exception as e:
            print(f"Error getting active window title: {e}")

    return active_window_title
