import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from joblib import dump

# Load the dataset
file_path = r'D:\Downloads\test (1).csv'
df = pd.read_csv(file_path)

# Handle missing values in the 'text' column
df['text'] = df['text'].fillna('')

# Use 'text' column as input and 'sentiment' column as target
X = df['text']
y = df['sentiment']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline to vectorize the text data and train a Naive Bayes model
model = Pipeline([('vect', CountVectorizer()), ('clf', MultinomialNB())])

# Train the model
model.fit(X_train, y_train)

# Save the trained model
model_path = 'sentiment_model_custom.joblib'
dump(model, model_path)
