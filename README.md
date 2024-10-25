# System Information Tool

A Python-based GUI application that provides comprehensive system information about your Windows computer. This tool consolidates various system details into a single, easy-to-read interface with export capabilities.

## Features

- **Hardware Information**
  - CPU specifications
  - RAM capacity (in GB)
  - GPU details
  - Motherboard information
  - Storage drives (size and free space in GB)
  - Network interfaces

- **System Details**
  - Operating system information
  - Version details
  - System configuration

- **User Interface**
  - Clean, scrollable GUI
  - Easy-to-read formatted output
  - Export functionality

## Requirements

- Python 3.x
- Windows operating system
- Required Python packages:
  - tkinter (usually comes with Python)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/seriousgamer42/get-computer-info
```

2. Navigate to the project directory:
```bash
cd system-information-tool
```

3. Run the application:
```bash
python system_info_gui.py
```

## Usage

1. Launch the application
2. Click "Get System Info" to retrieve current system information
3. Use the scrollbar to view all information
4. Click "Save to File" to export the information as JSON

## Output Format

The tool provides information in the following format:

```
Operating System:
[OS Name and Version]

Motherboard:
[Manufacturer, Product, Version, Serial Number]

CPU:
[Processor Name and Specifications]

RAM:
[Total RAM in GB]

Storage:
Drive | Total Size | Free Space
----------------------------------------
C: | 500.00 GB | 250.75 GB
...

GPU:
[Graphics Card Information]

Network Interfaces:
[List of Network Interfaces]
```

## Features in Development

- Real-time system monitoring
- Resource usage graphs
- Additional export formats
- System performance metrics

## Contributing

Feel free to fork this repository and submit pull requests. You can also open issues for bugs or feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Bradley Miller
- GitHub: [seriousgamer42](https://github.com/seriousgamer42)