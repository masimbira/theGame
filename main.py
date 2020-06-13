print("Welcome to my game")
name = input("What is your name? ")
age = int(input("What is your age?"))


print("Hello", name, "you are ", age, "years old")
if age >= 18:
    print("You are old enough to play")
    to_play = input("Do you want to play the game? ")
    if to_play == "yes":
        print("Let's play!")
    else:
        print("Exiting the game........!!")
else:
    print("You are not old enough to play")

