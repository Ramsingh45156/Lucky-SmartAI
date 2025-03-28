# import speech_recognition as sr
# import os
# import threading
# from mtranslate import translate
# from colorama import Fore,Style,init


# init(autoreset=True)

# def print_loop():
#     while True:
#         print(Fore.LIGHTGREEN_EX+"Listning....",end="",flush=True)
#         print(Style.RESET_ALL,end="",flush=True)
#         print("llll",end="",flush=True)
        
# def Trans_hindi_to_english(txt):
#     english_txt=translate(txt,to_language="en-in")
#     return english_txt

# def listen():
#     recognizer=sr.Recognizer()
#     recognizer.dynamic_energy_threshold=False
#     recognizer.energy_threshold=35000
#     recognizer.dynamic_energy_adjustment_damping=0.1
#     recognizer.dynamic_energy_ratio=1.9
#     recognizer.pause_threshold=0.3
#     recognizer.operation_timeout=None
#     recognizer.pause_threshold=0.2
#     recognizer.non_speaking_duration=0.1
    
#     with sr.Microphone() as source:
#         recognizer.adjust_for_ambient_noise(source)
#         while True:
#             print(Fore.LIGHTYELLOW_EX+"Listning....",end="",flush=True)
#             try:
#                 audio=recognizer.listen(source,timeout=None)
#                 print("\r"+Fore.LIGHTBLUE_EX + "Now Recog....",end="",flush=True)
#                 recognize_txt=recognizer.recognize_google(audio).lower()
#                 if recognize_txt:
#                     translated_tex=Trans_hindi_to_english(recognize_txt)
#                     print("\r"+ Fore.RED+"Mr.:-"+translated_tex)
#                     return translated_tex
#                 else:
#                     return ""
                
#             except sr.UnknownValueError:
#                 recognize_txt=""
#             finally:
#                 print("\r",end="",flush=True)
#             os.system("cls" if os.name=="nt" else "clear")
            
#     listen_thread=threading.Thread(target=listen)
#     print_thread=threading.Thread(target=print_loop)
#     listen_thread.start()
#     print_thread.start()
#     listen_thread.join()
#     print_thread.join()
            
            
# while True:
#     listen()



import speech_recognition as sr
import os
import threading
from mtranslate import translate
from colorama import Fore, Style, init

init(autoreset=True)

def print_loop():
    while True:
        print(Style.RESET_ALL, end="", flush=True)
        print("", end="", flush=True)

def Trans_hindi_to_english(txt):
    return translate(txt, to_language="en-in")
    

def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 33000  
    recognizer.dynamic_energy_adjustment_damping = 0.003
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.2
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.1

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.LIGHTYELLOW_EX + "Listening....", end="", flush=True)
            try:
                audio = recognizer.listen(source, timeout=None)
                recognize_txt = recognizer.recognize_google(audio, language="hi-IN").lower()
                
                if recognize_txt:
                    translated_txt = Trans_hindi_to_english(recognize_txt)
                    print("\r" + Fore.RED + "Mr.: " + translated_txt)
                    return translated_txt
                else:
                    return ""

            except sr.UnknownValueError:
                pass
                # print("\r" + Fore.YELLOW + "Could not understand audio.", flush=True)
            except sr.RequestError:
                print("\r" + Fore.RED + "API unavailable.", flush=True)
            finally:
                print("\r",end="",flush=True)
            # os.system("cls" if os.name=="nt" else "clear")

def main():
    listen_thread = threading.Thread(target=listen)
    print_thread = threading.Thread(target=print_loop, daemon=True)
    
    listen_thread.start()
    print_thread.start()
    
    listen_thread.join()
    print_thread.join()

# if __name__ == "__main__":
#     while True:
#         main()



def hearing():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 33000  # Reduced value for better recognition
    recognizer.dynamic_energy_adjustment_damping = 0.003
    recognizer.dynamic_energy_ratio = 1.5
    recognizer.pause_threshold = 0.2
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.1

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
           
            try:
                audio = recognizer.listen(source, timeout=None)
                
                recognize_txt = recognizer.recognize_google(audio, language="hi-IN").lower()
                
                if recognize_txt:
                    translated_txt = Trans_hindi_to_english(recognize_txt)
                    
                    return translated_txt
                else:
                    return ""

            except sr.UnknownValueError:
                pass
                # print("\r" + Fore.YELLOW + "Could not understand audio.", flush=True)
            except sr.RequestError:
                print("\r" + Fore.RED + "API unavailable.", flush=True)
            finally:
                print("\r",end="",flush=True)
            # os.system("cls" if os.name=="nt" else "clear")


