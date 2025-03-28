import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from Text_to_speek import speak

# Load the JSON data
with open(r'C:\Users\ramsi\Desktop\Lucky5.1\data.json', encoding='utf-8') as file:
    data = json.load(file)

# Extract training data
training_data = []
for intent in data.get('intents', []):
    if 'patterns' in intent:
        for pattern in intent['patterns']:
            training_data.append((pattern, intent['tag']))
    else:
        print(f"Warning: 'patterns' key is missing in intent: {intent}")

# Check if training_data is empty
if not training_data:
    print("Error: No training data found.")
    exit()

# Prepare features and labels
X, y = zip(*training_data)

# Convert text data to numerical format
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X, y)

# Function to get response
def get_response(user_input):
    # Convert user input to numerical format
    user_input_vectorized = vectorizer.transform([user_input])

    # Predict the intent
    predicted_intent = classifier.predict(user_input_vectorized)[0]

    # Get a random response for the predicted intent
    for intent in data.get('intents', []):
        if intent.get('tag') == predicted_intent:
            responses = intent.get('responses', [])
            if responses:
                return random.choice(responses)
    
    return "I'm sorry, I don't have a response for that."

# Example usage
# while True:
#     user_input = input("User: ")
#     response = get_response(user_input)
#     speak(response)
