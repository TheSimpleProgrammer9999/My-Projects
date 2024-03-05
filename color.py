var=None
List1=[]


while True:
    input_=input("purple  ")
    if input_=="black green--green black":
        printinput=input("-- ")
        print(printinput)
    elif input_=="black black -?":
        varinput=input("-? ")
        var=varinput
    elif input_=="black black-black-black black":
        print(var)
    elif input_=="black--black black black -?- black":
        listinput=input("-?- ")
        item=listinput
        List1.append(item)
    elif input_=="black black-black-black black":
        print(List1)
