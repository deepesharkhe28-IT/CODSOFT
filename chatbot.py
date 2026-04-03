import random
import datetime

# Bot name
bot_name = "VELORA"

# Store user name & last topic
user_name = ""
last_topic = ""

# Chatbot data
responses = {
    "greeting": {
        "keywords": ["hi", "hello", "hey", "hii", "heyy"],
        "responses": [
            "Hello! 👋",
            "Hey there! 😊",
            "Hi! How can I help you?",
            "Hello! Nice to meet you 😄",
            "Hey! What's up? 😎"
        ]
    },
    "how_are_you": {
        "keywords": ["how are you", "how are u", "how r u"],
        "responses": [
            "I'm doing great 😎",
            "All good! What about you?",
            "Feeling awesome today 🚀",
            "I'm fine! Thanks for asking 😊"
        ]
    },
    "name": {
        "keywords": ["your name", "who are you"],
        "responses": [
            "I am VELORA 🤖",
            "My name is VELORA, your smart assistant!",
            "You can call me VELORA 😄"
        ]
    },
    "creator": {
        "keywords": ["who made you", "creator", "developer"],
        "responses": [
            "I was created by a smart developer 😎",
            "My creator is working on making me smarter every day 🚀",
            "A talented programmer built me 💻"
        ]
    },
    "jokes": {
        "keywords": ["joke", "funny"],
        "responses": [
            "Why did the computer go to the doctor? Because it caught a virus 😂",
            "Why do programmers prefer dark mode? Because light attracts bugs 😆",
            "I told my computer I need a break… it froze 😅"
        ]
    },
    "study": {
        "keywords": ["study", "exam", "tips"],
        "responses": [
            "Stay consistent and take short breaks 📚",
            "Practice daily and revise regularly ✍️",
            "Focus on understanding concepts 💡"
        ]
    },
    "motivation": {
        "keywords": ["motivation", "sad", "demotivated"],
        "responses": [
            "Don't give up! You are stronger than you think 💪",
            "Success is near, keep going 🚀",
            "Believe in yourself ✨"
        ]
    },
    "hobby": {
        "keywords": ["hobby", "what do you do"],
        "responses": [
            "I love chatting with humans 🤖❤️",
            "I enjoy helping and learning new things!",
            "Talking to you is my favorite hobby 😄"
        ]
    },
    "food": {
        "keywords": ["food", "eat", "favorite food"],
        "responses": [
            "I don't eat, but I like pizza 🍕 😄",
            "Food is love! What's your favorite? 😋",
            "I hear burgers are amazing 🍔"
        ]
    },
    "thanks": {
        "keywords": ["thanks", "thank you"],
        "responses": [
            "You're welcome! 😊",
            "Anytime! 😄",
            "Glad I could help 👍"
        ]
    },
    "bye": {
        "keywords": ["bye", "exit", "quit"],
        "responses": [
            "Goodbye! 👋",
            "See you later!",
            "Take care 😊"
        ]
    }
}

# Function to respond
def get_response(user_input):
    global user_name, last_topic
    user_input = user_input.lower()

    # Name memory
    if "my name is" in user_input:
        user_name = user_input.split("my name is")[-1].strip()
        return f"Nice to meet you {user_name}! 😄"

    if "what is my name" in user_input:
        if user_name:
            return f"Your name is {user_name} 😊"
        else:
            return "I don't know your name yet 😅"

    # Time & Date
    if "time" in user_input:
        last_topic = "time"
        return "⏰ Current time: " + datetime.datetime.now().strftime("%H:%M:%S")

    if "date" in user_input:
        last_topic = "date"
        return "📅 Today's date: " + datetime.datetime.now().strftime("%d-%m-%Y")

    # Keyword matching
    for intent in responses:
        for keyword in responses[intent]["keywords"]:
            if keyword in user_input:
                last_topic = intent
                reply = random.choice(responses[intent]["responses"])

                if user_name:
                    reply += f" ({user_name})"

                return reply

    # Context reply
    if last_topic == "jokes":
        return "Want another joke? 😄"

    if last_topic == "study":
        return "Keep studying! You're doing great 📚💪"

    # Fallback
    return random.choice([
        "Hmm... I didn't understand that 🤔",
        "Can you say that differently?",
        "I'm still learning 😅 try something else!"
    ])

# Chat loop
def chatbot():
    print(f"🤖 Hello! I am {bot_name}, your AI assistant 🚀")
    print(f"{bot_name} Chatbot Started! (type 'bye' to exit)\n")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print(f"{bot_name}:", response)

        if "bye" in user_input.lower():
            break

# Run chatbot
chatbot()