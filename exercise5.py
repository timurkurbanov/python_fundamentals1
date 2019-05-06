distance = 0
energy = 10
while True:
    response = input("Are you going to run or walk?")
    if response == "q":
        break
    elif response == "r":
        if energy <= 0:
            print("stop for a rest")
        else:
            distance += 5
            energy -= 1    
    elif response == "w":
        if energy <= 0:
            print("stop for a rest")
        else:
            distance += 1
            energy+= 1
    else:
        print("I did not understand that")
    print ("Your distance from home is {}".format(distance))
    print ("Your energy level is {}".format(energy))
