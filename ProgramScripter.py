import time
from error_syntax import error


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
    try:
        if inputter==(f"write_var({var_create})"):
            print(stuffstoreinvar)

        elif inputter==(f"write_var({var_create2})"):
            print(stuffstoreinvar2)
    except NameError:
        pass

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
    try:
        if inputter=="string_calculate(+)":
            cal=input("first string: ")
            firststr=cal
            cal2=input("second string: ")
            secondstr=cal2
            print(int(var_create) + int(var_create2))
        
        if inputter=="calculate(-)":
            cal=input("first integer: ")
            firststr=cal
            cal2=input("second integer: ")
            secondstr=cal2
            print(int(firstint) - int(secondint))
                
        if inputter=="calculate(*)":
            cal=input("first integer: ")
            firststr=cal
            cal2=input("second integer: ")
            secondstr=cal2
            print(int(firstint) * int(secondint))
                
        if inputter=="calculate(/)":
            cal=input("first integer: ")
            firststr=cal
            cal2=input("second integer: ")
            secondstr=cal2
            print(int(firstint) / int(secondint))
    except NameError:
        error(f"interpreter_interrupted():\n\tVariable {firststr}, {secondstr} not availiable")
    
