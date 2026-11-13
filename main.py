import random

while True:
    user_choice = input("Roll the dice ? y/n")
    if user_choice.lower().strip() == "y":
        first = random.randint(1, 10)
        seccond = random.randint(1, 10)
        print(f"({first},{seccond})")
    elif user_choice.lower().strip() == "n":
        print("Thanks for playing")
        break
    else:
        print("please enter y or n and try again")
