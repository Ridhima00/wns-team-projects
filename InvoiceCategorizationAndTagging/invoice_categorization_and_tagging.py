import pandas as pd

# Load the Train dataset
train_df = pd.read_csv('D:/Downloads/Train.csv')

# Display the first few rows to understand the structure
print(train_df.head())
import spacy

# Load the SpaCy model
nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    # Process the text using SpaCy
    doc = nlp(text)
    # Extract and join lemmatized tokens, removing stop words and punctuation
    return ' '.join(token.lemma_ for token in doc if not token.is_stop and not token.is_punct)

# Apply preprocessing to the text column
train_df['processed_text'] = train_df['Invoice_Description'].apply(preprocess_text)
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Split the training data into train and validation sets
X_train, X_val, y_train, y_val = train_test_split(train_df['processed_text'], train_df['Product_Category'], test_size=0.2, random_state=42)

# Convert text data to TF-IDF features
vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_val_tfidf = vectorizer.transform(X_val)

# Train a logistic regression model
model = LogisticRegression(max_iter=100)
model.fit(X_train_tfidf, y_train)

# Predict the categories of the validation set
y_val_pred = model.predict(X_val_tfidf)

# Calculate the accuracy of the model on the validation set
val_accuracy = accuracy_score(y_val, y_val_pred)
print(f'Validation Accuracy: {val_accuracy:.2f}')
# Convert the test data to TF-IDF features
X_test_tfidf = vectorizer.transform(test_df['processed_text'])

# Make predictions on the test data
test_predictions = model.predict(X_test_tfidf)

# Add predictions to the Test DataFrame
test_df['Predicted_Category'] = test_predictions

# Save the results to a new CSV file
test_df.to_csv('D:/Downloads/Test_Predictions.csv', index=False)

print("Predictions saved to 'D:/Downloads/Test_Predictions.csv'")
