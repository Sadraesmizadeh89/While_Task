import random

n = random.randrange(0,100)

s = 10

while s >= 0 :
    a = int(input("Enter a number : (0 , 100) "))

    if a == n :
        print("its Correct!")
        f = "yes"
        break
    elif a < n :
        print("please enter large number! ")
    elif a > n :
        print("please enter smaller number! ")
    if s == -1 :
        print(f'you lost . the computer choice is {n}')
    s -= 1