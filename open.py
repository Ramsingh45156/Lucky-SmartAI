import pyautogui as ui
import time
from Text_to_speek import speak
from welcome import *
import random    
import webbrowser
import difflib 
from Speech import listen

# random_dlg=random.choice(websites)






def App_open(text):
    text=text.replace("open","")
    text=text.strip()
    random_dlg=random.choice(open_dld)
    speak(f"{random_dlg} {text}")
    ui.press("win")
    time.sleep(0.5)
    ui.write(text)
    time.sleep(0.5)
    ui.press("enter")
    random_dlg4=random.choice(success_responses)
    speak(random_dlg4)

def open_website_by_name(text):
    
    website_name_lower = text.lower()

    # Check if the exact website name exists in the dictionary
    if website_name_lower in websites:
        url = websites[website_name_lower]
        random_dlg=random.choice(open_dld)
        speak(random_dlg + " " +text)
        webbrowser.open(url)
        # speak(random_dlg4)
    else:
        # Find the closest matching website using string similarity
        matches = difflib.get_close_matches(website_name_lower, websites.keys())

        if matches:
            closest_match = matches[0]
            random_dlg2=random.choice(open_attempts_DLG)
            random_dlg=random.choice(open_dld)
            speak(f"{text} {random_dlg2} {random_dlg}")
            url = websites[closest_match]
            webbrowser.open(url)
            random_dlg4=random.choice(success_responses)
            speak(random_dlg4)
        else:
            random_dlg3=random.choice(not_responding)
            speak(text + " " + str(random_dlg3))
def open(text):
    text = text.lower()
    if "website" in text or "site" in text or "open web" in text or "open website" in text:
        text=text.replace("website","")
        text=text.replace("site","")
        text=text.replace("open web","")
        text=text.replace("open website","")
        text=text.strip()
        open_website_by_name(text)
        
        
    elif "application" in text or "app" in text or "open" in text or "open window" in text:
        text=text.replace("application","")
        text=text.replace("app","")
        text=text.replace("open","")
        text=text.replace("open window","")
        text=text.strip()
        App_open(text)
        
    else:
        text=text.replace("open","")
        text=text.strip()
        App_open(text)
        
        
        
        
        
    

# if __name__ == "__main__":
#     while True:
    
#         text = listen()
#         open(text)

    
# import pyautogui as ui
# import time
# from Text_to_speek import speak  # Assuming this module exists and works for text-to-speech
# from welcome import *  # Ensure this module exists with open_dld, open_attempts_DLG, etc.
# import random    
# import webbrowser
# import difflib 
# from Speech import listen  # Assuming this module exists and works for speech recognition

# # Dummy data for your speech responses and websites (replace with actual content)
# open_dld = ["Opening", "Launching"]
# open_attempts_DLG = ["Attempting to open", "Trying to open"]
# not_responding = ["Could not find", "No match found for"]
# success_responses = ["Successfully opened", "Here you go"]

# # Dictionary of websites (add your own)
# websites = {
#     "google": "https://www.google.com",
#     "youtube": "https://www.youtube.com",
#     "facebook": "https://www.facebook.com",
#     # Add more websites as needed
# }

# # Random selection from dialogues
# random_dlg = random.choice(open_dld)
# random_dlg2 = random.choice(open_attempts_DLG)
# random_dlg3 = random.choice(not_responding)
# random_dlg4 = random.choice(success_responses)

# # Function to open an application
# def App_open(text):
#     text = text.replace("open", "").strip()  # Clean up the input text
#     speak(f"{random_dlg} {text}")
#     ui.press("win")  # Press 'win' key to open the Start menu
#     time.sleep(0.5)
#     ui.write(text)  # Type the name of the application
#     time.sleep(0.5)
#     ui.press("enter")  # Press 'enter' to open the app
#     speak(random_dlg4)

# # Function to open a website by name
# def open_website_by_name(text):
#     website_name_lower = text.lower()

