import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Text_to_speek import speak

# Load spaCy's English tokenizer
nlp = spacy.load("en_core_web_sm")

# Load your Q&A dataset from a text file
def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    qna_pairs = [line.strip().split(':', 1) for line in lines if ':' in line]
    dataset = [{'question': q.strip(), 'answer': a.strip()} for q, a in qna_pairs]
    return dataset

# Preprocess the text using spaCy
def preprocess_text(text):
    # Create a doc object
    doc = nlp(text.lower())
    
    # Tokenize, remove stopwords, and apply lemmatization
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    
    return ' '.join(tokens)

# Train the TF-IDF vectorizer
def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(qa['question']) for qa in dataset]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    return vectorizer, X

# Retrieve the most relevant answer
def get_answer(question, vectorizer, X, dataset):
    question = preprocess_text(question)
    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(question_vec, X)
    best_match_index = similarities.argmax()
    return dataset[best_match_index]['answer']

# Main function to process user input
def mind(text):
    dataset_path = r'C:\Users\ramsi\Desktop\Lucky5.1\Qus_Data.txt'  # Ensure this path is correct
    dataset = load_dataset(dataset_path)
    vectorizer, X = train_tfidf_vectorizer(dataset)
    
    answer = get_answer(text, vectorizer, X, dataset)
    # speak(answer)
    return answer

# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ")
#         mind(user_input)
