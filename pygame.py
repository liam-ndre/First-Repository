print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name,",", age, "years of age")
health = 10

if age >= 18:
    print("You are old enough to play this game!")

    access_to_play = input("Do you want to play?")
    if access_to_play == "yes" or "Yes":
        print("Okay, let's play")

elif age >= 14 and age <= 17:
    print("You can play the game but with parental guidance :)")

    access_to_play = input("Do you want to play? ").lower()
    if access_to_play == "yes":
        print("Okay, let's play")

        direction = input("Left or Right? ").lower()
        if direction == "left":
            print("Okay let's go left")
        
        elif direction == "right":
            print("Okay let's go right")
        
        else:
            print("Oops, I couldn't lead you. Did you type either 'left' or 'right'?")
    else:
        print("Either you didn't type yes or you don't want to play :( . Either way I'll cya next time :)")

else:
    print("You are not old enough to play this game, sorry :(")
