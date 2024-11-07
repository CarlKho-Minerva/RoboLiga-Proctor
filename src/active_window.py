import os
import subprocess


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


def get_active_window():
    """Gets the name of the currently active window."""
    return get_current_window_title()
