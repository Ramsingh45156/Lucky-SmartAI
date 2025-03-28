from Text_to_speek import speak
from datetime import datetime
import datetime
import webbrowser
from Speech import *
from Brain import *
from Wish import wish_greeting
from Joke import get_random_joke
from welcome import *
import random
from Feamale_Voice import speak_F
from Check_online_offline import is_online
from open import open
from Random_advice import get_random_advice
import pyautogui as gui
from Model import get_response
from Battery import *
from Search_wiki import *
from Search_youtube import *
from datetime import datetime
from Check_weather import *
from Mark_voice import *

opeedlg=random.choice(open_input)

def cmd():
    greeting = wish_greeting()
    speak(f"{greeting}")
    while True:
        text=listen().lower()
        if text in wake_key_words:
            welcome=random.choice(welcome_greetings)
            speak(welcome)
        elif text in bye_keywords:
            Res_Random=random.choice(responses)
            speak(Res_Random)
        elif text.startswith(("Lucky","hello", "hello lucky", "lucky")):
            text=text.replace("Hello","")
            text=text.replace("Lucky","")
            text=text.replace("hello lucky","")
            text=text.replace("lucky","")
            text=text.strip()
            text1=mind(text)
            speak(text1)
            
        elif text.endswith(("Lucky","Hello","hello lucky", "lucky")):
            text=text.replace("Lucky","")
            text=text.replace("hello","")
            text=text.replace("hello lucky","")
            text=text.replace("lucky","")
            text=text.strip()
            text1=mind(text)
            speak(text1)
            
        elif text.startswith(("open", "kholo", "show me")):
            text=text.replace("open","")
            text=text.replace("kholo","")
            text=text.replace("show me","")
            text=text.strip()
            open(text)
        
        elif text in opeedlg:
            text=text.replace("big","")
            text=text.replace("open it","")
            text=text.replace("open karoge","")
            text=text.replace("open now","")
            text=text.replace("open please","")
            text=text.replace("open this","")
            text=text.strip()
            open(text)
        
        elif text.startswith(("Lucky","hello ", "hello lucky", "lucky")):
            response = get_response(text)
            speak(response)
            
        elif text.endswith(("Lucky", "hello", "hello lucky", "lucky")):
            response = get_response(text)
            speak(response)
            
        elif text.startswith(("what is", "who is", "what was", "What is","Who is","What this")):
            wiki_search(text)
        
        elif "check battery" in text or "check battery persent" in text or "check battery persentage" in text or "Check battery" in text or "battery" in text or "Battery" in text:
            battery_percentage()
            
        
        elif "close window" in text or "Close window" in text or "Close" in text or "remove window" in text  or "hata do" in text  or "hatao" in text  or "band karo" in text:
            gui.hotkey("alt","f4")
            random_dlg=random.choice(closedlg)
            speak(random_dlg)
        
        elif "search google" in text or "search on google" in text or "lucky search on google" in text or "goolge" in text:
            text=text.replace("search google","")
            text=text.replace("lucky search on google","")
            speak("What would you like to search on Google, Bosse?")
            search_query = listen()
            if search_query:
                speak(f"Searching for {search_query} on Google.")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
                time.sleep(2)
            else:
                None

        
        elif "music" in text or "play music" in text or "lucky play song" in text:
            speak("What music would you like to play Bosse?")
            search_query = listen()
            if search_query:
                speak(f"Playing {search_query} on YouTube.")
                video_link = get_first_youtube_link(search_query)
                if video_link:
                    webbrowser.open(video_link)
                    speak("enjoy bosse ")
                else:
                    speak("Sorry, I couldn't find the song on YouTube Bosse.")
                    time.sleep(2)
            else:
                pass
        
        
        
        elif "weather" in text or "check weather" in text or "Veder" in text or "check veder" in text:
            city = get_ip_location()
            speak(f"Getting weather report for {city}.") 
            weather, temp, feels_like = weather_forecast(city)
            if weather:
                speak(f"Also, the weather report says: {weather}.")
                speak(f"The current temperature is {temp}°C, but it feels like {feels_like}°C.")
            else:
                speak("Sorry, I couldn't fetch the weather report. Please try again.")
        
       
        elif "check ip address" in text or "IP address" in text or "tell me ip address" in text:
            x=find_my_ip()
            speak(f"Find you ip address Bosse")
            speak(f"you ip address is {x}") 
       
        elif "minimise" in text or "minimise the window" in text or "minimize karoge" in text or "minimize" in text:
            speak("Minimizing...")
            gui.hotkey("win", "down")
            gui.hotkey("win", "down")
            
        
        elif "mute" in text or "Mute" in text or "Stop the mike" in text:
            gui.press("volumemute")

        elif "write" in text or "likho" in text or "right" in text:
            speak("Writing")
            text = text.replace("write", "").replace("likho", "").replace("right", "")
            gui.write(text)
            
        elif "enter" in text or "press enter" in text or "send" in text:
            gui.press("enter")
            
        elif "select all" in text or 'select all paragraph' in text or "Select" in text:
            gui.hotkey("ctrl", "a")

        elif "copy" in text or 'copy this' in text:
            gui.hotkey("ctrl", "c")
            
        elif "paste" in text or 'paste here' in text:
            gui.hotkey("ctrl", "v")
            
        elif "undo" in text or 'undo karo' in text:
            gui.hotkey("ctrl", "z")

        elif "copy last paragraph" in text:
            gui.hotkey("ctrl", "shift", "c")

        elif "increase volume" in text or "volume badhao" in text or "increase the volume" in text:
            for _ in range(5):
                gui.press("volumeup")
            print("Volume increased.")

        elif "Decrees volume" in text or "volume kam karo" in text or "decrease the volume" in text or "Reduce volume" in text:
            for _ in range(5):
                gui.press("volumedown")
            speak("Volume decreased.")
            

        elif "full volume" in text or "full volume kr do" in text:
            for _ in range(15):
                gui.press("volumeup")
            speak("Now your system is at full volume.")
           
            
        elif "visit" in text:
            Nameofweb = text.replace("visit ", "").strip() 
            speak(f"Visiting {Nameofweb}")
            
            # Forming the URL
            Link = f"https://www.{Nameofweb}.com"
            webbrowser.open(Link)

        # Launch Website
        elif "launch" in text or "Lunch" in text:
            Nameofweb = text.replace("launch ", "").strip()  # Removed extra space
            speak(f"Launching {Nameofweb}")
            Link = f"https://www.{Nameofweb}.com"
            webbrowser.open(Link)     
        
        elif "scroll up" in text or "Do it" in text or "And up" in text or "do it" in text:
            gui.scroll(500)  # Positive value scrolls up

        # Scroll Down
        elif "scroll down" in text or "Do down" in text or "And down" in text:
            gui.scroll(-500)  # Negative value scrolls down

        # Play, Pause, Stop (using Spacebar)
        elif "play" in text or "pause" in text or "stop" in text:
            gui.press("space")

        # Search Functionality
        elif text.startswith("search"):
            gui.hotkey("/")  # Open search bar if applicable
            text = text.replace("search", "").strip()
            
            gui.write(text)
            time.sleep(3)
            gui.press("enter")
            
            speak(f"Searching {text}")
                  
               
        
        elif "maximize window" in text:
            speak("Maximizing Window.")
            gui.hotkey("win", "up")

        # 10. Restore Window
        elif "restore window" in text:
            speak("Restoring Window.")
            gui.hotkey("win", "shift", "up")

        # 11. Switch Window (Next)
        elif "switch window" in text or "next window" in text or "Witch next window" in text or "Witch window" in text or "Next window" in text:
            speak("Switching to Next Window.")
            gui.hotkey("alt", "tab")

        # 12. Switch to Previous Window
        elif "previous window" in text or "back window" in text or "back window" in text or "TVS window" in text:
            speak("Switching to Previous Window.")
            gui.hotkey("alt", "shift", "tab")

        # 13. Open Incognito / Private Window
        elif "private window" in text:
            speak("Opening Incognito Window.")
            gui.hotkey("ctrl", "shift", "n")

        # 14. Bookmark Page
        elif "bookmark page" in text or "save page" in text:
            speak("Bookmarking Page.")
            gui.hotkey("ctrl", "d")

        # 15. Open Browsing History
        elif "history" in text or "browse history" in text or "view history" in text:
            speak("Opening Browsing History.")
            gui.hotkey("ctrl", "h")

        # 16. Open Downloads
        elif "download" in text or "download history" in text or "Download history" in text:
            speak("Opening Downloads History.")
            gui.hotkey("ctrl", "j")

        # 17. Open Developer Tools (Inspect Element)
        elif "inspect element" in text or "open developer tools" in text:
            speak("Opening Developer Tools.")
            gui.hotkey("ctrl", "shift", "i")

        # 18. Clear Cookies / Browsing Data
        elif "clear cookies" in text or "delete cookies" in text or "clear browsing data" in text or "clear history" in text:
            speak("Clearing Browsing Data.")
            gui.hotkey("ctrl", "shift", "del")

        # 19. Enter Fullscreen
        elif "fullscreen" in text or "full screen" in text:
            speak("Entering Fullscreen Mode.")
            gui.hotkey("f11")

        # 20. Toggle Dark Mode
        elif "toggle dark mode" in text or "dark theme" in text or "Dark modes" in text or "Dark Mod" in text:
            speak("Toggling Dark Mode.")
            gui.hotkey("ctrl", "shift", "e")

        # 21. Mute / Unmute Tab
        elif "mute tab" in text:
            speak("Muting Tab.")
            gui.hotkey("ctrl", "m")

        elif "unmute" in text or "unmute tab" in text:
            speak("Unmuting Tab.")
            gui.hotkey("ctrl", "shift", "m")

        # 22. Open Extensions
        elif "manage extension" in text or "Manage Extension" in text:
            speak("Opening Extensions.")
            gui.hotkey("ctrl", "shift", "a")

        # 23. Open Browser Settings
        elif "browser setting" in text or "Browser setting" in text:
            speak("Opening Settings.")
            gui.hotkey("ctrl", ",")

        # 24. Save Page As
        elif "save as page" in text or "save as" in text or "Save save" in text:
            speak("Saving Page As.")
            gui.hotkey("ctrl", "s")

        # 25. Print Page
        elif "print page" in text or "print" in text:
            speak("Printing Page.")
            gui.hotkey("ctrl", "p")

        # 26. Open Bookmarks
        elif "view bookmark" in text:
            speak("Opening Bookmarks.")
            gui.hotkey("ctrl", "b")                    
        
        elif "go back" in text or "back" in text:
            speak("Going Back.")
            gui.hotkey("alt", "left")

        # 43. Go Forward
        elif "go forward" in text or "forward" in text:
            speak("Going Forward.")
            gui.hotkey("alt", "right")

        # 44. Stop Page Load
        elif "stop loading" in text or "stop" in text:
            speak("Stopping Page Load.")
            gui.press("esc")

        # 45. Scroll Up
        elif "scroll up" in text or "scroll page up" in text:
            speak("Scrolling Up.")
            gui.scroll(3)

        # 46. Scroll Down
        elif "scroll down" in text or "scroll page down" in text:
            speak("Scrolling Down.")
            gui.scroll(-3)

        # 47. Scroll to Top
        elif "scroll to top" in text:
            speak("Scrolling to Top.")
            gui.press("home")

        # 48. Scroll to Bottom
        elif "scroll to bottom" in text:
            speak("Scrolling to Bottom.")
            gui.press("end")

        # 49. Open New Tab
        elif "then" in text or "new tab" in text or "New then" in text:
            speak("Opening New Tab.")
            gui.hotkey("ctrl", "t")

        # 50. Reopen Closed Tab
        elif "reopen closed then" in text or "restore closed tab" in text:
            speak("Reopening Closed Tab.")
            gui.hotkey("ctrl", "shift", "t")

        # 51. Switch to a Specific Tab (Dynamic Tab Switching)
        elif "switch to tab" in text or "go to tab" in text:
            tab_number = ''.join(filter(str.isdigit, text))  # Extract number from text
            if tab_number:
                speak(f"Switching to Tab {tab_number}.")
                gui.hotkey("ctrl", tab_number)
            else:
                speak("Please specify a tab number.")
        elif "show desktop" in text or "hide windows" in text:
            speak("Showing Desktop.")
            gui.hotkey("win", "m")

        # 60. Open Task View
        elif "open task view" in text or "view tasks" in text:
            speak("Opening Task View.")
            gui.hotkey("win", "tab")    
        
        # 61. Switch Virtual Desktop
        elif "switch virtual desktop" in text or "change desktop" in text or " Witch virtual desktop" in text:
            speak("Switching Virtual Desktop.")
            gui.hotkey("ctrl", "win", "right")

        # 62. Open Notification Center
        elif "open notification center" in text or "show notifications" in text:
            speak("Opening Notification Center.")
            gui.hotkey("win", "a")

        # 63. Show Action Center
        elif "show action center" in text or "show action menu" in text:
            speak("Showing Action Center.")
            gui.hotkey("win", "a")

        # 64. Lock Screen / Switch User
        elif "lock screen" in text or "lock computer" in text or "switch user" in text or "change user" in text:
            speak("Locking Screen.")
            gui.hotkey("win", "l")

        # 66. Log Off / Sign Out
        elif "log off" in text or "sign out" in text:
            speak("Logging Off.")
            gui.hotkey("ctrl", "alt", "del")

        # 67. Shutdown Computer
        elif "shutdown" in text or "turn off computer" in text or "shut down" in text or "Shutdown computer" in text:
            speak("Shutting Down.")
            gui.hotkey("win", "d")
            time.sleep(0.5)
            gui.hotkey("alt", "f4")
            time.sleep(0.5)
            gui.press("enter")
            
        elif "restart" in text or "reboot" in text:
            speak("Restarting.")
            gui.hotkey("win", "d")
            time.sleep(0.5)
            gui.hotkey("alt", "f4")
            time.sleep(0.5)
            gui.hotkey("alt", "Down")
            time.sleep(0.5)
            gui.press("enter")

        

        # 69. Put Computer to Sleep
        elif "sleep" in text or "computer sleep" in text or "Laptop slip" in text:
            speak("Putting Computer to Sleep.")
            gui.hotkey("win", "d")
            time.sleep(0.5)
            gui.hotkey("alt", "f4")
            time.sleep(0.5)
            gui.hotkey("alt", "Up")
            time.sleep(0.5)
            gui.press("enter")

        elif "navigate forward" in text or "forward jao" in text:
            speak("Navigating forward to the next page.")
            gui.hotkey("alt", "right")

        elif "zoom in on the current page" in text or "current page me zoom in" in text:
            speak("Zooming in on the current page.")
            gui.hotkey("ctrl", "+")
            
        elif "zoom out on the current page" in text or "current page me zoom out" in text or "zoom" in text:
            speak("Zooming out on the current page.")
            gui.hotkey("ctrl", "-")

        elif "reset the zoom level" in text or "zoom reset karo" in text:
            speak("Resetting the zoom level to default.")
            gui.hotkey("ctrl", "0")

        
        elif "time batao" in text or "time" in text or "Tell me time" in text:
            now_time = datetime.now().strftime("%H:%M:%S")
            speak(str(now_time))

        elif "date batao" in text or "date" in text:
            now_time =datetime.now().strftime("%d:%m:%Y")
            speak(str(now_time))
        
        
        
        elif text in qa_dict:
            ans = qa_dict[text]
            speak_thread = threading.Thread(target=speak, args=(ans,))
            speak_thread.start()
            speak_thread.join()
                
        else:
            pass
                
                
