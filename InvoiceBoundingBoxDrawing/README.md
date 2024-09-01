
---

## Invoice Bounding Box Detection

### Overview

This project is a web-based application built using Streamlit that allows users to upload invoice documents in PDF or Word (.docx) formats and detects text within the documents. It highlights the detected text by drawing bounding boxes around it using Optical Character Recognition (OCR) with Tesseract. The application is designed to help users visualize and verify the textual content of invoices.

### Features

- **Supports PDF and Word documents**: Upload invoices in `.pdf` or `.docx` formats.
- **Text Detection with Bounding Boxes**: Uses OCR to detect text in documents and draws bounding boxes around the detected text regions.
- **Interactive Web Interface**: Built with Streamlit to provide an easy-to-use interface.
- **Error Handling**: Robust error handling to manage unsupported formats, processing errors, and other exceptions.

### Packages and Libraries

Below is a detailed description of the libraries and packages used in this project:

- **Streamlit (streamlit)**:  
  A framework for building web applications for machine learning and data science. It is used here to create an interactive web UI that allows users to upload files and display results.

- **OpenCV (cv2)**:  
  An open-source computer vision library used for image processing tasks such as reading images, converting images to grayscale, and drawing bounding boxes.

- **NumPy (numpy)**:  
  A powerful library for numerical computing in Python. In this project, it is used for array manipulations and converting images from the PIL format to a format suitable for OpenCV.

- **pdf2image (pdf2image)**:  
  A library that converts PDF files to images. It uses the Poppler toolset to render PDFs. This project uses pdf2image to convert uploaded PDF invoices into images for text detection.

- **Pillow (PIL) (PIL)**:  
  The Python Imaging Library (PIL), also known as Pillow, is a library for image processing in Python. It is used to load images extracted from DOCX files and convert them to a format suitable for OpenCV processing.

- **Pytesseract (pytesseract)**:  
  A Python wrapper for Google's Tesseract-OCR Engine. It is used to recognize and extract text from images. This project uses Pytesseract to detect text in converted images and extract bounding box coordinates.

- **python-docx (python-docx)**:  
  A library for creating, modifying, and extracting information from Microsoft Word (.docx) files. In this project, it is used to extract images embedded in Word documents.

- **io (io)**:  
  A standard Python module that provides core tools for working with streams (input/output). `BytesIO` from `io` is used here to handle binary streams when reading image data from Word documents.

- **tempfile (tempfile)**:  
  A module for creating temporary files and directories. It is used to store uploaded files temporarily during the processing stage.

- **os (os)**:  
  A standard library in Python that provides a way to interact with the operating system. It is used here for file operations like deleting temporary files after processing.

### Installation

To run this project, you need to have Python installed on your system. Follow these steps to set up the project:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/invoice-bounding-box-detection.git
   cd invoice-bounding-box-detection
   ```

2. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Required Packages**:

   Make sure you have all required packages installed. You can install them using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

   If the `requirements.txt` is not available, install the packages manually:

   ```bash
   pip install streamlit opencv-python-headless numpy pdf2image pillow pytesseract python-docx
   ```

4. **Install Tesseract-OCR**:

   - You need to install Tesseract-OCR on your system. For Windows, download the installer from Tesseract's [GitHub page](https://github.com/tesseract-ocr/tesseract).

   - For macOS, use Homebrew:

     ```bash
     brew install tesseract
     ```

   - For Linux, use apt-get:

     ```bash
     sudo apt-get install tesseract-ocr
     ```

5. **Install Poppler**:

   - `pdf2image` requires Poppler for converting PDFs to images. Download and install Poppler from [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/) or use Homebrew on macOS:

     ```bash
     brew install poppler
     ```

### Usage

1. **Run the Application**:

   To start the Streamlit app, run the following command in your terminal:

   ```bash
   streamlit run app.py
   ```

2. **Upload an Invoice**:

   The app will open in your web browser. Use the **file uploader** to upload a PDF or DOCX invoice document.

3. **View Results**:

   After uploading, the app will process the document, detect text, and display the image with bounding boxes around the detected text regions.

### Code Explanation

1. **Helper Function: Drawing Bounding Boxes**  
   The `draw_boxes()` function uses OpenCV to draw rectangles around detected text regions on the input image.

2. **Text Detection with Pytesseract**  
   The `get_text_boxes()` function utilizes Tesseract-OCR to extract text and bounding box coordinates from an image.

3. **Document Processing Function**  
   The `process_document()` function handles different types of documents (PDF or DOCX), converts them to images, detects text, and draws bounding boxes.

4. **Streamlit User Interface**  
   The `main()` function creates a web interface for uploading files and displaying results using Streamlit.

### Output
1. **Bounding Box Detection Result:**
![Screenshot 2024-08-28 074009](https://github.com/user-attachments/assets/8a092e58-20ce-4522-af22-eefe0551230c)

This screenshot shows the detected bounding boxes around the text in the uploaded invoice. The application uses Tesseract-OCR to identify and highlight the text within the document
2. **Application Interface:**
![Screenshot 2024-09-01 204122](https://github.com/user-attachments/assets/442e4b6d-5bf2-4181-b264-1257001c2fb0)

This screenshot displays the main interface of the Streamlit application, where users can upload their invoice documents.

### Known Issues

- **Poppler Path**: Make sure to set the correct `poppler_path` in the `convert_from_path()` function to point to your local Poppler installation.
- **Memory Usage**: Processing large documents might lead to high memory usage. Consider optimizing or resizing images if you encounter performance issues.



### Acknowledgments

- Streamlit for providing an amazing framework for building web apps.
- Tesseract-OCR for OCR capabilities.
- OpenCV for image processing.
- pdf2image for PDF to image conversion.
- Poppler for rendering PDFs to images.

---

