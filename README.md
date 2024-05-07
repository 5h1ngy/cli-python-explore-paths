# cli-python-explore-path (CLI ExplorePaths)

The "File Navigator CLI" project aims to provide developers with a Python library to create a command-line interface (CLI) for navigating the file system. This tool will be useful for simplifying users' interaction with files and directories on the operating system.

### Key Features of the Project
The project offers the following key features:

File System Navigation: Users can navigate through directories and view files present in the system.
Detailed File Display: Detailed information about files, such as size, creation date, and permissions, can be obtained.
Basic File Operations: Basic file operations, including copy, move, and delete, are supported through the interface.

### Technologies Used and Reasons for Choices Made
The "File Navigator CLI" project utilizes the following technologies:

- **prompt-toolkit**:  It is a Python library for creating command-line user interfaces. It was chosen for its ease of use and numerous features for handling keyboard input.

- **questionary**: This library simplifies the creation of interactive prompts for the user in a CLI. It was selected to make the user interaction with the application more intuitive.

- **wcwidth**: Used to calculate the width of characters in the terminal. This dependency is necessary to ensure that the user interface is properly formatted and visible on a variety of devices and screens.

## Project Structure

The project is divided into various modules, each serving a specific function:

- **`explorer/menu.py`**: This module manages the interactive user interface, allowing users to navigate between directories and select Python files for execution.

- **`explorer/file.py`**: It contains useful functions for file management, including suffix verification, searching for Python files in a directory, and determining whether a folder contains files with a specific suffix.

- **`explorer/apart.py`**: Provides functions for string manipulation, particularly the separation and concatenation of paths.

- **`__init__.py`**: Initialization file for the Explorer package.

- **`main.py`**: The main entry point to launch the ExplorePaths application.

## Requirements

- Python 3.x
- The `questionary` module installed (can be installed with `pip install questionary`)

## Installation

1. Clone the repository: `git clone https://github.com/5h1ngy/cli-python-explore-paths.git`
2. Navigate to the project directory: `cd ExplorePaths`
3. Install dependencies: `pip install -r requirements.txt`

## Usage

To launch the ExplorePaths application, run the following command:

```bash
python main.py path list
# path: a path browser start to show
# list: suffix list
#     none: show all files
#     .py: show Python files
#     .py/.yml: show Python and YAML files
```

## Contributions

We welcome contributions! If you'd like to contribute to ExplorePaths, please follow the guidelines in the `CONTRIBUTING.md` file.

## License

This project is licensed under the terms of the MIT License - see the `LICENSE` file for full details.