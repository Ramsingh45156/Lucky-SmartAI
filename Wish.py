import datetime
import random
from Text_to_speek import speak

# Current Date and Time
Today = datetime.date.today()
formatted_date = Today.strftime("%d %b %y")
Now = datetime.datetime.now()

def wish_greeting():
    current_hour = Now.hour

    if current_hour < 12:
        greetings = [
            "Good Morning, Boss! How can I assist you today?",
            "Morning, Boss! What can I do for you?",
            "Good day, Boss! Need any help this morning?",
            "Hi there, Boss! Wishing you a great start to the day!",
            "Rise and shine, Boss! What can I help you with today?",
            "Morning, Boss! How can I make your day better?",
            "Good morning, Boss! Anything important on the agenda?",
            "Hello, Boss! It’s a fresh new morning, what’s the plan?",
            "Wakey wakey, Boss! Let’s make today productive.",
            "Good morning, Boss! What’s the first task of the day?",
            "Rise and shine, Boss! I’m ready to assist you.",
            "Morning, Boss! Ready to conquer the day?",
            "Good morning, Boss! I hope your coffee is strong!",
            "Good morning, Boss! A new day, a new opportunity!",
            "Hello, Boss! What’s the game plan for today?",
            "Boss! It’s morning, let’s get things rolling!",
            "Top of the morning to you, Boss! Let’s do this!",
            "Good morning, Boss! How’s the energy today?",
            "Hello, Boss! Hope you had a restful sleep.",
            "Good morning, Boss! Let’s make today amazing!"
        ]
    elif 12 <= current_hour < 18:
        greetings = [
            "Good Afternoon, Boss! How's your day going?",
            "Hello, Boss! What can I do for you this afternoon?",
            "Good afternoon, Boss! Need help with anything?",
            "Hey there, Boss! How’s your afternoon treating you?",
            "Good afternoon, Boss! How can I assist you today?",
            "Hi, Boss! Hope your afternoon is going well.",
            "Good day, Boss! How can I help you?",
            "Afternoon, Boss! What’s on the agenda?",
            "Hello, Boss! Need anything for the rest of the day?",
            "Good afternoon, Boss! Let’s finish strong!",
            "Boss, how’s everything going this afternoon?",
            "Hope you’re having a smooth day, Boss!",
            "Afternoon, Boss! Want to check something?",
            "Good afternoon, Boss! The grind continues!",
            "Boss! Another great afternoon ahead!",
            "Hey Boss! Hope you’re feeling great today!",
            "Good afternoon, Boss! Let’s get things done!",
            "Boss, ready for the second half of the day?",
            "Hello, Boss! Here to make your afternoon smoother!",
            "Hey Boss! Got any exciting plans for later?",
        ]
    elif 18 <= current_hour < 22:
        greetings = [
            "Good Evening, Boss! How can I assist you tonight?",
            "Evening, Boss! How's it going?",
            "Good evening, Boss! Need any help tonight?",
            "Hello Boss! How’s your evening been?",
            "Good evening, Boss! Ready to relax or need something?",
            "Evening, Boss! What can I do for you tonight?",
            "Hi Boss! How's your evening going so far?",
            "Good evening, Boss! How can I help make your night easier?",
            "Evening greetings, Boss! What’s on your mind?",
            "Hello Boss! How’s your evening unfolding?",
            "Boss, evening time! What’s the plan now?",
            "Good evening, Boss! Work done or more tasks ahead?",
            "Hi Boss! Winding down for the night or still working?",
            "Evening vibes, Boss! How may I assist?",
            "Hey Boss! Need anything before calling it a day?",
            "Good evening, Boss! Let’s wrap up the day smoothly!",
            "Boss, the stars are out! Need help before bed?",
            "Hello Boss! Night is young, anything I can do?",
            "Evening, Boss! Wrapping up work or still hustling?",
            "Good evening, Boss! Anything urgent before the night ends?"
        ]
    else:
        greetings = [
            "Good Night, Boss! Time to rest and recharge!",
            "Night, Boss! Sweet dreams and a fresh start tomorrow!",
            "Good night, Boss! Let me know if you need anything!",
            "Hello Boss! Sleep well and wake up refreshed!",
            "Good night, Boss! Have a peaceful and relaxing sleep!",
            "Nighty night, Boss! See you bright and early!",
            "Boss, time to call it a day! Sleep well!",
            "Good night, Boss! Rest up for a great tomorrow!",
            "Boss, logging off? Have a restful night!",
            "Night, Boss! Sweet dreams and a productive tomorrow!",
            "Sleep tight, Boss! Let’s crush it again tomorrow!",
            "Good night, Boss! Don’t forget to relax!",
            "Rest well, Boss! A new day is waiting for you!",
            "Boss, it’s time to power down! Sleep well!",
            "Good night, Boss! Hope you had a great day!",
            "Boss, you deserve some rest! Sleep peacefully!",
            "Sweet dreams, Boss! Ready for another big day ahead?",
            "Night vibes, Boss! Time to relax and recharge!",
            "Good night, Boss! Let’s make tomorrow even better!",
            "Boss, the night is calm! Sleep well and stay strong!"
        ]
    
    return random.choice(greetings)

# # # Example usage
# greeting = wish_greeting()
# speak(f"Lucky says: {greeting}")
