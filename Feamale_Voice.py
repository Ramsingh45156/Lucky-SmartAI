import sys
import threading
import time
import pyttsx3
from textblob import TextBlob

# Emotion detection function
def detect_emotion(text):
    text_lower = text.lower()

    emotion_keywords = {
        "ecstatic": ["ecstatic"],
        "overjoyed": ["overjoyed"],
        "elated": ["elated"],
        "joyful": ["joyful"],
        "happy": ["happy"],
        "cheerful": ["cheerful"],
        "content": ["content"],
        "pleased": ["pleased"],
        "neutral": ["neutral"],
        "indifferent": ["indifferent"],
        "unhappy": ["unhappy"],
        "sad": ["sad"],
        "mournful": ["mournful"],
        "despondent": ["despondent"],
        "melancholy": ["melancholy"],
        "depressed": ["depressed"],
        "devastated": ["devastated"],
        "hopeful": ["hopeful"],
        "optimistic": ["optimistic"],
        "grateful": ["grateful"],
        "inspired": ["inspired"],
        "amused": ["amused"],
        "calm": ["calm"],
        "confused": ["confused"],
        "disappointed": ["disappointed"],
        "frustrated": ["frustrated"],
        "anxious": ["anxious"],
        "overwhelmed": ["overwhelmed"],
        "guilty": ["guilty"],
        "disgusted": ["disgusted"],
        "repulsed": ["repulsed"],
        "detached": ["detached"]
    }

    for emotion, keywords in emotion_keywords.items():
        if any(word in text_lower for word in keywords):
            return emotion
    return "unknown"

# Sentiment-based emotion classification
def get_emotion(sentiment):
    if sentiment > 0.7:
        return "ecstatic", (220, 1.5)
    elif 0.6 <= sentiment <= 0.7:
        return "overjoyed", (180, 1.4)
    elif 0.5 <= sentiment < 0.6:
        return "elated", (190, 1.3)
    elif 0.4 <= sentiment < 0.5:
        return "joyful", (180, 1.2)
    elif 0.3 <= sentiment < 0.4:
        return "happy", (170, 1.1)
    elif 0.2 <= sentiment < 0.3:
        return "cheerful", (160, 1.0)
    elif 0.1 <= sentiment < 0.2:
        return "content", (150, 0.9)
    elif -0.1 <= sentiment < 0.1:
        return "neutral", (130, 1)
    elif -0.2 <= sentiment < -0.1:
        return "unhappy", (110, 1)
    elif -0.3 <= sentiment < -0.2:
        return "sad", (100, 1)
    elif -0.4 <= sentiment < -0.3:
        return "mournful", (90, 1)
    elif -0.5 <= sentiment < -0.4:
        return "despondent", (80, 1)
    elif -0.6 <= sentiment < -0.5:
        return "melancholy", (70, 0.9)
    elif -0.7 <= sentiment < -0.6:
        return "depressed", (60, 0.8)
    elif sentiment <= -0.7:
        return "devastated", (50, 0.7)
    return "unknown", (100, 1)


