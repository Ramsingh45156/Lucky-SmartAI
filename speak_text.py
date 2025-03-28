import asyncio
import threading
import os
import edge_tts 
import pygame
import sys
import time
import psutil
from colorama import Fore,Style,init

init()
# VOICE = "en-AU-WilliamNeural"
VOICE = "hi-IN-MadhurNeural"
# VOICE = "hi-IN-SwaraNeural"
# VOICE = "en-IN-NeerjaNeural"
# VOICE = "en-IN-PrabhatNeural"
SPEECH_RATE = "+30%"
BUFFER_SIZE = 1024

def print_animated_message(message, color=Fore.LIGHTGREEN_EX, speed=0.031):
    """Even faster text animation"""
    for char in message:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(speed)
    print()


def check_file_lock(file_path):
    for proc in psutil.process_iter(['pid', 'name', 'open_files']):
        try:
            if proc.info['open_files']:  # Some processes may not have open_files attribute
                for file in proc.info['open_files']:
                    if file.path == file_path:
                        print(f"Process {proc.info['name']} (PID: {proc.info['pid']}) is using the file.")
                        return proc.info['pid']
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return None


def wait_until_file_free(file_path, timeout=5):
    """Waits until the file is free to delete."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        if not check_file_lock(file_path):
            return True
        time.sleep(0.5)  # Wait a bit before retrying
    return False


def remove_file(file_path):
    time.sleep(1)  # Ensure file is not in use
    attempts = 0
    while attempts < 5:  # Try max 5 times
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                # print(f"✅ Deleted file: {file_path}")
            return  # Exit function after success
        except PermissionError:
            pass
            # print(f"File is locked, retrying... ({attempts+1}/5)")
            time.sleep(1)  # Wait before retrying
        except Exception as e:
            # print(f"Error deleting file: {e}")
            pass  # Exit loop for unknown errors
        attempts += 1
            

async def amain(TEXT, output_file) -> None:
    try:
        cm_txt = edge_tts.Communicate(TEXT, VOICE, rate=SPEECH_RATE)  # Fixed class instantiation
        await cm_txt.save(output_file)
        thread = threading.Thread(target=play_audio, args=(output_file,))
        thread.start()
    except asyncio.TimeoutError:
        print("Connection timeout. Retrying...")
        await asyncio.sleep(5) 
        await amain(TEXT, output_file)  
    except Exception as e:
        # print(f"Error in TTS processing: {e}")
        pass

def play_audio(file_path):
    try:
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.delay(100)
        sound.stop()
        del sound  # Ensure pygame releases the file
        pygame.mixer.quit()
        time.sleep(1)
        remove_file(file_path)
    except Exception as e:
        # print(f"Error playing audio: {e}")
        pass

def speak1(TEXT, output_file=None):
    if output_file is None:
        output_file = os.path.join(os.getcwd(), "output.mp3")  # Proper file path
    asyncio.run(amain(TEXT, output_file))


def speak(text):
    t1=threading.Thread(target=speak1,args=(text,))
    t2=threading.Thread(target=print_animated_message,args=(text,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    
    
    



# # Test the speak function
# speak("Hello sir, I am Lucky! AI stands for Artificial Intelligence, which refers to the simulation of human intelligence in machines that are programmed to think and learn like humans.")

# speak("namaste sar, main lakee hoon! ai ka matalab aartiphishiyal intelijens hai, jo masheenon mein maanav buddhi ke anukaran ko sandarbhit karata hai jinhen manushyon kee tarah sochane aur seekhane ke lie prograam kiya jaata hai.")

# speak("नमस्ते सर, मैं लकी हूँ! AI का मतलब आर्टिफिशियल इंटेलिजेंस है, जो मशीनों में मानव बुद्धि के अनुकरण को संदर्भित करता है जिन्हें मनुष्यों की तरह सोचने और सीखने के लिए प्रोग्राम किया जाता है।")

# speak("नमस्ते सर, हम लकी बनी! AI के मतलब आर्टिफिशियल इंटेलिजेंस हवे, जे मशीन में मनुष्य के बुद्धि जइसन सोच-सझ के क्षमता देला, ताकि ऊ मनुष्य जइसन सीखे आ समझे सके।")