import random

def OnlyIf(Input=0):
    print("[Info]>> Input is :",Input)
    if Input==0:
        print("This will shows only if 0.")

def IfElse(Input=0):
    print("[Info]>> Input is :",Input)
    if Input==0:
        print("This will shows when if else catch 0.")
    else:
        print("This will shows when if else catch others then 0.")

def ExtendIfElse(Input=0):
    print("[Info]>> Input is :",Input)
    if Input==0:
        print("This shows when Extend if-else catchs 0.")
    elif Input==2:
        print("It shows when the Extend if-else got not 0 but 2")
    else:
        print("Shows up when Extend if-else gets exception not 0 and nor 2.")

def WhileLoop(Input=0):
    print("[Info]>> Input is :",Input)
    TempStart = -1
    while TempStart < Input:
        print("While loop still running... Currently cached:", TempStart)

def ForLoop(Input=0):
    print("[Info]>> Input is :",Input)
    for i in range(Input):
        print("Currently in the range of Input makes for continue!! i is:", i)
        TempStart += 1

if __name__ == "__main__":
    OnlyIf(random.randint(0,1))
    IfElse(random.randint(0,10))
    ExtendIfElse(random.randint(0,7))
    WhileLoop(random.randint(1,4))
    ForLoop(random.randint(1,6))
    print("[Info]>> Can runs for more times to check different result!!")