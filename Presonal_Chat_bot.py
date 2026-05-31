print("Welcome to your Personal Chat Bot. ")
print("You can ask me any basic questions and type bye to exit from the bot.")

import datetime
import time 

presenthour=datetime.datetime.now().hour
name=input("Enter your name. ")

if 5<= presenthour<11:
    print(f"Good morning, {name} ")
elif 11<= presenthour<=18:
    print(f"Good afternoon, {name} ")
elif 17<= presenthour <=20:
    print(f"Good evening.  {name}")
else: print(f"Good Night, {name}")

# Creating the memory of the bot
responses = {
    "hi": "Hello, I am your personal chat bot. You can ask me any question.",
    "hello": "Hi! How can I help you?",
    "how are you": "I am very fine. Thank you. How about you?",
    "who are you": "Hi, I am your personal chat bot.",
    "motivate me": "Keep going as you work on your projects.",
    "happy": "Great to hear that.",
    "can you explain what functions are in programming":
    "A function is a reusable block of code that performs a specific task."
}

def getresponseofbot(UserQuestion):
    UserQuestion = UserQuestion.lower()
    if UserQuestion in responses:
        return responses[UserQuestion]

    return "I am still in learning phase"

while True:
    userinput = input("Please ask your question: ")

    if userinput.lower() == "bye":
        print("Bot Response: Goodbye!")
        break

    reply = getresponseofbot(userinput)
    print("Bot Response:", reply)