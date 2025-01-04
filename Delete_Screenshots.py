import os
from datetime import datetime

def delete_screenshots(directory):
    try:
        # List all files in the directory
        files = os.listdir(directory)
        
        # Filter files that start with 'Screenshot' and are files
        screenshots = [
            (file, os.path.getmtime(os.path.join(directory, file)))
            for file in files
            if file.startswith("Screenshot") and os.path.isfile(os.path.join(directory, file))
        ]
        
        # Sort files by modification time (ascending)
        screenshots.sort(key=lambda x: x[1])  # x[1] is the modification time
        
        # Count the files
        count = len(screenshots)
        
        if count == 0:
            print("No files starting with 'Screenshot' found.")
            return
        
        # Display the files to be deleted
        print(f"The following {count} files will be deleted (ordered by date):")
        for file, mtime in screenshots:
            mtime_readable = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
            print(f"{os.path.join(directory, file)} (Last Modified: {mtime_readable})")
        
        # Confirm deletion
        confirmation = input("Do you want to delete these files? (yes/no): ").strip().lower()
        if confirmation == 'yes':
            for file, _ in screenshots:
                file_path = os.path.join(directory, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            print(f"All {count} files have been deleted.")
        else:
            print("No files were deleted.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define the directory containing the screenshots
screenshot_directory = '/Users/sai/Desktop'

# Run the function
delete_screenshots(screenshot_directory)
