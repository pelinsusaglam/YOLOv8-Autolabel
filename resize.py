from PIL import Image
import os

# Target dimensions for resizing
target_size = (640, 640)

# Specify the folder path containing the images to resize
source_folder = "_images"

# Specify the target folder to save the resized images
target_folder = 'yarisma_goruntu'
os.makedirs(target_folder, exist_ok=True)

# Get and sort all files in the source folder
image_files = [file for file in os.listdir(source_folder) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]
image_files.sort()

# Process each file
for filename in image_files:
    # Create the full file path
    file_path = os.path.join(source_folder, filename)
    
    # Open the image
    with Image.open(file_path) as img:
        # Resize the image
        resized_img = img.resize(target_size)
        
        # Save the resized image to the target folder with the same name
        target_path = os.path.join(target_folder, filename)
        resized_img.save(target_path)
        
        print(f"Image resized and saved: {target_path}")

print("All images have been resized.")

