from ultralytics import YOLO
import os

# Load the model
model = YOLO("teknofest.pt")

# Get prediction results
results = model.predict(source="yarisma_goruntu", save=True)

# Function to normalize coordinates
def normalize_coordinates(box_coordinates, image_width, image_height):
    normalized_boxes = []
    for box in box_coordinates:
        x_min_norm = box[0] / image_width
        y_min_norm = box[1] / image_height
        width_norm = box[2] / image_width
        height_norm = box[3] / image_height
        normalized_boxes.append([x_min_norm, y_min_norm, width_norm, height_norm])
    return normalized_boxes

# Image dimensions
image_width = 640
image_height = 640

# Folder to save labels
folder_path = 'label'
os.makedirs(folder_path, exist_ok=True)

# Function to create label files
def labelling(class_idss, normalized_box_coordinates, filename):
    with open(os.path.join(folder_path, f"{filename}.txt"), "w") as dosya:
        for class_id, box in zip(class_idss, normalized_box_coordinates):
            x_min_norm, y_min_norm, width_norm, height_norm = box
            # Format coordinates to 6 decimal places
            x_min_str = "{:.6f}".format(x_min_norm)
            y_min_str = "{:.6f}".format(y_min_norm)
            width_str = "{:.6f}".format(width_norm)
            height_str = "{:.6f}".format(height_norm)
            dosya.write(f"{class_id} {x_min_str} {y_min_str} {width_str} {height_str}\n")

# Create label files
import os

# Start counter to match results with sequential names
counter = 1

for result in results:
    box_coordinates = result.boxes.xywh.tolist()
    class_idss = [int(class_id) for class_id in result.boxes.cls.tolist()]  # Convert class IDs to integers
    normalized_box_coordinates = normalize_coordinates(box_coordinates, image_width, image_height)
    
    # Create sequential filename (e.g., 000001.txt)
    filename = f"{counter:06}"
    
    # Save the txt file
    labelling(class_idss, normalized_box_coordinates, filename)
    
    counter += 1

print("All images have been processed and labeled.")

