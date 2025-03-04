#!/usr/bin/env python3

import os
import shutil
import argparse


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
                        f"Invalid structure: '{key}' must have a non-empty list as a value."
                    )
            return func(*args, **kwargs)
        else:
            raise ValueError(
                "It's not possible to execute the function because the provided dictionary is empty."
            )

    return wrapper


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
        # After the finteration, check if its not really emphy
        if is_directory_not_empty(unsorted_files_path):
            raise RuntimeError(
                " In Directory : {} some files could not be sorted".format(
                    unsorted_files_path
                )
            )


def main(directory):

    print("Sorting files in directory: '{}'".format(directory))
    new_directory = directory + "_sorted"

    files_sorter(files_types, directory, new_directory)

    print("All files were sorted in directory: '{}' ".format(new_directory) + "\U0000270C")


if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser(
        description="Accepts a directory name as a parameter and moves the files to another directory "
        "with subdirectories according to each file type. The script must be executed over the directory path."
    )

    # Add argument for directory (optional)
    parser.add_argument(
        "--directory", "--dir", type=str, help="Directory to be sorted name"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Ensure that the directory exist in the current path
    if not os.path.isdir(args.directory):
        print(
            " Directory {} doesn't exist in the current working directory".format(
                args.directory
            )
        )
    else:
        # Call the main function with the parsed arguments
        main(args.directory)
