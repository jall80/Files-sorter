from setuptools import setup, find_packages

setup(
    name="filesorter",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],  
    entry_points={
        "console_scripts": [
            "filesorter=filesorter.main:main", 
        ],
    },
    author="Jose Lopez Li",
    author_email="jall08jall@gmail.com",
    description="This Python script organizes files in a directory by sorting them into subfolders based on their file extensions. It categorizes files into predefined types (e.g., video, audio, documents) and moves them accordingly. Unmatched files are placed in an 'others' folder. The script ensures directories exist, validates inputs, and raises errors if sorting is incomplete. It runs via command line with the --directory argument, creating a <directory>_sorted folder for organized storage.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jall80/Files-sorter", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
