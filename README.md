# ExplorePaths

ExplorePaths is a tool for navigating and executing Python files within a specified path. The application provides an interactive user interface for selecting and running Python files and navigating between directories.

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
python main.py ./ path/to/start/directory
# explorer path list
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