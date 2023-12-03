# import libraries
import pandas as pd
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import streamlit as st

# Load the dataset with necessary columns
columns = ['password', 'strength']
data = pd.read_csv('password.csv', header=0, usecols=columns)
sample_size = 10000 
data = data.sample(n=sample_size, random_state=42)

# Check for missing values in each column
missing_values = data.isnull().sum()

# Remove the columns with missing values
dataset = data.dropna()
dataset.isnull().sum()

dataset['strength'] = pd.to_numeric(dataset['strength'], errors='coerce')
dataset = dataset.dropna(subset=['strength'])
dataset['strength'] = dataset['strength'].astype('int')

# Text preprocessing
# convert to lowercase
dataset['password'] = dataset['password'].str.lower()
# Remove special characters
dataset['password'] = dataset['password'].str.replace('[^a-zA-Z0-9]', ' ', regex=True)

# Feature engineering
dataset['password_length'] = dataset['password'].apply(len)
dataset['numbers'] = dataset['password'].apply(lambda x: any(char.isdigit() for char in x))
dataset['uppercase'] = dataset['password'].apply(lambda x: any(char.isupper() for char in x))
dataset['symbols'] = dataset['password'].apply(lambda x: any(char in string.punctuation for char in x))
dataset['lowercase'] = dataset['password'].apply(lambda x: any(char.islower() for char in x))

# Split the dataset
X = dataset[['password', 'password_length', 'numbers', 'uppercase', 'symbols', 'lowercase']]
y = dataset['strength']

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1, 3))
X_vectorizer = vectorizer.fit_transform(X['password'])

# Split the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X_vectorizer, y, test_size=0.2, random_state=42)

# Train a  model Random Forest classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)


# Streamlit App
st.title("Password Strength Predictor")
user_input = st.text_input("Enter your password:")
if user_input:
    # Preprocess the input password and extract features
    user_input_vectorizer = vectorizer.transform([user_input])
    user_input_combined = pd.concat([pd.DataFrame(user_input_vectorizer.toarray()), pd.DataFrame({
        'password': [user_input],
        'password_length': [len(user_input)],
        'numbers': [any(char.isdigit() for char in user_input)],
        'uppercase': [any(char.isupper() for char in user_input)],
        'symbols': [any(char in string.punctuation for char in user_input)],
        'lowercase': [any(char.islower() for char in user_input)]
    })], axis=1)

    # Make prediction using the trained model
    prediction = model.predict(user_input_vectorizer)[0]
    st.write(f"Predicted Strength: {prediction}")

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    st.write(f"accuracy: {accuracy}")

