import os

def rename_images(directory):
    # List the files in the specified directory
    files = os.listdir(directory)
    
    # Filter only .jpg and .png file extensions
    image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    # Sort the files
    image_files.sort()
    
    # Start a counter for renaming files
    counter = 1
    
    for file in image_files:
        # Get the file extension
        ext = os.path.splitext(file)[1]
        
        # Create the new file name
        new_name = f"{counter:06}{ext}"
        
        # Create the old and new file paths
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        
        print(f"{old_path} -> {new_path}")
        
        # Increment the counter
        counter += 1

# Get the directory path from the user
directory_path = "_images"

# Call the function
rename_images(directory_path)
