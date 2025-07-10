File Organizer
A Python script that automatically organizes files in a directory by grouping them into folders based on their file type and creation date.
Features

Smart Organization: Groups files by extension type into organized folders
Date-based Sorting: Creates monthly folders (YYYY-MM format) based on file creation date
Duplicate Handling: Automatically handles filename conflicts by adding counters
User-friendly GUI: Simple folder selection dialog using tkinter
Safe Operation: Moves files instead of copying to avoid duplicates

How it Works

Select Directory: Choose the folder you want to organize
File Processing: Script scans all files in the selected directory
Folder Creation: Creates organized structure:
Selected_Directory/
├── PDF/
│   ├── 2024-01/
│   └── 2024-02/
├── Images/
│   ├── 2024-01/
│   └── 2024-02/
└── Documents/
    ├── 2024-01/
    └── 2024-02/

File Movement: Moves files to appropriate folders based on type and date

Installation

Clone this repository:
bashgit clone https://github.com/yourusername/file-organizer.git
cd file-organizer

Run the script:
bashpython file_organizer.py


Requirements

Python 3.6+
tkinter (usually comes with Python)
No additional dependencies required!

Usage
bashpython file_organizer.py

A dialog box will appear asking you to select a folder
Choose the directory you want to organize
The script will automatically organize all files
Check the console for progress updates

Supported File Types
The script automatically categorizes files by extension:

Documents: .pdf, .doc, .docx, .txt, .rtf
Images: .jpg, .jpeg, .png, .gif, .bmp, .svg
Videos: .mp4, .avi, .mkv, .mov, .wmv
Audio: .mp3, .wav, .flac, .aac
Archives: .zip, .rar, .7z, .tar, .gz
Code: .py, .js, .html, .css, .java, .cpp
And more...

Error Handling

Skips hidden files (starting with '.')
Handles permission errors gracefully
Provides clear error messages
Prevents moving folders (files only)

Contributing
Feel free to fork this project and submit pull requests for improvements!
License
This project is open source and available under the MIT License.
Author
Built as part of my AI/ML learning journey - practicing Python fundamentals and file handling.
