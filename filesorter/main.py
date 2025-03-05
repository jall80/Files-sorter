#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import argparse

"""
File Sorter Script
------------------

Purpose:
This script is designed to organize files in a specified directory by moving them
into categorized subdirectories based on their file extensions. Files that do not
match any predefined categories are moved into an 'others' folder.

Supported File Types:
- Video: .mp4, .mkv, .avi, .mov, .webm, .flv
- Audio: .mp3, .wav, .flac, .aac, .ogg, .m4a
- Documents: .docx, .txt, .rtf, .odt
- PDFs: .pdf
- Spreadsheets: .xlsx, .xls, .csv, .ods
- Presentations: .pptx, .ppt, .odp
- Images: .jpg, .jpeg, .png, .gif, .bmp, .svg, .tiff, .webp
- Archives: .zip, .rar, .tar, .7z, .gz, .bz2
- Executables: .exe, .msi, .apk, .bin, .run
- Scripts: .sh, .bat, .ps1, .cmd
- Python: .py, .pyc, .pyo
- C/C++: .cpp, .hpp, .c, .h
- Java: .java, .class, .jar
- JavaScript: .js, .mjs
- PHP: .php, .phtml
- HTML: .html, .htm
- CSS: .css, .scss, .sass
- Ruby: .rb
- TypeScript: .ts
- JSON: .json
- XML: .xml
- YAML: .yaml, .yml
- Markdown: .md
- Database: .sql, .sqlite, .db, .mdb
- System: .dll, .sys, .ini, .log, .cfg

Usage:
python filesorter.py --directory /path/to/your/files
python filesorter.py --directory files

Options:
--directory or --dir : Specify the directory you wish to sort.

Author:
Jose Lopez Li

License:
"""

files_types = {
    "video": [".mp4", ".mkv", ".avi", ".mov", ".webm", ".flv"],
    "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "documents": [".docx", ".txt", ".rtf", ".odt"],
    "pdf": [".pdf"],
    "excel": [".xlsx", ".xls", ".csv", ".ods"],
    "powerpoint": [".pptx", ".ppt", ".odp"],
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff", ".webp"],
    "archives": [".zip", ".rar", ".tar", ".7z", ".gz", ".bz2"],
    "executables": [".exe", ".msi", ".apk", ".bin", ".run"],
    "scripts": [".sh", ".bat", ".ps1", ".cmd"],
    "python": [".py", ".pyc", ".pyo"],
    "cpp": [".cpp", ".hpp"],
    "c": [".c", ".h"],
    "java": [".java", ".class", ".jar"],
    "javascript": [".js", ".mjs"],
    "php": [".php", ".phtml"],
    "html": [".html", ".htm"],
    "css": [".css", ".scss", ".sass"],
    "ruby": [".rb"],
    "typescript": [".ts"],
    "json": [".json"],
    "xml": [".xml"],
    "yaml": [".yaml", ".yml"],
    "markdown": [".md"],
    "database": [".sql", ".sqlite", ".db", ".mdb"],
    "system": [".dll", ".sys", ".ini", ".log", ".cfg"],
}


def check_dict(func):
    def wrapper(*args, **kwargs):  # Accepts any arguments
        if (
            args and isinstance(args[0], dict) and args[0]
        ):  # Check if argument is a non-empty dictionary
            for key, value in args[0].items():
                if (
                    not isinstance(value, list) or not value
                ):  # Check if value is a non-empty list
                    raise ValueError(
                        "Invalid structure: '{}' must have a non-empty list as a value.".format(
                            key
                        )
                    )
            return func(*args, **kwargs)
        else:
            raise ValueError(
                "It's not possible to execute the function because the provided dictionary is empty."
            )

    return wrapper


def is_directory_not_empty(directory_path: str) -> bool:
    return bool(os.listdir(directory_path))


