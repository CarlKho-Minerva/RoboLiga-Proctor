# RoboLiga-Proctor

BYOD Python Monitoring Script for the Virtual Robot League @ UAI '24 🇦🇷

<div>
    <a href="https://www.loom.com/share/4813cf2dafaf4566b694b01116e8eb84">
      <p>Robotics Project Update in Argentina - Watch Video</p>
    </a>
    <a href="https://www.loom.com/share/4813cf2dafaf4566b694b01116e8eb84">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/4813cf2dafaf4566b694b01116e8eb84-edc501872d420996-full-play.gif">
    </a>
</div>

## Overview

RoboLiga-Proctor is a monitoring tool designed for the Virtual Robot League competitions at Universidad Abierta Interamericana. It captures screenshots and logs window activity to ensure fair play during remote competitions.

## Features

- Automated screenshot capture every 3 seconds
- Active window monitoring
- Activity logging with timestamps
- Cross-platform support (Windows & macOS)

## For Users

### Requirements

- Python 3.11+
- PIL (Pillow)
- pygetwindow (Windows only)

### Quick Start

1. Clone the repository

```bash
git clone https://github.com/yourusername/RoboLiga-Proctor.git
```

2. Set up virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the monitor

```bash
python main.py
```

### Output

- Screenshots are saved in `screenshots`

- Activity logs are stored in `activity_log.txt`

## For Contributors

### Project Structure

```
├── main.py             # Entry point
├── config.py           # Configuration settings
├── utils/
│   ├── active_window.py    # Window tracking
│   ├── activity_logger.py  # Logging functions
│   └── screenshot.py       # Screenshot capture
```

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Submit a pull request

### Coding Standards

- Follow PEP 8 guidelines
- Add docstrings to functions
- Comment complex logic
- Include type hints where possible

## License

MIT License - See LICENSE file for details

## Contact

For questions or issues, please open a GitHub issue or contact the maintainers.
