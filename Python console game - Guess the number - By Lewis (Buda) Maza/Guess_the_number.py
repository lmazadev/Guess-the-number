#By Lewis Maza (Buda). 2024
from random import randint

attempts = 0
estimated_number = 0
secret_number = randint(1,100)

name = input("Hi, tell me your name: ")
print(f"Hello {name}, I`ve thought of a number from 1 to 100.\nYou've 8 tries to guess.")


while attempts < 8:
    estimated_number = int(input("¿What's the number?: "))
    attempts+=1

    if estimated_number not in range(1,101):
        print("Your number isn't in the range. (1 to 100)")
    elif estimated_number < secret_number:
        print("The number is higher.")
    elif estimated_number > secret_number:
        print("The number is lower.")
    else:
        print(f"Congratulations {name}!, the secret number was: {secret_number}. You did it in {attempts} attempts.")
        break

if estimated_number != secret_number:
        print(f"GAME OVER.\nThe secret number was: {secret_number}.")
