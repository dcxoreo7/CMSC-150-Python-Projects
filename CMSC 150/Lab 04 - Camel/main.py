import random


print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")

done = False

miles_traveled = 0
thirst = 0
camel_tiredness = 0
distance_of_the_natives = -20
number_of_drinks_in_canteen = 10
total = miles_traveled

while done == False:
    print("A. Drink from your Canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")


    user_choice = input("What is your choice? ")
    if user_choice.upper() == "Q":
        done = True

    elif user_choice.upper() == "D":
        distance_of_the_natives = distance_of_the_natives + random.randrange(7,14)
        camel_tiredness = 0
        print("The camel is happy")
        print("the natives continued their pursuit")
        print("during your rest and are")
        print("now",total - distance_of_the_natives,"miles away from you")

    elif user_choice.upper() == "E":
        print("miles traveled",total)
        print("number of drinks in canteen",number_of_drinks_in_canteen)
        print("The natives are",total - distance_of_the_natives,"miles away from you")

    elif user_choice.upper() == "C":
        x = random.randrange(10,20)
        print("You travel", x,"miles")
        total = total + x
        thirst = thirst + 1
        camel_tiredness = camel_tiredness + random.randrange(1,3)
        distance_of_the_natives = distance_of_the_natives + random.randrange(7,14)
        oasis_encounter = random.randrange(1, 21)
        if oasis_encounter == 1:
            number_of_drinks_in_canteen = 10
            camel_tiredness = 0
            thirst = 0
            print("You stumble upon an oasis")
            print("and refill your canteen with")
            print("fresh water and take a")
            print("rest with your camel")
            distance_of_the_natives = distance_of_the_natives + random.randrange(7, 14)
            print("during your rest, the natives continued their pursuit")

    elif user_choice.upper() == "B":
        y = random.randrange(5,12)
        miles_traveled = miles_traveled + random.randrange(5,12)
        print("You travel", y,"miles")
        thirst = thirst + 1
        camel_tiredness = camel_tiredness + 1
        distance_of_the_natives = distance_of_the_natives + random.randrange(7,14)
        oasis_encounter = random.randrange(1, 21)
        if oasis_encounter == 1:
            number_of_drinks_in_canteen = 10
            camel_tiredness = 0
            thirst = 0
            print("You stumble upon an oasis")
            print("and refill your canteen with")
            print("fresh water and take a")
            print("rest with your camel")

    elif user_choice.upper() == "A":
        if number_of_drinks_in_canteen > 0:
           number_of_drinks_in_canteen = number_of_drinks_in_canteen -1
           thirst = 0
           print("You feel refreshed")
        else: print("You're Canteen is empty")

    if thirst > 6:
            print("You died of ethirst")
            done = True
    elif thirst > 4:
        print("You are thirsty")

    if camel_tiredness > 8:
            print("Your Camel is dead")
            print("You try and run on foot but")
            print("despite your efforts, you")
            print("get caught by the natives")
            done = True

    elif camel_tiredness > 5:
        print("Your Camel is getting tired")

    if distance_of_the_natives > total:
        print("the natives have caught up to you")
        print("you try to escape but its too late")
        done = True
    elif distance_of_the_natives > total - 15:
        print("the natives are close")


    if total > 199:
        print("you made it across the desert and have escaped")
        print("the pursuit of the natives all with")
        print("your new camel!")
        done = True







