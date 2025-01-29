'''
Author: Joel Jonassi
Email: joeljonassi@outlook.com
Feel free to modify this source code
'''

import os
import shutil
import sys

from sympy.codegen.ast import continue_


def organizer_help():
    print("\033[1mNAME\033[0m")
    print("\torganizer")
    print()
    print("\033[1mSYNOPSIS\033[0m")
    print("\torganizer[DIRECTORY PATH TO BE ORGANIZED]")
    print("\033[1mDESCRIPTION\033[0m")
    print("\tFile Organizer Utility")
    print("\tThis utility helps you organize files in a directory by their file types.")
    print("\tIt scans the current working directory, identifies the file types, and then")
    print("\tmoves each file into a corresponding subdirectory named after its file type.")
    print("\tThis helps in keeping directory neat and organized.")
    print()


argument = ""
GREEN = '\033[92m'
RESET = '\033[0m'
python_executable = sys.executable
current_working_directory = os.getcwd()
if len(sys.argv) == 1:
    answer = input("This Directory will be organized do you want to continue? yes or no\n")
    if answer == 'y' or answer == "yes" :
        argument = "./"
    elif answer == 'no' or answer == 'n':
        argument = "--help"
    else:
        exit(1)
elif len(sys.argv):
    argument = sys.argv[1]

# Define the main folder path
if argument == "--help":
    organizer_help()
else:
    # Create subfolders for different file types
    subfolders = {
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt"],
        "Zip Files":[".zip", ".deb"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Videos": [".mp4", ".avi", ".mov"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Code" :[".py", ".c", ".js", ".json", ".csc", ".apk", ".xml"],
        "Others": []
    }

    for filename in os.listdir(argument):
        file_path = os.path.join(argument, filename)

        # Check if it's a file (not a folder)
        if os.path.isfile(file_path):
            _, extension = os.path.splitext(filename)

            # Determine the appropriate subfolder
            subfolder = "Others"
            for folder, extensions in subfolders.items():
                if extension.lower() in extensions:
                    subfolder = folder
                    break

            # Create the subfolder if it doesn't exist
            subfolder_path = os.path.join(argument, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)

            # Move the file to a subfolder
            destination_path = os.path.join(subfolder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"Moved {filename} to {subfolder} folder." + GREEN + " ✓" + RESET)