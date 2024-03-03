import time


def text(text_):
    print(text_)

while True:
    inputter=input(">>")
    if inputter=="write()":
        inputp=input("\t>>")
        print(inputp + "\n\n")

    elif inputter=="CreateVar(:1)":
        inputv=input("\t>>")
        var_create=inputv
        inputvalue=input("Store value in class <var> ")
        stuffstoreinvar=inputvalue
        
    elif inputter=="CreateVar(:2)":
        inputv_=input("\t>>")
        var_create2=inputv_
        _inputvalue=input("Store value in class <var> ")
        stuffstoreinvar2=_inputvalue
        
    elif inputter=="CreateVar(:3)":
        inputv__=input("\t>>")
        var_create3=inputv__
        inputvalue__=input("Store value in class <var> ")
        stuffstoreinvar3=inputvalue__
        
    elif inputter=="CreateVar(:4)":
        inputv___=input("\t>>")
        var_create4=inputv___
        __inputvalue=input("Store value in class <var> ")
        stuffstoreinvar4=__inputvalue

    elif inputter=="credits(True)":
        text("\t-----credits-----\nProgrammed by the GitHub user TheSimpleProgrammer9999\nThis is a simple programming language,\ncalled ProgramScripter.The programming language\nintroduces basic mechanics, such\nas simple arithmetic, and variables. But it does not support lists or syntax errors. It\nonly supports basic arithmetic, printing stuff on the screen,\nprinting variables. The owner who write this programming language is\nnot a Python developer. He doesn't know how to code a syntax\nor whatever that is complex. So it is a very simple programming language.\nIt also doesn't support files either. You write code in the terminal\nin this programming language.")

    elif inputter=="<close>":
        text("Interpreter:: <closing>")
        break
    try:
        if inputter==(f"write_var() {var_create}"):
            print(stuffstoreinvar)

        elif inputter==(f"write_var() {var_create2}"):
            print(stuffstoreinvar2)
            
        elif inputter==(f"write_var() {var_create3}"):
            print(stuffstoreinvar3)
            
        elif inputter==(f"write_var() {var_create4}"):
            print(stuffstoreinvar4)
    except NameError:
        pass

    try:
        if inputter=="calculate(+)":
            cal=input("first integer: ")
            firstint=cal
            cal2=input("second integer: ")
            secondint=cal2
            print(int(firstint) + int(secondint))
        
        elif inputter=="calculate(-)":
            cal=input("first integer: ")
            firstint=cal
            cal2=input("second integer: ")
            secondint=cal2
            print(int(firstint) - int(secondint))
                
        elif inputter=="calculate(*)":
            cal=input("first integer: ")
            firstint=cal
            cal2=input("second integer: ")
            secondint=cal2
            print(int(firstint) * int(secondint))
                
        elif inputter=="calculate(/)":
            cal=input("first integer: ")
            firstint=cal
            cal2=input("second integer: ")
            secondint=cal2
            print(int(firstint) / int(secondint))
                            
        elif inputter=="calculate(%)":
            cal=input("first integer: ")
            firstint=cal
            cal2=input("second integer: ")
            secondint=cal2
            print(int(firstint) % int(secondint))

    except ZeroDivisionError:
       pass
