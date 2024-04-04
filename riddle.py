from random import*

answers=["8","water","oxygen"]
questions=["how many planets there are in the solar system?","what is all around you but you can't see it?","what is white, sometimes blue, and it is transparent?"]

question=None
answer=choice(answers)

if answer=="8":
    question=questions[0]

if answer=="water":
    question=questions[2]

if answer=="oxygen":
    question=questions[1]
thing=input(f"enter the answer to this question: {question} ")

if thing==answer:
    print("correct!")
else:
    print("incorrect!")
