var=None
List=[]


while True:
    input_=input(">> ")
    if input_=="!! <:::>":
        inputprint=input("::: ")
        print(inputprint)

    elif input_=="!!! :::":
        inputvar=input("!!! ")
        var=inputvar
        value=input("::: ")
        val=value

    elif input_==f"!! :{var}:":
        if var==None:
            pass
        else:
            print(val)

    elif input_=="++ []":
        inputlist=input("#### ")
        item_add=inputlist
        List.append(item_add)
    
    elif input_=="-- []":
        inputlist_=input("###- ")
        removed_item=inputlist_
        try:
            List.remove(removed_item)
        except ValueError:
            pass

    elif input_=="!! <::::>":
        print(List)