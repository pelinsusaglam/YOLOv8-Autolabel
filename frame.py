import cv2
import os

# Specify the path to the video file
video_path = 'video.mov'
# Specify the folder where frames will be saved
output_dir = 'extracted_frames'

# Create the folder if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the video
cap = cv2.VideoCapture(video_path)

# Get the video frame rate (FPS)
fps = cap.get(cv2.CAP_PROP_FPS)
print(f'Video frame rate (FPS): {fps}')

# Specify how many seconds between each saved frame
seconds_between_frames = 2  # For example, save one frame every 2 seconds

# Calculate how many frames to skip between saves
frames_between_saves = int(fps * seconds_between_frames)
print(f'A frame will be saved every {frames_between_saves} frames.')

frame_count = 0

while True:
    # Read frames from the video
    ret, frame = cap.read()
    
    if not ret:
        break  # End the loop when the video ends
    
    # Save frames only at the specified interval
    if frame_count % frames_between_saves == 0:
        frame_filename = os.path.join(output_dir, f'frame_{frame_count:04d}.png')
        cv2.imwrite(frame_filename, frame)
    
    frame_count += 1

# Release the video capture
cap.release()

print(f'{frame_count // frames_between_saves} frames were saved.')

