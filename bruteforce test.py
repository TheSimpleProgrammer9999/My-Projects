list_=[]
from time import sleep
counter= -1
try:
    while True:
        thing=input("enter a password: ")
        thing_=list(thing)
        for i in range(len(thing_)):
            sleep(0.5)
            counter+=1
            list_.append(thing[counter])
            print(list_)
        sleep(0.5)
        list_=[]
        counter= -1
except KeyboardInterrupt:
    print("\n\nbye")
    exit()