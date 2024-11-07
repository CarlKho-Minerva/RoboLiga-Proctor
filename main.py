import time
from activity_logger import log_activity, get_active_window_title
from config import screenshot_interval


def main():
    """Main monitoring loop."""
    try:
        print("Starting activity monitoring...")
        while True:
            active_window = get_active_window_title()
            log_activity(active_window)
            time.sleep(screenshot_interval)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
