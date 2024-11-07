import time
from activity_logger import log_user_activity, get_current_window_title
from config import screenshot_interval


def main():
    """Main monitoring loop."""
    try:
        print("Starting activity monitoring...")
        while True:
            window_title = get_current_window_title()
            log_user_activity(window_title)
            time.sleep(screenshot_interval)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
