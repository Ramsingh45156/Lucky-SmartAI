import sys
import time
import webbrowser
from Brain_Model import mind
import threading
import wikipedia
from Text_to_speek import speak
# from google_search import google_search  # Assuming you have a google_search function



def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.075)  # Adjust the sleep duration for the animation speed
    print()  



qa_file_path = r"C:\Users\ramsi\Desktop\Lucky5.1\Qus_Data.txt"

def load_qa_data(file_path):
    qa_dict = {}

    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()  # Corrected line assignment with '='
            if not line:
                continue

            parts = line.split(":")
            if len(parts) != 2:
                continue

            q, a = parts  # Corrected assignment with '='

            qa_dict[q] = a

    return qa_dict

# Load data from the file
qa_dict = load_qa_data(qa_file_path)


def save_qa_data(file_path, qa_dict):
    with open(file_path, "w", encoding="utf-8") as f:
        for q, a in qa_dict.items():
            f.write(f"{q}:{a}\n")  # Write each question-answer pair to the file




def wiki_search(prompt):
    # Remove unnecessary terms from the prompt
    search_prompt = prompt.replace("Lucky", "").replace("wikipedia", "").strip()

    try:
        # Get Wikipedia summary
        wiki_summary = wikipedia.summary(search_prompt, sentences=2)

        # Start the animation and speech threads
        animate_thread = threading.Thread(target=print_animated_message, args=(wiki_summary,))
        speak_thread = threading.Thread(target=speak, args=(wiki_summary,))

        animate_thread.start()
        speak_thread.start()

        animate_thread.join()
        speak_thread.join()

        # Store the summary in qa_dict
        qa_dict[search_prompt] = wiki_summary

        # Save the updated qa_dict to a file
        save_qa_data(qa_file_path, qa_dict)

    except wikipedia.exceptions.DisambiguationError as e:
        speak("There is a disambiguation page for the given query. Please provide more specific information.")
        print("There is a disambiguation page for the given query. Please provide more specific information.")
    
    except wikipedia.exceptions.PageError:
        google_search(prompt)  
def google_search(query):
    
    query = query.replace("who is ", "").strip()

    if query:
        
        url = "https://www.google.com/search?q=" + query
        webbrowser.open_new_tab(url)

        
        speak("You can see search results for " + query + " in Google on your screen.")

        
        print("You can see search results for " + query + " in Google on your screen.")
    else:
        
        speak("I didn't catch what you said.")
        print("I didn't catch what you said.")



def Brain(text):
    try:
        response = mind(text)  

        if not response:
            wiki_search(text)  
            return

        
        animate_thread = threading.Thread(target=print_animated_message, args=(response,))
        speak_thread = threading.Thread(target=speak, args=(response,))

        animate_thread.start()
        speak_thread.start()

        animate_thread.join()
        speak_thread.join()

        
        qa_dict[text] = response 
        save_qa_data(qa_file_path, qa_dict)

    except Exception as e:
       
        print(f"An error occurred: {str(e)}")
    
    
        wiki_search(text)
        
# Brain("hello")