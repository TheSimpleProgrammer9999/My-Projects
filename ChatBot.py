# A simple chat bot

import random as rd

running = True
ideas = ["Learn coding", "Play outdoors", "Read a book", "Learn electronics", "(If you're a programmer)make a simple FPS game", "(If you have free time)play with Lego"]
ideaNum = None

while running:
    user = input("Type something: ");
    if (("hello" in user.lower()) or ("hi" in user.lower())):
        print("Hello user!")
        
    if ("bye" in user.lower()):
        print("bye!");
        running = False
        
    if (("what is your name" in user.lower()) or ("who are you" in user.lower())):
        print("I'm a chatbot named Simple C. Bot")
    
    if (("give me ideas" in user.lower()) or ("what to do" in user.lower()) or ("ideas" in user.lower())):
        # chooses a random number between one and six
        randNum = rd.randint(1, 6)
        if randNum == 1:
            ideaNum = 0
        elif randNum == 2:
            ideaNum = 1
        elif randNum == 3:
            ideaNum = 2
        elif randNum == 4:
            ideaNum = 3
        elif randNum == 5:
            ideaNum = 4
        elif randNum == 6:
            ideaNum = 5

        idea = ideas[ideaNum]
        print("Here is an idea(it might not be that good):\n", idea)

    if (("thanks" in user.lower()) or ("thank you" in user.lower())):
        print("You're welcome!")
        
        
