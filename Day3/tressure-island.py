

print('''
           __
    .-'" (M /--.
  .'   .'|o|  @ `..
 /  .-/       _....'
|  '-/      .' |
|   /      |_\ |       Miami Dolphins
 \  |    /\|  /
  '.|   /   .'
    |  /_.-'
    | /
    | |       tre
   (,-,)
''')


print("Welcome to Tressure island, Your mission is to find the tressure")

direction = input("Type left or right to advance : ")

if direction == "left":
    swim = input("Type swim or wait to advance : ")
    if swim == "wait":
        door = input("Which door you want to choose ? (green,yellow,blue)")
        if door != "yellow":
            print("Game over")
        else:
            print("You Win!")
    else:
        print("Game over")
else:
    print("Game over")