def track_emotion_phrases(text):
    love_words = [
        'Love', 'Romance', 'Affection', 'Passion', 'Adoration', 'Devotion', 'Warmth', 'Amour', 'Infatuation', 
        'Desire', 'Attraction', 'Yearning', 'Admiration', 'Enchantment', 'Sweetheart', 'Heartfelt', 'Tender', 
        'Embrace', 'Cherish', 'Butterfly', 'Sweetness', 'Amorous', 'Sentiment', 'Woo', 'Serenade', 'Hug', 'Kiss', 
        'Whisper', 'Yearn', 'Lovers', 'Connection', 'Affinity', 'Magnetic', 'Attracted', 'Beloved', 'Emotion', 
        'Fond', 'Harmony', 'Sympathy', 'Infatuated', 'Enamored', 'Darling', 'Tenderly', 'Suitor', 'Heartwarming', 
        'Softness', 'Heartthrob', 'Amicable', 'Attachment', 'Honeyed', 'Admirer', 'Adore', 'Swoon', 'Entranced', 
        'Enveloped', 'Heartstrings', 'Lovestruck', 'Warmhearted', 'Companionate', 'Quixotic', 'Wooing', 'Nurturing', 
        'Stargazing', 'Whispers', 'Languishing', 'Enthralled', 'Romeo', 'Juliet', 'Emblazoned', 'Fancy', 'Allure', 
        'Rapture', 'Enraptured', 'Fantasy', 'Longing', 'Alluring', 'Savor', 'Spark', 'Enchanted', 'Elation'
    ]
    
    happy_words = [
        'Happy', 'Joyful', 'Pleased', 'Content', 'Cheerful', 'Delight', 'Euphoric', 'Merry', 'Upbeat', 'Radiant', 
        'Sunny', 'Ecstatic', 'Buoyant', 'Lighthearted', 'Vibrant', 'Carefree', 'Satisfied', 'Optimistic', 'Whimsical', 
        'Playful', 'Jubilant', 'Grateful', 'Spirited', 'Enthusiastic', 'Exhilarated', 'Blessed', 'Mirthful', 'Gleeful', 
        'Hopeful', 'Peppy', 'Zestful', 'Jocular', 'Sprightly', 'Jolly', 'Elfin', 'Blithe', 'Pleasurable', 'Chipper', 
        'Jaunty', 'Chirpy', 'Zippy'
    ]
    
    sad_words = [
        'Sad', 'Unhappy', 'Melancholy', 'Gloomy', 'Depressed', 'Downcast', 'Miserable', 'Dismal', 'Sorrowful', 'Blue',
        'Despondent', 'Heartbroken', 'Mournful', 'Weary', 'Forlorn', 'Grief-stricken', 'Woeful', 'Disheartened', 'Down',
        'Hopeless', 'Tearful', 'Lonely', 'Regretful', 'Nostalgic', 'Somber', 'Heavy-hearted', 'Dejected'
    ]
    
    angry_words = [
        'Angry', 'Furious', 'Irate', 'Wrathful', 'Resentful', 'Enraged', 'Indignant', 'Infuriated', 'Seething', 'Annoyed',
        'Aggravated', 'Outraged', 'Raging', 'Hostile', 'Fuming', 'Exasperated', 'Bitter'
    ]
    
    fear_words = [
        'Fear', 'Afraid', 'Terrified', 'Panic', 'Scared', 'Apprehensive', 'Dread', 'Uneasy', 'Tense', 'Frightened',
        'Nervous', 'Worried', 'Timid', 'Shaky', 'Hesitant'
    ]
    
    surprise_words = [
        'Surprised', 'Astonished', 'Amazed', 'Startled', 'Shocked', 'Dumbfounded', 'Flabbergasted', 'Stunned', 'Astounded',
        'Speechless', 'Wide-eyed'
    ]
    
    disgust_words = [
        'Disgusted', 'Revolted', 'Repulsed', 'Nauseated', 'Grossed out', 'Loathing', 'Aversion', 'Sickened',
        'Horrified', 'Detested'
    ]
    
    calm_words = [
        'Calm', 'Relaxed', 'Tranquil', 'Serene', 'Peaceful', 'At ease', 'Contented', 'Untroubled', 'Composed',
        'Still', 'Quiet', 'Balanced'
    ]
    
    energetic_words = [
        'Energetic', 'Lively', 'Exuberant', 'Dynamic', 'Active', 'Peppy', 'Vigorous', 'High-spirited', 'Bubbly',
        'Effervescent', 'Zesty'
    ]
    
    text_lower = text.lower()
    
    if any(word.lower() in text_lower for word in love_words):
        return "Love"
    elif any(word.lower() in text_lower for word in happy_words):
        return "Happy"
    elif any(word.lower() in text_lower for word in sad_words):
        return "Sad"
    elif any(word.lower() in text_lower for word in angry_words):
        return "Angry"
    elif any(word.lower() in text_lower for word in fear_words):
        return "Fear"
    elif any(word.lower() in text_lower for word in surprise_words):
        return "Surprise"
    elif any(word.lower() in text_lower for word in disgust_words):
        return "Disgust"
    elif any(word.lower() in text_lower for word in calm_words):
        return "Calm"
    elif any(word.lower() in text_lower for word in energetic_words):
        return "Energetic"
    else:
        return "Neutral"


# Animated text display function
def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)  # Adjust speed
    print()

# Speech function
def speakbasic(text):
    try:
        engine = pyttsx3.init()
        rate = 320  # Default speed
        engine.setProperty('rate', rate)

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[6].id)  # Select default voice

        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        emotion, (adjusted_rate, adjusted_volume) = get_emotion(sentiment)

        engine.setProperty('rate', adjusted_rate)
        engine.setProperty('volume', adjusted_volume)

        # print(f"[Detected Emotion]: {emotion}")
        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        pass

# Main Speak Function with Threads
def speak_F(text):
    speak_thread = threading.Thread(target=speakbasic, args=(text,))
    print_thread = threading.Thread(target=print_animated_message, args=(f"L.U.C.K.Y : {text}",))

    speak_thread.start()
    print_thread.start()

    speak_thread.join()
    print_thread.join()

# Test Run
# speak_F("I am very excited to assist you sir")