def advice():
    while True:
        x=[625,754,695,934,967,887,495,823,844,898,756,672,611] 
        x1=random.choice(x)
        time.sleep(x1)
        speak("I have some suggestion for you, boss")
        text=listen().lower()
        if "yes tell me" in text or "yes" in text or "Just tell me" in text or "Tell":
            advice = get_random_advice()
            speak(advice)
        
        else:
            speak("no probelm boss,i think you need some advice so i give")
            

def RandomJok():
    while True:
        x=[615,154,295,334,367,387,595,323,644,198,356,672,611] 
        x1=random.choice(x)
        time.sleep(x1)
        speak("I have some joke for you, boss")
        text=listen().lower()
        if "yes tell me" in text or "yes" in text or "Just tell me" in text:
            RandomJok = get_random_joke()
            speak(RandomJok)
        
        else:
            speak("no probelm boss,I just want to include some entertanment in your day")

           
def Lucky():
    t1=threading.Thread(target=cmd)
    t2=threading.Thread(target=advice)
    t3=threading.Thread(target=battery_alert)
    t4=threading.Thread(target=check_plugin_status)
    t5=threading.Thread(target=RandomJok)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()



        
def check_lucky(): 
    if is_online():
        online_dlg=random.choice(onlineDLG)
        speak_M(online_dlg)
        Lucky()
        
    else:
        offline_dlg=random.choice(offlineDLG)
        speak_F(offline_dlg)
        
# check_lucky()




def mainFun():
    call_me_dlg=random.choice(call_me)
    speak_M(call_me_dlg)
    while True:
        text=hearing().lower()
        if "Lucky" in text or "hello lucky" in text or "Hello lucky" in text or "Lucky utho" in text or "lucky" in text:
            check_lucky()
        else:
            pass
        
    

mainFun()
