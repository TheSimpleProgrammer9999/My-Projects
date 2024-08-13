#modules
import math

#variables
mainIncluded = False
inMain = False
type_ = None
expression = None
geometryIncluded = False
examplesIncluded = False
ans = None
value = None
currentline = 1
debugger = []
#---------------------

#opens and check the contents of the file, then list them
with open("Simplescript.txt", 'r') as f:
    x = list(f)

#example functions, used when the player needs examples
def example1():
    print("""
your first program:
------------------------
include main

main {
    // first program
    print & hello world
} 
""")

def example2():
    print("""
something that repeats after you:
------------------------
include main

main {
    // repeater
    ask & write something, then I will repeat after you.
    assign & myVar = none
    storeans & myVar
    printvar & myVar
}
""")

def example3():
    print("""
simple operations:
------------------------
include main

main {
    // this will calculate 12 + 96(you can do other basic operations too)
    operation & 12 + 96
}
""")

def help_():
    print("*" * 30, """
print & arg: prints something(replace arg with something you want to print)
operation & arg: evaluates arg and returns the answer(replace arg with an operation, e.g 12 + 96)
constants: views mathematical constants
package arg: packages are other stuff you can work with but you have to 'import' them(replace arg with the package you want to import)

""", "*" * 30, """
There are currently 2 packages: geometry and examples
""", "*" * 30, """
circumferenceDiameter & arg: converts circumference value to diameter(you need the geometry package to do this)
diameterCircumference & arg: converts diameter value to circumference(you need the geometry package to do this)
radiusDiameter & arg: calculates the radius of the diameter(replace arg with the diameter length)
ask & arg: inputs the user(replace arg with the prompt)
assign & arg = arg2: this is how you create a variable(replace arg with the variable name and arg2 with the value)
storeans & arg: stores stuff that the user inputted(replace arg with the variable name)
printvar & arg: prints the value of a variable(replace arg with the variable name)
'repeat # arg: arg2': repeats arg2 arg times(replace arg with the number of how many times to repeat, and replace arg2 with the code that will be repeated. There could only be one block of code in the repeat loop)
'//': creates a comment
example1, example2, example3: shows examples in case you don't know what to create(you need the examples package)
""", "*" * 30)

