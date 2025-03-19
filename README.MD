# Raspberry Pi Throttle Monitor

## Overview
The **Raspberry Pi Throttle Monitor** is a simple GUI-based tool that continuously monitors the system's throttling status. It uses the `vcgencmd get_throttled` command to check if the Raspberry Pi is experiencing voltage, frequency, or temperature-related issues.

## Features
- **Real-time Monitoring**: Automatically updates every few seconds (configurable).
- **User-Friendly UI**: Displays eight status indicators in an organized layout.
- **Color-Coded Warnings**:
  - **Red**: Indicates current issues.
  - **Orange**: Indicates past occurrences.
- **Compact and Fixed-Sized Window**: Ensures a clean and simple display.

## Requirements
- Raspberry Pi (Any model running Raspberry Pi OS)
- Python 3
- Tkinter (usually pre-installed with Python)

## Installation
1. Clone the repository or copy the script.
   ```sh
   git clone https://github.com/your-repo/pi-throttle-monitor.git
   cd pi-throttle-monitor
   ```
2. Ensure you have Python installed.
   ```sh
   python3 --version
   ```
3. Run the script.
   ```sh
   python3 monitor.py
   ```

## How It Works
1. The script executes `vcgencmd get_throttled`, which returns a hexadecimal value.
2. This value is converted into a 32-bit binary string.
3. The relevant bits (0, 1, 2, 3, 16, 17, 18, 19) are checked, and the corresponding sections in the UI change color.
4. The script refreshes the status every 5 seconds (default, can be adjusted in the script).

## UI Breakdown
Each section represents a specific throttle-related event:

| Indicator | Meaning |
|-----------|---------|
| **Red** (Current Issue) | Active problems (voltage, frequency, temperature) |
| **Orange** (Past Issue) | Previously occurred but not currently active |

### Bit Mappings
| Bit | Description |
|----|--------------------------------------|
| 0  | Under-voltage detected |
| 1  | Arm frequency capped |
| 2  | Currently throttled |
| 3  | Soft temperature limit active |
| 16 | Under-voltage has occurred |
| 17 | Arm frequency capped has occurred |
| 18 | Throttling has occurred |
| 19 | Soft temperature limit has occurred |

## Configuration
- **Update Interval**: Change `refresh_interval = 5` (in seconds) inside the script to adjust how often the monitor updates.

## Notes
- This tool is designed for Raspberry Pi but can be modified to run on other Linux systems that support `vcgencmd`.
- It does not require root access.

## License
This project is licensed under the MIT License.

---

