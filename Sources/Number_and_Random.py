import random

def rand_float():
    rand_num = random.random()
    print("test : ", rand_num)
    return rand_num

def rand_int(head=0,tail=100):
    rand_num = random.randint(head,tail)
    print("test : ", rand_num)
    return rand_num

if __name__ == "__main__":
    print("A random int :", rand_int(0,20))
    print("A random int :", rand_float())
    print("1+1=", (1 + 1) )
    print("7-3=", (7 - 3) )
    print("7/3=", (7 / 3) )
    print("8/0.2=", (8 / .2) )
    print("8/0.3=", (8 / .3) )
    print("7*6=", (7 * 6) )
    print("7%3=", (7 % 3) )