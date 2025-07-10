import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory(title="Select folder to organize")

if not directory:
    print("No folder selected. Exiting.")
    exit()

for filename in os.listdir(directory):
    if filename.startswith('.'):
        continue  # Skip hidden files
    filepath = os.path.join(directory, filename)
    if not os.path.isfile(filepath):
        continue  # Skip folders
    ext = os.path.splitext(filename)[1].lstrip('.').upper()
    if not ext:
        continue  # Skip files without extension
    mtime = os.path.getmtime(filepath)
    month_folder = datetime.fromtimestamp(mtime).strftime('%Y-%m')
    ext_folder = os.path.join(directory, ext)
    month_path = os.path.join(ext_folder, month_folder)
    os.makedirs(month_path, exist_ok=True)
    # Handle name conflicts
    target_file = os.path.join(month_path, filename)
    counter = 1
    name, ext_with_dot = os.path.splitext(filename)
    while os.path.exists(target_file):
        target_file = os.path.join(month_path, f"{name}_{counter}{ext_with_dot}")
        counter += 1
    try:
        shutil.move(filepath, target_file)
        print(f"Moved '{filename}' to '{month_path}'")
    except Exception as e:
        print(f"Could not move '{filename}': {e}")
