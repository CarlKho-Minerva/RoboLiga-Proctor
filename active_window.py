import psutil

def get_active_window():
    """Gets the name of the currently active window."""
    try:
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] and proc.info['pid'] == psutil.Process().ppid():
                return proc.info['name']
    except Exception as e:
        return "Unknown"
