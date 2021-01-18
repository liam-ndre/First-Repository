print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name,",", age, "years of age")

health = 10

if age >= 18:
    print("You are old enough to play this game!")

    access_to_play = input("Do you want to play? ").lower()
    if access_to_play == "yes":
        print("Okay, let's play")
        print("Current Health =" , health, "HP")

        direction = input("You begin walking and encounter a fork in the road. Where do you go? Left or Right? ").lower()
        if direction == "left":
            print("Okay let's go left")

            equippable_sword = input("Wow, you found a sword. Would you like to pick it up? (Yes/No?) ").lower()
            if equippable_sword == "yes":
                print("You have now acquired a rust sword!")

                lake = input("You progress further and notice that there is a lake with stone path running across the middle. You also notice that you can go around but it will take longer. What path do you choose to take here? (Across/Around?) ").lower()
                if lake == "across":
                    print("You have made it across but have been bitten by a carnivorous fish. You have lost 5 health as a result")
                    health -= 5
                    print("Health = ", health, "HP")

                
            elif equippable_sword == "no":
                print("You have not acquired the rust sword and will not have the opportunity to do so for the rest of the game")

            else:
                print("The sword sees you as a threat for not complying with the rules and it kills you")

        
        elif direction == "right":
            print("You die, F")
        
        else:
            print("That was neither left or right. The path is confused and eats you up for not adhering to the rules")
        

elif age >= 14 and age <= 17:
    print("You can play the game but with parental guidance :)")

    access_to_play = input("Do you want to play? ").lower()
    if access_to_play == "yes":
        print("Okay, let's play")

        direction = input("Left or Right? ").lower()
        if direction == "left":
            print("Okay let's go left")
            print("Wow, you found a sword. Would you like to pick it up?")

            equippable_sword = input("Yes or No? ").lower()
        
        elif direction == "right":
            print("You die, F")
        
        else:
            print("Oops, I couldn't lead you. Did you type either 'left' or 'right'?")
    else:
        print("Either you didn't type yes or you don't want to play :( . Either way I'll cya next time :)")

else:
    print("You are not old enough to play this game, sorry :(")
