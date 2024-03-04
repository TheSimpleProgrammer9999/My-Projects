import time

List1=[]
List2=[]
List3=[]


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

    elif inputter=="GetList(:1)":
            item1input=input("\tstore <value> in List1 ")
            stuffstoreinitem1=item1input
            List1.append(stuffstoreinitem1)
            
    elif inputter=="GetList(:2)":
            item2input=input("\tstore <value> in List2 ")
            stuffstoreinitem2=item2input
            List2.append(stuffstoreinitem2)
            
    elif inputter=="GetList(:3)":
            item3input=input("\tstore <value> in List3 ")
            stuffstoreinitem3=item3input
            List3.append(stuffstoreinitem3)

    elif inputter=="credits(True)":
        text("\t-----credits-----\nProgrammed by the GitHub user TheSimpleProgrammer9999\nThis is a simple programming language,\ncalled ProgramScripter.The programming language\nintroduces basic mechanics, such\nas simple arithmetic, variables, and lists. But it does not support syntax errors. It\nonly supports basic arithmetic, printing stuff on the screen,\nprinting variables, lists, and printing lists. The owner who write this programming language is\nnot a Python developer. He doesn't know how to code a syntax\nor whatever that is complex. So it is a very simple programming language.\nIt also doesn't support files either. You write code in the terminal\nin this programming language.")

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

        elif inputer==("write_list() List1"):
            print(List1)
            
        elif inputer==("write_list() List2"):
            print(List2)
                        
        elif inputer==("write_list() List3"):
            print(List3)
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
                                        
        elif inputter=="calculate(**)":
            cal=input("first integer: ")
            firstint=cal
            cal2=input("second integer: ")
            secondint=cal2
            print(int(firstint) ** int(secondint))

    except ZeroDivisionError:
       pass
