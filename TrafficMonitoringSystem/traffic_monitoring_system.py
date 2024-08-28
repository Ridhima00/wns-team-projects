import cv2
import numpy as np
import tensorflow as tf
import pytesseract
import matplotlib.pyplot as plt
# Set up Tesseract path for license plate recognition
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your path

# Load the pre-trained TensorFlow object detection model
model_dir = r'D:\Downloads\ssd_mobilenet_v2_320x320_coco17_tpu-8\ssd_mobilenet_v2_320x320_coco17_tpu-8\saved_model'
detect_fn = tf.saved_model.load(model_dir)

# Define the category index for relevant objects
category_index = {
    1: {'id': 1, 'name': 'person'},
    3: {'id': 3, 'name': 'car'},
    4: {'id': 4, 'name': 'motorcycle'},
    6: {'id': 6, 'name': 'bus'},
    8: {'id': 8, 'name': 'truck'},
}


# Function to perform object detection
def detect_objects(image):
    input_tensor = tf.convert_to_tensor(image)
    input_tensor = input_tensor[tf.newaxis, ...]
    detections = detect_fn(input_tensor)
    return detections


# Function for counting vehicles crossing a line
def count_vehicles(detections, frame, line_coords):
    vehicle_count = 0
    h, w = frame.shape[:2]
    for i in range(int(detections['num_detections'][0])):
        box = detections['detection_boxes'][0][i].numpy()
        score = detections['detection_scores'][0][i].numpy()
        class_id = int(detections['detection_classes'][0][i].numpy())

        if score > 0.5 and class_id in [3, 4, 6, 8]:  # Cars, Motorcycles, Buses, Trucks
            (startY, startX, endY, endX) = (box[0] * h, box[1] * w, box[2] * h, box[3] * w)
            cv2.rectangle(frame, (int(startX), int(startY)), (int(endX), int(endY)), (0, 255, 0), 2)

            # Check if the vehicle crosses the line
            midY = (startY + endY) / 2
            if line_coords[0][1] < midY < line_coords[1][1]:
                vehicle_count += 1
                label = f"Vehicle {int(score * 100)}%"
                cv2.putText(frame, label, (int(startX), int(startY) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),
                            2)
    return vehicle_count


# Function for license plate recognition
def recognize_license_plate(frame, box):
    h, w = frame.shape[:2]
    (startY, startX, endY, endX) = (box[0] * h, box[1] * w, box[2] * h, box[3] * w)
    license_plate_region = frame[int(startY):int(endY), int(startX):int(endX)]
    gray_plate = cv2.cvtColor(license_plate_region, cv2.COLOR_BGR2GRAY)
    license_text = pytesseract.image_to_string(gray_plate, config='--psm 8')
    return license_text.strip()


# Main function to process video and perform detection
def process_video(video_path):
    # Attempt to open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Error: Frame not read correctly. Exiting...")
            break

        if frame is None or frame.size == 0:
            print("Error: Received empty frame. Exiting...")
            break

        # Convert frame from BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame using Matplotlib
        plt.imshow(rgb_frame)
        plt.axis('off')  # Hide the axis
        plt.show(block=False)  # Show the frame without blocking
        plt.pause(0.01)  # Pause to update the plot

        # Close the plot to display the next frame
        plt.close()

    cap.release()

    cv2.destroyAllWindows()


# Run the video processing function
process_video(r'D:\Downloads\traffic.mp4')  # Replace with your video file or 0 for webcam
