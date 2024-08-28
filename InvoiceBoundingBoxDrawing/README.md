Invoice Bounding Box Detection
Project Background
This project is designed to detect and draw bounding boxes around key text fields in invoices. The primary aim is to automate the process of identifying important sections like invoice numbers, dates, item descriptions, and totals, among others. The project uses the following key technologies:

OpenCV: For image processing and drawing bounding boxes.
Tesseract OCR: For text detection and extraction from images.
Streamlit: For creating an interactive user interface that allows users to upload invoices and see the bounding box detection in action.
pdf2image and python-docx: For converting PDF and DOCX files into images.
How to Run the Code
Install the required dependencies: Ensure you have Python installed. Then, install the required packages using pip:

bash
Copy code
pip install streamlit opencv-python-headless numpy pdf2image pillow pytesseract python-docx
Set up Tesseract: Install Tesseract OCR on your system and ensure it is added to your system's PATH. You can download Tesseract here.

Install Poppler: If you haven't done so already, install Poppler, which is required to convert PDF files to images. Ensure that the poppler_path in the code points to the correct location of the Poppler binaries.

Run the Streamlit app: Navigate to the directory where your invoice_bounding_box_drawing.py file is located, and run the following command:

bash
Copy code
streamlit run invoice_bounding_box_drawing.py
This command will start the Streamlit application and open it in your default web browser.

Upload and Process Invoices: In the Streamlit app, upload a PDF or DOCX file of an invoice. The app will then process the document and display an image with bounding boxes drawn around detected text fields.

Example Screenshots
1. Application Interface
[Screenshot 2024-08-28 073920](https://github.com/user-attachments/assets/ac95f0d1-990c-461e-8cfe-6f4a672732c4)

Description: This screenshot shows the initial interface of the application where users can upload their invoices for processing.

2. Processed Invoice with Bounding Boxes
[Screenshot 2024-08-28 074009](https://github.com/user-attachments/assets/5a1cf893-0600-465d-9c8e-60279581941d)
Description: This screenshot shows the result after uploading an invoice. The application successfully detects key text fields and draws bounding boxes around them.

Troubleshooting
Common Issues
Tesseract Not Found: Ensure Tesseract is installed and added to the PATH environment variable.
Unsupported File Format: Ensure that only PDF or DOCX files are uploaded. The app does not support other file formats.
Final Remarks
This project provides a basic yet effective way to automate the detection of important fields in invoices. With further improvements, it can be expanded to include more advanced features like categorization of detected fields, export of data in structured formats, and integration with other financial tools.
