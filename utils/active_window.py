import os
import subprocess


def get_current_window_titles():
    """Gets the titles of all currently active windows and the active window title."""
    window_titles = []
    active_window_title = "Unknown"
    if os.name == "nt":
        try:
            import pygetwindow as gw

            windows = gw.getWindowsWithTitle('')
            window_titles = [window.title for window in windows if window.title]
            active_window = gw.getActiveWindow()
            if active_window:
                active_window_title = active_window.title
        except ImportError as e:
            print(f"Error importing pygetwindow: {e}")
        except Exception as e:
            print(f"Error getting window titles on Windows: {e}")
    elif os.name == "posix":
        try:
            script = 'tell application "System Events" to get name of (processes where background only is false)'
            window_titles = (
                subprocess.check_output(["osascript", "-e", script]).decode().strip().split(", ")
            )
            script_active = 'tell application "System Events" to get name of (processes where frontmost is true)'
            active_window_title = (
                subprocess.check_output(["osascript", "-e", script_active]).decode().strip()
            )
        except subprocess.CalledProcessError as e:
            print(f"Error executing AppleScript: {e}")
        except Exception as e:
            print(f"Error getting window titles on macOS: {e}")

    return window_titles, active_window_title


def get_active_window():
    """Gets the name of the currently active window."""
    return get_current_window_titles()
