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

    access_to_play = input("Do you want to play?").lower()
    if access_to_play == "yes":
        print("Okay, let's play")

else:
    print("You are not old enough to play this game, sorry :(")
