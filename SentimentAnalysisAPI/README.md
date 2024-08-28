Sentiment Analysis API
Project Background
The Sentiment Analysis API is a simple web application built using FastAPI that uses machine learning algorithms (like Naive Bayes) to analyze text data and determine its sentiment — positive, negative, or neutral. This API can be used for analyzing customer feedback, reviews, or any text input to assess its sentiment, providing valuable insights for businesses.

Getting Started
Prerequisites
Python 3.7 or higher
FastAPI
Uvicorn
scikit-learn
pandas
joblib
Installation
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd SentimentAnalysisAPI
Install the Required Packages:

bash
Copy code
pip install -r requirements.txt
Ensure your requirements.txt file includes:

Copy code
fastapi
uvicorn
scikit-learn
pandas
joblib
Train the Model:

Make sure your train.csv file is in the correct directory and run the following Python script to train the model:

bash
Copy code
python sentiment_model_custom.py
This will generate a model file named sentiment_model_custom.joblib.

Running the Application
Start the FastAPI Server:

bash
Copy code
uvicorn main:app --reload
You should see output similar to:

vbnet
Copy code
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
Access the API Documentation:

Open a browser and navigate to http://127.0.0.1:8000/docs to access the Swagger UI for the API.

Using the API
Example Request
Endpoint: /predict
Method: POST
Request Body:
json
Copy code
{
  "text": "I love this product!"
}
Example Response
Response:
json
Copy code
{
  "sentiment": "1"
}
Screenshots


Screenshot 1: Example API Request and Response
Description: This screenshot demonstrates how to make a request to the /predict endpoint using the Swagger UI, along with the expected response for a sample text input.
[Screenshot 2024-08-28 143101](https://github.com/user-attachments/assets/6a9b26f0-fc09-43e3-a543-1f1858250844)
[Screenshot 2024-08-28 143139](https://github.com/user-attachments/assets/dc89092e-90f0-4f7d-a5b6-ef18ce7675b0)

