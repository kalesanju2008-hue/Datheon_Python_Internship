# Task 4 – Automated File Organizer & Cleanup Utility

## Description
A Python-based utility that automatically organizes files in a selected directory based on their file extensions.

The program scans the selected folder, identifies file types, creates category folders, and moves files into their respective folders. It helps maintain a clean and organized directory while reducing manual file management.

## Features
- Scan files in a selected directory.
- Identify file extensions automatically.
- Create category folders when required.
- Organize documents, images, videos, audio, archives, and code files.
- Move unknown file types into an Others folder.
- Prevent overwriting duplicate filenames by adding numbered suffixes.
- Handle permission and file-operation errors.
- Generate an activity log.
- Ask for confirmation before organizing files.
- Never delete files.

## Technologies Used
- Python 3
- OS Module
- Shutil Module
- Logging Module
- pathlib
- File Handling
- Conditional Statements
- Loops and Functions

## Project Files
- `organizer.py` – Main file organization program.
- `organizer.log` – Activity log generated when the program runs.
- `README.md` – Project documentation.

## Installation
1. Install Python 3.
2. Download or clone this repository.
3. Open the terminal in the project folder.

No external Python packages are required.

## How to Run

Run the following command:

`python organizer.py`

Enter the folder path you want to organize and confirm the operation by typing `y`.

## Output
The program automatically creates category folders and moves files into the appropriate folders.

It also displays a summary containing:
- Number of successfully moved files.
- Number of errors.
- Location of the activity log.

## Safety Note
The program does not delete files and avoids overwriting existing filenames. It is recommended to test the utility on a sample folder before organizing important files.
