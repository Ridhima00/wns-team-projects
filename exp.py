import streamlit as st
import cv2
import numpy as np
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
from io import BytesIO
from docx import Document
import tempfile
import os
 #Path to the uploaded file




# Function to extract text boxes using pytesseract
def get_text_boxes(image):
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        d = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
        boxes = []
        for i in range(len(d['level'])):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            boxes.append((x, y, w, h))
        return boxes
    except Exception as e:
        st.error(f"Error in extracting text boxes with Tesseract: {e}")
        return []



    # Helper function to draw bounding boxes
# Helper function to draw bounding boxes
def draw_boxes(image, boxes, color=(255, 0, 0), thickness=2):
    try:
        for box in boxes:
            x, y, w, h = box
            image = cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness)
        return image
    except Exception as e:
        st.error(f"Error in drawing bounding boxes: {e}")
        return image




def process_document(doc):
    try:
        if isinstance(doc, str):  # Check if 'doc' is a file path (string)
            if doc.endswith('.pdf'):
                st.write("PDF file detected.")
                try:
                    images = convert_from_path(doc, poppler_path=r'D:\Downloads\Release-24.07.0-0\poppler-24.07.0\Library\bin')
                    img = np.array(images[0])
                except Exception as e:
                    st.error(f"Failed to convert PDF to image: {e}")
                    return None

            elif doc.endswith('.docx'):
                st.write("DOCX file detected.")
                try:
                    document = Document(doc)
                    img = None
                    for rel in document.part.rels.values():
                        if "image" in rel.target_ref:
                            img = Image.open(BytesIO(rel.target_part.blob))
                            img = np.array(img)
                            break
                    if img is None:
                        st.error("No image found in the Word document.")
                        return None
                except Exception as e:
                    st.error(f"Failed to process DOCX file: {e}")
                    return None

            else:
                st.error("Unsupported file format.")
                return None

        # Detect text boxes
        try:
            boxes = get_text_boxes(img)
            if not boxes:
                st.warning("No text boxes detected.")
        except Exception as e:
            st.error(f"Error in text box detection: {e}")
            return None

        # Draw bounding boxes
        try:
            img_with_boxes = draw_boxes(img, boxes, color=(0, 255, 0))
            return img_with_boxes
        except Exception as e:
            st.error(f"Error in drawing boxes on image: {e}")
            return None

    except Exception as e:
        st.error(f"An unexpected error occurred in processing the document: {e}")
        return None






def main():
    st.title("Invoice Bounding Box Detection")

    uploaded_file = st.file_uploader("Upload an invoice (PDF or Word)", type=['pdf', 'docx'])

    if uploaded_file is not None:
        try:
            # Create a temporary file to store the uploaded file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_file_path = tmp_file.name

            # Process the document
            img_with_boxes = process_document(tmp_file_path)

            if img_with_boxes is not None:
                st.image(img_with_boxes, channels="RGB")
            else:
                st.error("Failed to process the document.")

        except Exception as e:
            st.error(f"An error occurred while processing the uploaded file: {e}")

        finally:
            # Clean up the temporary file
            if os.path.exists(tmp_file_path):
                os.remove(tmp_file_path)


if __name__ == "__main__":
    main()
