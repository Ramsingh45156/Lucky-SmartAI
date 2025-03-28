import speech_recognition as sr
import threading
from mtranslate import translate
from colorama import Fore, Style, init

init(autoreset=True)

def Trans_hindi_to_english(txt):
    return translate(txt, to_language="en-in")

def listen():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 3000  # Lowered for quick detection
    recognizer.pause_threshold = 0.1  # Faster response
    recognizer.non_speaking_duration = 0.05  # Minimize delay

    with sr.Microphone() as source:
        while True:
            try:
                print(Fore.LIGHTYELLOW_EX + "Listening....", end="", flush=True)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)  # Faster response
                
                recognize_txt = recognizer.recognize_google(audio, language="hi-IN").lower()
                if recognize_txt:
                    translated_txt = Trans_hindi_to_english(recognize_txt)
                    print("\r" + Fore.RED + "Mr.: " + translated_txt)
                    return translated_txt

            except sr.UnknownValueError:
                print("\r" + Fore.YELLOW + "Could not understand.", flush=True)
            except sr.RequestError:
                print("\r" + Fore.RED + "API issue.", flush=True)

def main():
    listen_thread = threading.Thread(target=listen)
    listen_thread.start()
    listen_thread.join()

if __name__ == "__main__":
    while True:
        main()
