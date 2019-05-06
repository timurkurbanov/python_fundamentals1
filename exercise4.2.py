print("Enter your age, please")
number = input() #asking a user to enter thier age
age = 32 - int(number)
if int(number) < 105:
    print("We are {} years apart from each other".format(age))
if int(number) > 105:
    print("I am not sure I believe you")
