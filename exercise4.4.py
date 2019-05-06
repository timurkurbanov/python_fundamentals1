print("Guess a number...")
secret_number = 1
user_number = int(input())

if secret_number == user_number:
    print("You win!")
elif secret_number - user_number == 1:
    print("So close!")
else:
    print("Try again!")


