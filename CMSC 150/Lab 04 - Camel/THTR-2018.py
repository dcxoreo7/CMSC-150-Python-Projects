import random


print("Welcome to !")
print("During 'Yell Like Hell' you find the secret Simpson medallion")
print("that could lead to world destruction if in the.")
print("Its your job to escape hyrule with the triforce")
print("and deliver it to Princess Zelda who is in Termina all while")
print("on your trustee steed Epona, whom you must keep from dying from tiredness")
print("Make sure that you use your health potion mixture accordingly so that you dont fatigue and pass out.")
print("Also try not to allow Ganon's forces gain ground on you, if so")
print("defeat them and claim the loot necessary to successfully escape.")


done = False

miles_traveled = 0
stamina = 50
eponas_tiredness = 0
carrot = 7
rupees = 0
distance_of_ganons_forces = -10
health_potions = 4
total = miles_traveled

while done == False:
    print("A. Use a health potion.")
    print("B. Travel observantly, keeping an eye out for rupees.")
    print("C. Ahead full speed.")
    print("D. Feed Epona and rest for the night.")
    print("F. Buy care package from Beetles shop")
    print("E. Inventory check.")
    print("Q. Quit.")


    user_choice = input("What is your choice? ")
    if user_choice.upper() == "Q":
        done = True

    elif user_choice.upper() == "D":
        eponas_tiredness = eponas_tiredness - 3
        carrot = carrot - 1
        stamina = stamina + 20
        print("Epona is now energized")
        print("You feel slightly rested")
        distance_of_ganons_forces = distance_of_ganons_forces + random.randrange(4, 14)


    elif user_choice.upper() == "E":
        print("sheikah tracker reads",total,"miles traveled")
        print("stamina",stamina)
        print("you have",health_potions,"health potions")
        print("Sheikah tracer reads that Ganon's forces are",total - distance_of_ganons_forces,"miles away from you")
        print("you have",rupees,"rupees")

    elif user_choice.upper() == "F":
        if rupees < 80:
            print("You need more rupees")
        else:
            rupees = rupees - random.randrange(55, 80)
            health_potions = health_potions + random.randrange(2, 4)
            carrot = carrot + random.randrange(2, 4)
            print("You buy a couple of carrots and potions for the road.")


    elif user_choice.upper() == "C":
        x = random.randrange(17,25)
        print("You travel", x,"miles")
        total = total + x
        eponas_tiredness = eponas_tiredness + random.randrange(1,3)
        distance_of_ganons_forces = distance_of_ganons_forces + random.randrange(8,14)
        outpost_encounter = random.randrange(1, 10)
        stamina = stamina - random.randrange(5,10)
        if outpost_encounter == 1:
            eponas_tiredness = eponas_tiredness - 1
            stamina = stamina - random.randrange(10, 15)
            rupees = rupees + random.randrange(10, 25)
            print("You travel with so much speed")
            print("that you unknowingly find yourself")
            print("in a bandit outpost.")
            print("You fight your way out and take what you can, but get wounded during the process.")


    elif user_choice.upper() == "B":
        y = random.randrange(10,15)
        print("You travel", y,"miles")
        distance_of_ganons_forces = distance_of_ganons_forces + random.randrange(8,14)
        print("you find a few rupees on the road while traveling lightly")
        rupees = rupees + random.randrange(25,50)
        stamina = stamina - random.randrange(2, 5)

    elif user_choice.upper() == "A":
        if health_potions > 0:
           health_potions = health_potions - 1
           stamina = 100
           print("You feel rejuvienated")
        else: print("You don't have anymore potions left.")

    if stamina < 1:
            print("You passed out and were captured by Ganon's forces.")
            print("Ganon now has the triforce and with it, he will rule the world.")
            print("GAME OVER")
            done = True
    elif stamina < 15:
        print("You feel weak")

    if eponas_tiredness > 12:
            print("Epona fainted")
            print("You try to run and battle foot but")
            print("despite your efforts, you")
            print("are overwhelmed by Ganon's Forces.")
            print("GAME OVER")
            done = True

    elif eponas_tiredness > 7:
        print("Epona is getting tired")

    if distance_of_ganons_forces > total - 20:
        print("Ganons forces are close")

    elif distance_of_ganons_forces > total:
        print("you are caught and overwhelmed by Ganon's forces")
        print("GAME OVER")
        done = True


    if total > 300:
        print("you made it out of Hyrule to where Zelda")
        print("is and deliver the triforce, thus")
        print("saving the world from Ganon!")
        done = True