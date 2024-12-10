# YOLOv8-Autolabel
This repository is created to automatically label and organize images for object detection tasks using YOLOv8.

YOLOv8 is the version of the You Only Look Once (YOLO) series, a state-of-the-art, real-time object detection model. YOLOv8 builds upon the previous iterations, offering faster inference times, improved accuracy, and greater flexibility for tasks such as image classification, object detection, and segmentation.

AutoLabel is a repository designed to streamline the labeling process for object detection tasks, particularly when working with YOLO models. It provides various utilities to assist with image preprocessing, annotation, and label generation automatically.

### Features

The repository includes several scripts that enable the following:

* Frame Extraction: Extract frames from videos at specified intervals (e.g., every 2 seconds).
* Image Resizing: Resize images to a target size (e.g., 640x640) for consistent input into YOLO models.
* ROI Selection: Manually select points in images to define Regions of Interest (ROI) for further analysis.
* Bounding Box Normalization: Normalize bounding box coordinates for YOLO format, ensuring consistency across different image resolutions.
* Label Generation: Use YOLOv8’s pre-trained model to automatically generate labels for object detection tasks in YOLO format.
