# Importing time module to show current time
import time


# Welcome message
print("=" * 50)
print("🤖 Hello! I am DecodeBot")
print("🤖 Your Friendly AI Chatbot")
print("💬 Type 'help' to see commands")
print("❌ Type 'bye' to exit")
print("=" * 50)


# Infinite loop so chatbot keeps running
while True:

    # Taking input from user
    # .lower() converts text to lowercase
    # .strip() removes extra spaces
    user = input("\nYou: ").lower().strip()

    # Greeting responses
    if user in ["hello", "hi", "hey", "good morning", "good evening"]:
        print("Bot: Hey there! 😊 How are you doing today?")

    # Asking about chatbot health
    elif user == "how are you":
        print("Bot: I'm doing great and ready to chat with you! 😄")

    # Asking chatbot name
    elif user in ["what is your name", "who are you"]:
        print("Bot: My name is DecodeBot, your virtual assistant 🤖")

    # Asking creator
    elif user == "who created you":
        print("Bot: I was created by a talented Python developer named as Rao 🚀")

    # Asking chatbot abilities
    elif user == "what can you do":
        print("Bot: I can chat with you, tell the time, and answer simple questions!")

    # Time feature
    elif user == "time":

        # Getting current system time
        current_time = time.strftime("%I:%M:%S %p")

        print(f"Bot: The current time is {current_time} ⏰")

    # Date feature
    elif user == "date":

        # Getting current system date
        current_date = time.strftime("%d-%m-%Y")

        print(f"Bot: Today's date is {current_date} 📅")

    # Motivational response
    elif user == "motivate me":
        print("Bot: Believe in yourself! Every expert was once a beginner 💪")

    # Joke feature
    elif user == "tell me a joke":
        print("Bot: Why do programmers prefer dark mode? 😅")
        print("Bot: Because light attracts bugs!")

    # Help menu
    elif user == "help":

        print("\n📌 Available Commands:")
        print("------------------------------------------------")
        print("hello / hi              -> Greeting")
        print("how are you             -> Ask chatbot status")
        print("what is your name       -> Know chatbot name")
        print("who created you         -> Creator info")
        print("what can you do         -> Features")
        print("time                    -> Current time")
        print("date                    -> Current date")
        print("motivate me             -> Motivation")
        print("tell me a joke          -> Funny joke")
        print("bye                     -> Exit chatbot")
        print("------------------------------------------------")

    # Exit condition
    elif user == "bye":
        print("Bot: Goodbye! 😊 Have an amazing day ahead.")
        break

    # Empty input handling
    elif user == "":
        print("Bot: You didn't type anything 😅")

    # Default response for unknown commands
    else:
        print("Bot: Hmm... I don't understand that yet 🤔")
        print("Bot: Type 'help' to see what I can do.")