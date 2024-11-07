import os
import subprocess

def get_active_window_title():
    active_window_title = "Unknown"
    if os.name == "nt":
        try:
            import pygetwindow as gw
            active_window = gw.getActiveWindow()
            if active_window:
                active_window_title = active_window.title
        except ImportError as e:
            print(f"Error importing pygetwindow: {e}")
    elif os.name == "posix":
        try:
            script = 'tell application "System Events" to get name of (processes where frontmost is true)'
            active_window_title = subprocess.check_output(['osascript', '-e', script]).decode().strip()
        except Exception as e:
            print(f"Error getting active window title: {e}")

    return active_window_title

def get_active_window():
    """Gets the name of the currently active window."""
    return get_active_window_title()
