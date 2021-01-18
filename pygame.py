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

            elif equippable_sword == "no":
                print("You have not acquired the rust sword and will not have the opportunity to do so for the rest of the game")
                lake = input("You progress further and notice that there is a lake with stone path running across the middle. You also notice that you can go around but it will take longer. What path do you choose to take here? (Across/Around?) ").lower()
                
            if lake == "across":
                print("You have made it across but have been bitten by a carnivorous fish. You have lost 5 health as a result")
                health -= 5
                print("Health = ", health, "HP")
            
            elif lake == "around":
                print("You went around safely")
                    
                new_area = input("After crossing the river you notice that there is a house about 100m north-west and a river 200m east. Which new area do you decide to go to? (House/River?)").lower
                    
                if new_area == "house":
                    print("You walk towards the wooden log house and see that the door is unlocked. You enter and notice that there is a man inside. He notices your health bar, walks over and decreases your health by")
                    health -= 5
                    print("Health = ", health, "HP")
                
                elif new_area == "river":
                        
                    fishing_rod = input("You see a fishing rod, do you wish to pick it up?(Yes/No?) ").lower()
                        
                    if fishing_rod == "yes":
                        print("You get a blister")
                        health -= 5
                        print("Health = ", health, "HP")
                        
                if health <= 0:
                    print("You have no more health, you slowly decend to a sweet slumber. :)")
                            
                else:
                    print("You have survived and you win")
           
            else:
                print("The sword sees you as a threat for not complying with the rules and it kills you")

        elif direction == "right":
            print("You die, F")

        else:
            print("That was neither left or right. The path is confused and eats you up for not adhering to the rules")

    else:
        print("Either you didn't type yes or you don't want to play :( . Either way I'll cya next time :)")

else:
    print("You are not old enough to play this game, sorry :(")