#     # Check if the exact website name exists in the dictionary
#     if website_name_lower in websites:
#         url = websites[website_name_lower]
#         speak(f"{random_dlg} {text}")
#         webbrowser.open(url)  # Open the website
#         speak(random_dlg4)
#     else:
#         # Find the closest matching website using string similarity
#         matches = difflib.get_close_matches(website_name_lower, websites.keys())
#         if matches:
#             closest_match = matches[0]
#             url = websites[closest_match]
#             speak(f"{text} {random_dlg2} {random_dlg}")
#             webbrowser.open(url)
#             speak(random_dlg4)
#         else:
#             speak(f"{text} {random_dlg3}")

# # Main function to process commands
# def open(text):
#     text = text.lower()  # Convert input to lowercase for easier matching
#     if "website" in text or "site" in text or "open web" in text or "open website" in text:
#         text = text.replace("website", "").replace("site", "").replace("open web", "").replace("open website", "").strip()
#         open_website_by_name(text)
#     elif "application" in text or "app" in text or "open" in text or "open window" in text:
#         text = text.replace("application", "").replace("app", "").replace("open", "").replace("open window", "").strip()
#         App_open(text)
#     else:
#         speak("Sorry, I didn't understand the command.")

# # Main loop to continuously listen for speech input
# if __name__ == "__main__":
#     while True:
#         text = listen()  # Listen to the user's command
#         open(text)  # Process the command


# import pyautogui as ui
# import time
# from Text_to_speek import speak  # Assuming this module exists and works for text-to-speech
# from welcome import *  # Importing your `welcome.py` file with dialogue and website data
# import random    
# import webbrowser
# import difflib 
# from Speech import listen  # Assuming this module exists and works for speech recognition

# # Random selection from your dialogues in welcome.py
# random_dlg = random.choice(open_dld)
# random_dlg2 = random.choice(open_attempts_DLG)
# random_dlg3 = random.choice(not_responding)
# random_dlg4 = random.choice(success_responses)

# # Function to open an application
# def App_open(text):
#     text = text.replace("open", "").strip()  # Clean up the input text
#     speak(f"{random_dlg} {text}")
#     ui.press("win")  # Press 'win' key to open the Start menu
#     time.sleep(0.5)
#     ui.write(text)  # Type the name of the application
#     time.sleep(0.5)
#     ui.press("enter")  # Press 'enter' to open the app
#     speak(random_dlg4)

# # Function to open a website by name
# def open_website_by_name(text):
#     website_name_lower = text.lower()

#     # Check if the exact website name exists in the dictionary (from welcome.py)
#     if website_name_lower in websites:
#         url = websites[website_name_lower]
#         speak(f"{random_dlg} {text}")
#         webbrowser.open(url)  # Open the website
#         speak(random_dlg4)
#     else:
#         # Find the closest matching website using string similarity
#         matches = difflib.get_close_matches(website_name_lower, websites.keys())
#         if matches:
#             closest_match = matches[0]
#             url = websites[closest_match]
#             speak(f"{text} {random_dlg2} {random_dlg}")
#             webbrowser.open(url)
#             speak(random_dlg4)
#         else:
#             speak(f"{text} {random_dlg3}")

# # Main function to process commands
# def open(text):
#     text = text.lower()  # Convert input to lowercase for easier matching
#     if "website" in text or "site" in text or "open web" in text or "open website" in text:
#         text = text.replace("website", "").replace("site", "").replace("open web", "").replace("open website", "").strip()
#         open_website_by_name(text)
#     elif "application" in text or "app" in text or "open" in text or "open window" in text:
#         text = text.replace("application", "").replace("app", "").replace("open", "").replace("open window", "").strip()
#         App_open(text)
#     else:
#         speak("Sorry, I didn't understand the command.")

# # Main loop to continuously listen for speech input
# if __name__ == "__main__":
#     while True:
#         text = listen()  # Listen to the user's command
#         open(text)  # Process the command
