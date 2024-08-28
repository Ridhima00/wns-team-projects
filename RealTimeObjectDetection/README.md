Real-Time Object Detection using YOLOv5 and Flask
Project Background
This project demonstrates a real-time object detection application using the YOLOv5 model and a Flask web server. It utilizes your computer's webcam to capture live video, detect objects in real-time, and display the results on a web interface. YOLOv5 (You Only Look Once version 5) is a popular deep-learning model known for its speed and accuracy in object detection tasks. The Flask web framework serves the processed video feed, enabling the visualization of detected objects in a user-friendly web page.

How to Run the Code
Prerequisites
Before running the project, make sure you have the following installed on your system:

Python (version 3.6 or above)
pip (Python package installer)
Visual C++ Redistributable (for handling PyTorch dependencies)
Webcam (for real-time video capture)
Required Python Libraries
Flask
OpenCV (cv2)
PyTorch
Installation Steps
Clone the Repository:

bash
Copy code
git clone <repository_url>
cd <repository_directory>
Set up a Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install the Required Libraries:

bash
Copy code
pip install flask opencv-python-headless torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
Running the Application
Start the Flask Server:

Run the following command in your terminal:

bash
Copy code
python your_script_name.py
Replace your_script_name.py with the name of your Python file.

Open the Web Interface:

After running the script, you will see an output similar to:

csharp
Copy code
* Running on http://127.0.0.1:5000
Open your web browser and navigate to http://127.0.0.1:5000 to view the real-time object detection.

Post-Run Examples

Screenshot of the web interface running, displaying real-time object detection with bounding boxes around detected objects.
Screenshot 2024-08-27 204330
Commentary on Post-Run Examples
Real-Time Object Detection: The application captures frames from the webcam, processes them using the YOLOv5 model, and detects various objects like people, cars, etc. Detected objects are highlighted with bounding boxes and labeled with confidence scores.

Web Interface: The Flask server hosts a minimal web page that displays the processed video stream. The feed is updated in real-time, showing object detection results.

Troubleshooting
OSError or DLL Not Found Error: Ensure that all dependencies, especially the Visual C++ Redistributable, are installed. Check your system PATH variable to confirm Python and the virtual environment paths are correctly set.

Camera Access Issues: Make sure that your webcam is connected and accessible. Close any other application that might be using the webcam.

Conclusion
This project demonstrates a straightforward implementation of a real-time object detection system using Python, Flask, and the YOLOv5 model. It provides a hands-on example of combining computer vision and web development to create interactive applications.

Note:
