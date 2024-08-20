import cv2

# Open video file or capture device
cap = cv2.VideoCapture('traffic.mp4')  # Replace 'traffic.mp4' with 0 for webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Display the frame
    cv2.imshow('Traffic Monitoring', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import cv2

# Load the pre-trained model
net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt', 'MobileNetSSD_deploy.caffemodel')

# Class labels that the model can detect
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow",
           "dog", "motorbike", "person", "pottedplant",
           "sofa", "train", "tvmonitor"]

cap = cv2.VideoCapture('traffic.mp4')  # Replace 'traffic.mp4' with 0 for webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Prepare the frame for object detection
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.2:  # Filter weak detections
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('Traffic Monitoring', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Assume `frame` contains an image with a vehicle's license plate
license_plate = frame[startY:endY, startX:endX]  # Crop the region where the license plate is located
gray = cv2.cvtColor(license_plate, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)[1]

# Use Tesseract to detect text
text = pytesseract.image_to_string(thresh, config='--psm 8')
print("Detected License Plate Text:", text)
# Assume you have coordinates for a line
line = [(100, 300), (400, 300)]  # Define your line points

# Count vehicles crossing the line
vehicle_count = 0

# Update this within your detection loop
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]

    if confidence > 0.2:
        idx = int(detections[0, 0, i, 1])
        if CLASSES[idx] in ["car", "bus", "motorbike"]:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # Simple logic to check if a vehicle crossed the line
            if startY < line[1][1] < endY:
                vehicle_count += 1
                print(f"Vehicle crossed the line. Total count: {vehicle_count}")

            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
            cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.line(frame, line[0], line[1], (0, 0, 255), 2)  # Draw the line on the frame
cv2.imshow('Traffic Monitoring', frame)
# Assume you have coordinates for a line
line = [(100, 300), (400, 300)]  # Define your line points

# Count vehicles crossing the line
vehicle_count = 0

# Update this within your detection loop
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]

    if confidence > 0.2:
        idx = int(detections[0, 0, i, 1])
        if CLASSES[idx] in ["car", "bus", "motorbike"]:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # Simple logic to check if a vehicle crossed the line
            if startY < line[1][1] < endY:
                vehicle_count += 1
                print(f"Vehicle crossed the line. Total count: {vehicle_count}")

            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
            cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.line(frame, line[0], line[1], (0, 0, 255), 2)  # Draw the line on the frame
cv2.imshow('Traffic Monitoring', frame)
