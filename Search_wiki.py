import threading
import wikipedia
from Text_to_speek import speak
from Brain import * 

def wiki_search(prompt):
    search_prompt = prompt.replace("jarvis", "").replace("wikipedia", "").strip()

    try:
        wiki_summary = wikipedia.summary(search_prompt, sentences=2)

       
        # animate_thread = threading.Thread(target=print_animated_message, args=(wiki_summary,))
        speak_thread = threading.Thread(target=speak, args=(wiki_summary,))

        # animate_thread.start()
        speak_thread.start()

        # animate_thread.join()
        speak_thread.join()

        
        qa_dict[search_prompt] = wiki_summary  
        save_qa_data(qa_file_path, qa_dict)  

    except wikipedia.exceptions.DisambiguationError as e:
        speak("There is a disambiguation page for the given query. Please provide more specific keywords.")
        # print("Disambiguation Error:", e)

    except wikipedia.exceptions.PageError:
        speak("No Wikipedia page found for the given query. Searching on Google instead.")
        google_search(prompt)  

# wiki_search("how is krishna")