import sys
import threading
import time
import pyttsx3
from textblob import TextBlob

def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.040) 
    print()

def speakbasic(text):
    try:
        engine = pyttsx3.init()
        rate = 240
        engine.setProperty('rate', rate)

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[12].id)

        blob = TextBlob(text)
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        pass
    
def speak_M(text):
    speak_thread = threading.Thread(target=speakbasic, args=(text,))
    print_thread = threading.Thread(target=print_animated_message, args=(f"{text}",))

    speak_thread.start()
    print_thread.start()

    speak_thread.join()
    print_thread.join()
    
# speak_M("Hello sir, I am Lucky! AI stands for Artificial Intelligence, which refers to the simulation of human intelligence in machines that are programmed to think and learn like humans.")

# speak_M("ka hal ba")