def move_file_to_new_directory(
    destination_directory: str, source_directory: str, filename: str
):

    # Make sure the destination directory exists
    os.makedirs(destination_directory, exist_ok=True)

    # Define source and destination paths
    source = os.path.join(source_directory, filename)
    destination = os.path.join(destination_directory, filename)

    # Move the file to the new location
    shutil.move(source, destination)


@check_dict
def files_sorter(files_dict: dict, source_directory: str, new_directory: str):
    # Make sure the sorted directory exists
    os.makedirs(new_directory, exist_ok=True)
    sorted_files_path = os.path.abspath(new_directory)
    unsorted_files_path = os.path.abspath(source_directory)
    destination_directory = ""

    # Loop through directories and file types in the dictionary
    for direc_name, file_type_list in files_dict.items():
        # Loop through files in the source directory
        for filename in os.listdir(unsorted_files_path):
            # Check if the file type matches any in the current directory list
            file_ext = os.path.splitext(filename)[1]
            if file_ext in file_type_list:
                # Update destination_directory if file matches the types
                destination_directory = os.path.join(sorted_files_path, direc_name)
                move_file_to_new_directory(
                    destination_directory, unsorted_files_path, filename
                )

    # Iteration to bring not sorted files
    if is_directory_not_empty(unsorted_files_path):
        destination_directory = os.path.join(sorted_files_path, "others")
        for filename in os.listdir(unsorted_files_path):
            move_file_to_new_directory(
                destination_directory, unsorted_files_path, filename
            )
        # After the iteration, check if it's not really empty
        if is_directory_not_empty(unsorted_files_path):
            raise RuntimeError(
                "In Directory: {} some files could not be sorted".format(
                    unsorted_files_path
                )
            )


def main():
    parser = argparse.ArgumentParser(
        description="""
    File Sorter: A tool to organize files into subdirectories based on their types.
    
    This script takes a directory as input and sorts the files inside it into categorized 
    subdirectories based on file extensions. Files without a matching type will be placed 
    in a directory named 'others'.
    
    Supported file types include, but are not limited to:
    - Video: .mp4, .mkv, .avi, .mov, .webm, .flv
    - Audio: .mp3, .wav, .flac, .aac, .ogg, .m4a
    - Documents: .docx, .txt, .rtf, .odt
    - PDFs: .pdf
    - Spreadsheets: .xlsx, .xls, .csv, .ods
    - Presentations: .pptx, .ppt, .odp
    - Images: .jpg, .jpeg, .png, .gif, .bmp, .svg, .tiff, .webp
    - Archives: .zip, .rar, .tar, .7z, .gz, .bz2
    - Executables: .exe, .msi, .apk, .bin, .run
    - Scripts: .sh, .bat, .ps1, .cmd
    - Python: .py, .pyc, .pyo
    - C/C++: .cpp, .hpp, .c, .h
    - Java: .java, .class, .jar
    - JavaScript: .js, .mjs
    - PHP: .php, .phtml
    - HTML: .html, .htm
    - CSS: .css, .scss, .sass
    - Ruby: .rb
    - TypeScript: .ts
    - JSON: .json
    - XML: .xml
    - YAML: .yaml, .yml
    - Markdown: .md
    - Database: .sql, .sqlite, .db, .mdb
    - System: .dll, .sys, .ini, .log, .cfg
    
    Usage:
    - --directory or --dir: Specify the directory to be sorted.
    
    Example:
    - python filesorter.py --directory /path/to/my/files

    Over the relative path:

    - python filesorter.py --directory files
    """
    )

    parser.add_argument(
        "--directory", "--dir", type=str, required=True, help="Directory to be sorted"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Ensure the directory exists
    if not os.path.isdir(args.directory):
        print("Directory '{}' doesn't exist.".format(args.directory))
        return

    print("Sorting files in directory: '{}'".format(args.directory))
    new_directory = "{}_sorted".format(args.directory)

    files_sorter(files_types, args.directory, new_directory)

    print("All files were sorted in directory: '{}' ✅".format(new_directory))


if __name__ == "__main__":
    main()
