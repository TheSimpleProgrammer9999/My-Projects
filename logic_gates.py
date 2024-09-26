a = None
b = None

def doubleinput():
    global a, b
    a = input("Enter for a ")
    b = input("Enter for b ")

while True:
    mode = input("What type(NOT, OR, AND, XOR, NOR, NAND, XNOR)? R to quit. ")
    if mode == "NOT":
        a = input("Enter for a ")
        if a == "1":
            print("OUTPUT: 0")
        elif a == "0":
            print("OUTPUT: 1")
        else:
            print("ERROR!")
    elif mode == "OR":
        doubleinput()
        if a == "1" or b == "1":
            print("OUTPUT: 1")
        elif a == "0" and b == "0":
            print("OUTPUT: 0")
        else:
            print("ERROR!")
    elif mode == "AND":
        doubleinput()
        if a == "1" and b == "1":
            print("OUTPUT: 1")
        elif a == "0" or b == "0":
            print("OUTPUT: 0")
        else:
            print("ERROR!")
    elif mode == "XOR":
        doubleinput()
        if a == "1" and b == "1" or a == "0" and b == "0":
            print("OUTPUT: 0")
        elif a == "1" and b == "0" or a == "0" and b == "1":
            print("OUTPUT: 1")
        else:
            print("ERROR!")

    elif mode == "NOR":
        doubleinput()
        if a == "1" or b == "1":
            print("OUTPUT: 0")
        elif a == "0" or b == "0":
            print("OUTPUT: 1")
        else:
            print("ERROR!")

    elif mode == "NAND":
        doubleinput()
        if a == "1" and b == "1":
            print("OUTPUT: 0")
        elif a == "0" or b == "0":
            print("OUTPUT: 1")
        else:
            print("ERROR!")

    elif mode == "XNOR":
        doubleinput()
        if a == "1" and b == "1" or a == "0" and b == "0":
            print("OUTPUT: 1")
        elif a == "1" and b == "0" or a == "0" and b == "1":
            print("OUTPUT: 0")
        else:
            print("ERROR!")

    else:
        if not mode.lower() == "r":
            print("\nERROR!")
            continue
        else:
            break
        