#main
def main():
    global mainIncluded, inMain, type_, expression, geometryIncluded, examplesIncluded, ans, value, currentline
    for line in x:
        if line == "include main" or line == "include main\n":
            mainIncluded = True
            type_ = f"SPECIAL_PACKAGE, line {currentline}"
            debugger.append(type_)

        if line == "package geometry" or line == "package geometry\n":
            geometryIncluded = True
            type_ = f"PACKAGE, line {currentline}"
            debugger.append(type_)

        if line == "package examples" or line == "package examples\n":
            examplesIncluded = True
            type_ = f"PACKAGE, line {currentline}"
            debugger.append(type_)

        if line == "main {" or line == "main {\n":
            if mainIncluded == True:
                inMain = True
                type_ = f"MAIN, line {currentline}"
                debugger.append(type_)
            else:
                raise Exception("Error: No function named 'main'")
            
        if "operation" in line or "operation\n" in line:
            if inMain == True:
                type_ = f"OBJECT, line {currentline}"
                debugger.append(type_)
                try:
                    operation = line[line.index("&") + 2: -1]
                except ValueError:
                    pass
                else:
                    print(eval(operation))
            else:
                raise Exception(f"Error: No object called '{line.strip()}'")

        if "constants" in line or "constants\n" in line:
            if inMain == True:
                type_ = f"OBJECT, line {currentline}"
                debugger.append(type_)
                print(f"pi: {math.pi}\neuler: {math.e}\nsqrt of 2: {math.sqrt(2)}")
            else:
                raise Exception(f"Error: No object called '{line.strip()}'")

        if "circumferenceDiameter" in line or "circumferenceDiameter\n" in line:
            if inMain == True:
                if geometryIncluded == True:
                    type_ = f"OBJECT, line {currentline}"
                    debugger.append(type_)
                    try:
                        circumferenceVal = line[line.index("&") + 2: -1]
                    except ValueError:
                        pass
                    else:
                        diameter = float(circumferenceVal) / math.pi
                        print(diameter)
            else:
                raise Exception(f"Error: No object called '{line.strip()}'")

        if "diameterCircumference" in line or "diameterCircumference\n" in line:
            if inMain == True:
                if geometryIncluded == True:
                    type_ = f"OBJECT, line {currentline}"
                    debugger.append(type_)
                    try:
                        diameterVal = line[line.index("&") + 2: -1]
                    except ValueError:
                        pass
                    else:
                        circumference = float(diameterVal) * math.pi
                        print(circumference)
                else:
                    raise Exception(f"Error: No object called '{line.strip()}'")
            else:
                raise Exception(f"Error: No object called '{line.strip()}'")

        if "radiusDiameter" in line or "radiusDiameter\n" in line:
            if inMain == True:
                if geometryIncluded == True:
                    type_ = f"OBJECT, line {currentline}"
                    debugger.append(type_)
                    try:
                        circleLength = line[line.index("&") + 2: -1]
                    except ValueError:
                        pass
                    else:
                        radius = float(circleLength) / 2
                        print(radius)
                else:
                    raise Exception(f"Error: No object called '{line.strip()}'")
            else:
                raise Exception(f"Error: No object called '{line.strip()}'")

        if "print" in line or "print\n" in line:
            if inMain == True:
                type_ = f"OBJECT, line {currentline}"
                debugger.append(type_)
                try:
                    string = line[line.index("&") + 2: -1]
                except ValueError:
                    pass
                else:
                    print(string)
            else:
                raise Exception(f"Error: No object called '{line.strip()}'")
            
        if "ask" in line or "ask\n" in line:
            if inMain == True:
                type_ = f"OBJECT, line {currentline}"
                debugger.append(type_)
                try:
                    prompt = line[line.index("&") + 2: -1]
                except ValueError:
                    pass
                else:
                    ans = input(prompt)
            else:
                raise Exception(f"Error: No object called '{line.strip()}'")

        if "assign" in line or "assign\n" in line:
            if inMain == True:
                type_ = f"OBJECT, line {currentline}"
                debugger.append(type_)
                try:
                    var = line[line.index("&") + 2: line.index("=") - 1]
                except ValueError:
                    pass
                else:
                    value = line[line.index("=") + 2: -1]
            else:
                raise Exception(f"Error: No object called '{line.strip()}'")
            
        if "printvar" in line or "printvar\n" in line:
            if inMain == True:
                type_ = f"OBJECT, line {currentline}"
                debugger.append(type_)
                try:
                    varName = line[line.index("&") + 2: -1]
                    if varName == var:
                        if value == "none":
                            print(None)
                        else:
                            print(value)
                    else:
                        raise Exception(f"Error: No variable called '{varName}'")
                except ValueError:
                    pass
            else:
                raise Exception(f"Error: No object called '{line.strip()}'")
            
        if "storeans" in line or "storeans\n" in line:
            if inMain == True:
                type_ = f"OBJECT, line {currentline}"
                debugger.append(type_)
                try:
                    varName = line[line.index("&") + 2: -1]
                    if varName == var:
                        value = ans
                    else:
                        raise Exception(f"Error: No variable called '{varName}'")
                except NameError:
                    pass
            else:
                raise Exception(f"Error: No object called '{line.strip()}'")    

        if "example1" in line or "example1\n" in line:
            if inMain == True:
                if examplesIncluded == True:
                    type_ = f"OBJECT, line {currentline}"
                    debugger.append(type_)
                    example1()
                else:
                    raise Exception(f"Error: No object called '{line.strip()}'")
            else:
                raise Exception(f"Error: No object called '{line.strip()}'")
            
        if "example2" in line or "example2\n" in line:
            if inMain == True:
                if examplesIncluded == True:
                    type_ = f"OBJECT, line {currentline}"
                    debugger.append(type_)
                    example2()
                else:
                    raise Exception(f"Error: No object called '{line.strip()}'")
            else:
                raise Exception(f"Error: No object called '{line.strip()}'")
            
        if "example3" in line or "example3\n" in line:
            if inMain == True:
                if examplesIncluded == True:
                    type_ = f"OBJECT, line {currentline}"
                    debugger.append(type_)
                    example3()
                else:
                    raise Exception(f"Error: No object called '{line.strip()}'")
            else:
                raise Exception(f"Error: No object called '{line.strip()}'")

        if "data" in line or "data\n" in line:
            type_ = "*DATAPOINT"
            debugger.append(type_)
            if inMain == True:
                for i in debugger:
                    print(i)
            else:
                raise Exception(f"Error: No object called '{line.strip()}'")
            
        if "//" in line:
            type_ = f"COMMENT, line {currentline}"
            debugger.append(type_)
        
        # da repeat loop is kinda wild




        if "repeat" in line or "repeat\n" in line:
            if inMain == True:
                type_ = f"OBJECT, line {currentline}"
                debugger.append(type_)
                try:
                    number = line[line.index("#") + 2: line.index(":")]
                except ValueError:
                    pass
                else:
                    for i in range(int(number) - 1):
                        if "operation" in line or "operation\n" in line:
                            if inMain == True:
                                try:
                                    operation = line[line.index("&") + 2: -1]
                                except ValueError:
                                    pass
                                else:
                                    print(eval(operation))
                            else:
                                raise Exception(f"Error: No object called '{line.strip()}'")

                        elif "constants" in line or "constants\n" in line:
                            if inMain == True:
                                print(f"pi: {math.pi}\neuler: {math.e}\nsqrt of 2: {math.sqrt(2)}")
                            else:
                                raise Exception(f"Error: No object called '{line.strip()}'")

                        elif "circumferenceDiameter" in line or "circumferenceDiameter\n" in line:
                            if inMain == True:
                                if geometryIncluded == True:
                                    try:
                                        circumferenceVal = line[line.index("&") + 2: -1]
                                    except ValueError:
                                        pass
                                    else:
                                        diameter = float(circumferenceVal) / math.pi
                                        print(diameter)
                            else:
                                raise Exception(f"Error: No object called '{line.strip()}'")

                        elif "diameterCircumference" in line or "diameterCircumference\n" in line:
                            if inMain == True:
                                if geometryIncluded == True:
                                    try:
                                        diameterVal = line[line.index("&") + 2: -1]
                                    except ValueError:
                                        pass
                                    else:
                                        circumference = float(diameterVal) * math.pi
                                        print(circumference)
                                else:
                                    raise Exception(f"Error: No object called '{line.strip()}'")
                            else:
                                raise Exception(f"Error: No object called '{line.strip()}'")

                        elif "radiusDiameter" in line or "radiusDiameter\n" in line:
                            if inMain == True:
                                if geometryIncluded == True:
                                    try:
                                        circleLength = line[line.index("&") + 2: -1]
                                    except ValueError:
                                        pass
                                    else:
                                        radius = float(circleLength) / 2
                                        print(radius)
                                else:
                                    raise Exception(f"Error: No object called '{line.strip()}'")
                            else:
                                raise Exception(f"Error: No object called '{line.strip()}'")

                        elif "print" in line or "print\n" in line:
                            if inMain == True:
                                try:
                                    string = line[line.index("&") + 2: -1]
                                except ValueError:
                                    pass
                                else:
                                    print(string)
                            else:
                                raise Exception(f"Error: No object called '{line.strip()}'")
                            
                        elif "ask" in line or "ask\n" in line:
                            if inMain == True:
                                try:
                                    prompt = line[line.index("&") + 2: -1]
                                except ValueError:
                                    pass
                                else:
                                    ans = input(prompt)
                            else:
                                raise Exception(f"Error: No object called '{line.strip()}'")

                        elif "assign" in line or "assign\n" in line:
                            if inMain == True:
                                try:
                                    var = line[line.index("&") + 2: line.index("=") - 1]
                                except ValueError:
                                    pass
                                else:
                                    value = line[line.index("=") + 2: -1]
                            else:
                                raise Exception(f"Error: No object called '{line.strip()}'")
                            
                        elif "printvar" in line or "printvar\n" in line:
                            if inMain == True:
                                try:
                                    varName = line[line.index("&") + 2: -1]
                                    if varName == var:
                                        if value == "none":
                                            print(None)
                                        else:
                                            print(value)
                                    else:
                                        raise Exception(f"Error: No variable called '{varName}'")
                                except ValueError:
                                    pass
                            else:
                                raise Exception(f"Error: No object called '{line.strip()}'")
                            
                        elif "storeans" in line or "storeans\n" in line:
                            if inMain == True:
                                try:
                                    varName = line[line.index("&") + 2: -1]
                                    if varName == var:
                                        value = ans
                                    else:
                                        raise Exception(f"Error: No variable called '{varName}'")
                                except NameError:
                                    pass
                            else:
                                raise Exception(f"Error: No object called '{line.strip()}'")    

                        elif "example1" in line or "example1\n" in line:
                            if inMain == True:
                                if examplesIncluded == True:
                                    example1()
                                else:
                                    raise Exception(f"Error: No object called '{line.strip()}'")
                            else:
                                raise Exception(f"Error: No object called '{line.strip()}'")
                            
                        elif "example2" in line or "example2\n" in line:
                            if inMain == True:
                                if examplesIncluded == True:
                                    example2()
                                else:
                                    raise Exception(f"Error: No object called '{line.strip()}'")
                            else:
                                raise Exception(f"Error: No object called '{line.strip()}'")
                            
                        elif "example3" in line or "example3\n" in line:
                            if inMain == True:
                                if examplesIncluded == True:
                                    example3()
                                else:
                                    raise Exception(f"Error: No object called '{line.strip()}'")
                            else:
                                raise Exception(f"Error: No object called '{line.strip()}'")
                            
                        if "//" in line:
                            ...

            else:
                raise Exception(f"Error: No object called '{line.strip()}'")

        if "help" in line or "help\n" in line:
            if inMain == True:
                help_()
            else:
                raise Exception(f"Error: No object called '{line.strip()}'")


        currentline += 1
            




#calls the main function
if __name__ == '__main__':
    main()
