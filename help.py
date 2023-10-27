import os
import shutil
from datetime import datetime

# Function to get the last modification date of a file
def get_modification_date(file_path):
    modification_time = os.path.getmtime(file_path)
    return datetime.utcfromtimestamp(modification_time)

while True:
    while True:
        # Prompt the user for origin and target directory paths
        origin_directory = input("Enter the origin directory path: ")
        target_directory = input("Enter the target directory path: ")

        # Check if the entered paths are valid
        if not os.path.isdir(origin_directory) or not os.path.isdir(target_directory):
            print("Error: One or both of the entered paths are invalid.")
            continue  # Restart the loop to reprompt the user

        # Confirm paths with the user
        print(f"\nYou entered the following paths:")
        print(f"Origin Directory: {origin_directory}")
        print(f"Target Directory: {target_directory}")

        confirm = input("\nPress Enter to proceed with the above paths, or type 'abort' to cancel: ")

        if confirm.lower() == 'abort':
            print("Program aborted.")
            break  # Break out of the inner loop to re-prompt for directories
        else:
            break  # Exit the inner loop if the user confirms the paths

    if confirm.lower() == 'abort':
        continue  # Restart the outer loop to begin again
    else:
        # Create a list to keep track of moved files for potential undo
        moved_files = []

        # Create a list to keep track of created YYYY-MM directories for potential undo
        created_directories = []

        # Iterate through the files in the origin directory and its subfolders
        for root, dirs, files in os.walk(origin_directory):
            for file in files:
                # Get the full path of the file
                file_path = os.path.join(root, file)

                # Get the last modification date of the file
                modification_date = get_modification_date(file_path)

                # Determine target folder based on whether there are subdirectories
                if root == origin_directory:
                    target_folder = os.path.join(target_directory, modification_date.strftime('%Y-%m'))
                else:
                    rel_path = os.path.relpath(root, origin_directory)
                    target_folder = os.path.join(target_directory, rel_path, modification_date.strftime('%Y-%m'))
                
                os.makedirs(target_folder, exist_ok=True)

                # Move the file to the target folder
                shutil.move(file_path, os.path.join(target_folder, file))

                # Add moved file to the list for potential undo
                moved_files.append((os.path.join(target_folder, file), file_path))

                # Add created directory to the list for potential undo
                created_directories.append(target_folder)

                # Print verbose output
                print(f"Moved {file} to {target_folder}")

        # Prompt user if they want to undo the action
        while True:
            undo = input("Type 'undo' to undo the last action, or press Enter to continue: ")

            if undo.lower() == 'undo':
                for target_path, source_path in moved_files:
                    shutil.move(target_path, source_path)
                    print(f"Undid move of {os.path.basename(source_path)}")

                # Remove created YYYY-MM directories
                for directory in created_directories:
                    try:
                        os.rmdir(directory)
                        print(f"Removed directory: {directory}")
                    except OSError as e:
                        print(f"Error removing directory: {e}")

                break  # Exit the loop if the user types 'undo'
            elif not undo:  # Check if input is empty (user pressed Enter)
                print("Actions not undone. Program completed.")
                break  # Exit the loop if the user presses Enter
            else:
                print("Invalid input. Please type 'undo' or press Enter.")
