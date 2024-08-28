from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load

# Initialize FastAPI app
app = FastAPI()

# Load the trained model
model = load('sentiment_model_custom.joblib')

# Define the request model
class TextData(BaseModel):
    text: str

@app.post("/predict")
async def predict_sentiment(data: TextData):
    # Predict the sentiment
    prediction = model.predict([data.text])
    sentiment_mapping = {'negative': 0, 'positive': 1, 'neutral': 2}
    return {"sentiment": sentiment_mapping[prediction[0]]}
