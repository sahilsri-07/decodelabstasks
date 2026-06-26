from datetime import datetime
import random

responses = {
    "hello": [
        "Hello! 👋",
        "Hi there! 😊",
        "Hey! Nice to meet you!"
    ],
    "hi": [
        "Hello! 👋",
        "Hi! How can I help you today?",
        "Hey!"
    ],
    "hey": [
        "Hey! 😊",
        "Hello there!",
        "Hi!"
    ],
    "good morning": [
        "Good Morning! ☀️ Have a productive day!"
    ],
    "good afternoon": [
        "Good Afternoon! 😊"
    ],
    "good evening": [
        "Good Evening! 🌇"
    ],
    "good night": [
        "Good Night! 🌙 Sleep well!"
    ],
    "how are you": [
        "I'm doing great! Thanks for asking.",
        "I'm always ready to help!"
    ],
    "what is your name": [
        "My name is DecodeBot.",
        "I'm DecodeBot, your AI assistant."
    ],
    "who are you": [
        "I'm a Rule-Based AI Chatbot built using Python."
    ],
    "who made you": [
        "I was developed by Sahil Srivastava."
    ],
    "who created you": [
        "I was created as part of DecodeLabs Project 1."
    ],
    "are you human": [
        "No, I'm a Python chatbot."
    ],
    "what are you doing": [
        "Waiting for your next question."
    ],
    "what is ai": [
        "AI stands for Artificial Intelligence."
    ],
    "what is machine learning": [
        "Machine Learning allows computers to learn from data."
    ],
    "what is deep learning": [
        "Deep Learning is a subset of Machine Learning."
    ],
    "what is python": [
        "Python is a popular programming language for AI."
    ],
    "what is chatbot": [
        "A chatbot is a program that talks with users."
    ],
    "what is coding": [
        "Coding means writing instructions for computers."
    ],
    "what is algorithm": [
        "An algorithm is a step-by-step solution to a problem."
    ],
    "what is data structure": [
        "A data structure organizes data efficiently."
    ],
    "motivate me": [
        "Keep learning. Small progress every day creates big results.",
        "Success comes from consistency.",
        "Believe in yourself. You can do it!"
    ],
    "tell me a joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did Python go to school? To improve its class!",
        "Why was the computer cold? It forgot to close Windows!"
    ],
    "capital of india": [
        "New Delhi is the capital of India."
    ],
    "capital of france": [
        "Paris is the capital of France."
    ],
    "largest planet": [
        "Jupiter is the largest planet in our Solar System."
    ],
    "fastest animal": [
        "The Peregrine Falcon is the fastest animal."
    ],
    "i am happy": [
        "That's wonderful! 😊"
    ],
    "i am sad": [
        "I'm sorry to hear that. I hope things get better soon."
    ],
    "i love coding": [
        "That's awesome! Keep building projects."
    ],
    "thank you": [
        "You're welcome!"
    ],
    "thanks": [
        "Happy to help!"
    ],
    "bye": [
        "Goodbye! 👋",
        "See you soon!",
        "Take care!"
    ]
}

print("=" * 60)
print("🤖 WELCOME TO DECODEBOT")
print("=" * 60)
print("Type 'help' for available commands.")
print("Type 'exit' to quit.")
print("=" * 60)

while True:

    user_input = input("\nYou : ").lower().strip()

    if user_input == "exit":
        print("Bot :", random.choice(responses["bye"]))
        break

    elif user_input == "help":
        print("""
Available Commands

Greetings
- hello
- hi
- hey

Bot
- who are you
- what is your name
- who made you

AI
- what is ai
- what is machine learning
- what is deep learning

Programming
- what is python
- what is coding
- what is algorithm
- what is data structure

Fun
- tell me a joke
- motivate me

Knowledge
- capital of india
- capital of france
- largest planet
- fastest animal

Utility
- time
- date
- calculate 25+50

Exit
- exit
""")

    elif user_input == "time":
        print("Bot :", datetime.now().strftime("%I:%M:%S %p"))

    elif user_input == "date":
        print("Bot :", datetime.now().strftime("%d-%m-%Y"))

    elif user_input.startswith("calculate "):
        expression = user_input.replace("calculate", "").strip()

        try:
            result = eval(expression)
            print("Bot :", result)
        except:
            print("Bot : Invalid expression.")

    elif user_input in responses:
        print("Bot :", random.choice(responses[user_input]))

    else:
        print("Bot : Sorry, I don't understand that.")
        print("Bot : Type 'help' to see available commands.")