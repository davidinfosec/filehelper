# File Organizer Tool

The File Organizer Tool is a Python script designed to help you efficiently organize files based on their last modification dates. This tool allows you to specify an origin directory and a target directory, and it will move files to subfolders within the target directory, grouped by the year and month of their last modification.

## How to Use

1. Run the Script

    Make sure you have Python installed on your system. Run the script using a Python interpreter.

    ```bash
    python help.py
    ```

2. Enter Paths

    You will be prompted to enter the origin directory (where your unorganized files are located) and the target directory (where you want the organized files to be moved).

3. Confirm Paths

    Verify the entered paths. If they are correct, press Enter. If you want to abort, type 'abort' and press Enter.

4. Organizing Files

    The tool will create subfolders in the target directory based on the last modification dates of the files. Each file will be moved to the corresponding subfolder (e.g., YYYY-MM format).

5. Undo Action (Optional)

    After organizing, you have the option to undo the last action. If you choose to undo, the files will be moved back to their original locations, and any created subfolders will be removed.

## Notes

- The script keeps track of moved files for potential undo. However, keep in mind that once the script is closed, this history is lost.
- Use caution when organizing files, especially in directories with important data. Always make sure you have backups before running the tool.

## Requirements

- Python 3.x
- Standard Python libraries (os, shutil, datetime)

## License

This tool is released under the MIT License.

Remember to include any additional information specific to your tool or project. If there are any special instructions, dependencies, or considerations, be sure to mention them in the README.
