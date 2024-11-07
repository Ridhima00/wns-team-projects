

# Invoice Categorization Using Natural Language Processing (NLP)

This project demonstrates how to automate invoice categorization using NLP and machine learning. By preprocessing text data and applying a classification model, this solution organizes invoices into meaningful categories, which can streamline financial tracking and reporting.

---

## 1. Importing Packages and Installing Requirements

We start by installing and importing essential Python libraries that support data manipulation, model building, and text preprocessing. 

### Required Packages

- **`pandas`**: A library for data manipulation and analysis, useful for handling structured data in CSV or Excel files. 
- **`numpy`**: Provides support for numerical operations in Python and is used alongside pandas for efficient data handling.
- **`scikit-learn`**: A machine learning library that provides utilities for building and evaluating models, including splitting datasets, vectorizing text, and training models.
- **`spacy`**: A natural language processing library used here to preprocess text by tokenizing and lemmatizing words, making them easier to analyze for patterns.

### Installation

To install these packages, use the following command:

```bash
pip install pandas numpy scikit-learn spacy
```

### Importing Libraries

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import spacy
```

---

## 2. Loading the Datasets

We load both the training and testing data using `pandas`, which reads structured data from specified file paths.

```python
# Load the Train dataset
train_df = pd.read_csv('D:/Downloads/Train.csv')

# Load the Test dataset
test_df = pd.read_csv('D:/Downloads/Test.csv')

# Display the first few rows of both datasets
print("Train Dataset:")
print(train_df.head())

print("\nTest Dataset:")
print(test_df.head())
```

- **`train_df` and `test_df`**: Store data from the `Train.csv` and `Test.csv` files, respectively.
- **`print(train_df.head())`** and **`print(test_df.head())`**: Display the first few rows to verify that the data has loaded correctly.

---

## 3. Preprocessing Text Data with SpaCy

Text data often includes redundant or unnecessary words and punctuation. Using `spacy`, we clean this data by:

   - **Tokenization**: Breaking down text into individual words (tokens).
   - **Lemmatization**: Reducing words to their base forms (e.g., “running” becomes “run”).
   - **Stop Words and Punctuation Removal**: Removing common words (like “the,” “is”) and punctuation.

```python
# Load the SpaCy model
nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    # Process the text using SpaCy
    doc = nlp(text)
    # Extract and join lemmatized tokens, removing stop words and punctuation
    return ' '.join(token.lemma_ for token in doc if not token.is_stop and not token.is_punct)

# Apply preprocessing to the text column in the Train dataset
train_df['processed_text'] = train_df['Invoice_Description'].apply(preprocess_text)

# Apply preprocessing to the text column in the Test dataset
test_df['processed_text'] = test_df['Invoice_Description'].apply(preprocess_text)
```

- **`nlp = spacy.load('en_core_web_sm')`**: Loads a pre-trained English model for tokenizing, lemmatizing, and cleaning text.
- **`preprocess_text(text)`**: Defines a function to:
  - Process the text.
  - Extract each word’s lemma (base form) using `token.lemma_`.
  - Filter out stop words and punctuation.
- **`apply(preprocess_text)`**: Runs this function on each row of `Invoice_Description` in both the train and test datasets, storing cleaned text in new columns `processed_text`.

---

## 4. Model Training

### a) Splitting the Data

We split `train_df` into training and validation sets, allowing us to test the model’s accuracy on unseen data.

```python
# Split the training data into train and validation sets
X_train, X_val, y_train, y_val = train_test_split(train_df['processed_text'], train_df['Product_Category'], test_size=0.2, random_state=42)
```

- **`X_train` and `X_val`**: Hold the text data for training and validation.
- **`y_train` and `y_val`**: Hold the labels (categories) for each set.
- **`test_size=0.2`**: Reserves 20% of the data for validation.
- **`random_state=42`**: Ensures consistent splitting across runs.

### b) Converting Text to TF-IDF Features

We convert the text into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency), which measures word importance.

```python
# Convert text data to TF-IDF features
vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_val_tfidf = vectorizer.transform(X_val)
```

- **`TfidfVectorizer(max_features=5000)`**: Limits features to the 5000 most important terms.
- **`fit_transform(X_train)`**: Learns vocabulary from `X_train` and converts it to a TF-IDF matrix.
- **`transform(X_val)`**: Applies this vocabulary to `X_val`, ensuring the same terms are used.

### c) Training the Model

We use Logistic Regression, a simple classifier for text data, to categorize the invoices.

```python
# Train a logistic regression model
model = LogisticRegression(max_iter=100)
model.fit(X_train_tfidf, y_train)
```

- **`LogisticRegression(max_iter=100)`**: Initializes the model with a limit of 100 iterations.
- **`model.fit(X_train_tfidf, y_train)`**: Trains the model on the TF-IDF features and categories.

### d) Evaluating the Model

We use `accuracy_score` to measure model performance on `X_val`.

```python
# Predict the categories of the validation set
y_val_pred = model.predict(X_val_tfidf)

# Calculate the accuracy of the model on the validation set
val_accuracy = accuracy_score(y_val, y_val_pred)
print(f'Validation Accuracy: {val_accuracy:.2f}')
```

- **`model.predict(X_val_tfidf)`**: Predicts categories for `X_val`.
- **`accuracy_score(y_val, y_val_pred)`**: Compares predicted categories to actual categories and calculates accuracy.

---

## 5. Making Predictions on the Test Set

Finally, we categorize the `Test.csv` data using the trained model.

```python
# Convert the test data to TF-IDF features
X_test_tfidf = vectorizer.transform(test_df['processed_text'])

# Make predictions on the test data
test_predictions = model.predict(X_test_tfidf)

# Add predictions to the Test DataFrame
test_df['Predicted_Category'] = test_predictions

# Save the results to a new CSV file
test_df.to_csv('D:/Downloads/Test_Predictions.csv', index=False)

print("Predictions saved to 'D:/Downloads/Test_Predictions.csv'")
```

- **`vectorizer.transform(test_df['processed_text'])`**: Converts the cleaned test data to TF-IDF features.
- **`model.predict(X_test_tfidf)`**: Predicts categories for `test_df`.
- **`test_df['Predicted_Category'] = test_predictions`**: Adds predictions to `test_df`.
- **`test_df.to_csv('D:/Downloads/Test_Predictions.csv', index=False)`**: Saves predictions as a new CSV file.

---

## Summary

This project showcases how NLP and machine learning can streamline invoice categorization. By preprocessing text, converting it to numerical features, and training a classifier, we automate the organization of invoices into meaningful categories, improving efficiency and making large datasets more manageable and actionable.
