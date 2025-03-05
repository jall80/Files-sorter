# Files-Sorter

## Overview
Files-Sorter is a Python script that organizes files in a specified directory by sorting them into subdirectories based on their file extensions. It is useful for managing downloads, project files, or cleaning up large, mixed file collections.

## Features
- Categorizes files into predefined types (e.g., video, audio, documents, images, etc.).
- Uses a dictionary (`files_types`) to map extensions to categories.
- Ensures the dictionary is valid using a decorator (`@check_dict`).
- Automatically creates necessary directories for sorting.
- Moves unmatched files to an "others" folder.
- Detects and raises an error if any files remain unsorted.

## Installation
To install the script, clone the repository and run the following command:

```bash
pip install .
```

## Usage
Run the script via the command line with the following syntax:

```bash
filesorter --directory <folder_path>
```

or

```bash
filesorter --dir <folder_path>
```

or

```bash
filesorter --dir <folder_name>
```

### Execution example
```bash
filesorter --directory /path/to/your/files
```

This will create a new directory named `<folder_path>_sorted`, where files will be categorized and placed in appropriate subdirectories.

### Full example
#### Before Running the Script
```
Downloads/
│-- video1.mp4
│-- audio1.mp3
│-- document1.pdf
│-- image1.png
│-- script.py
```

#### After Running the Script (`filesorter --dir Downloads`)
```
Downloads_sorted/
│-- Videos/
│   └── video1.mp4
│-- Audio/
│   └── audio1.mp3
│-- Documents/
│   └── document1.pdf
│-- Images/
│   └── image1.png
│-- Others/
│   └── script.py
```

## Error Handling
- If the specified directory does not exist, an error message is displayed.
- If any files remain unsorted, an error is raised.

## Contributing
Feel free to fork the repository and submit pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License.

## Contact
Author: Jose Lopez Li  
Email: jall08jall@gmail.com  
GitHub: [Files-Sorter Repository](https://github.com/jall80/Files-sorter)

