import random
list = (0)
number = random.randint(1,10)
while number != int(list):
    list = int(input("your geuss:  "))
    if list < number:
        print("higher")
    elif list > number:
        print("lower")
if number == list:
    print("you win the number was",number)
