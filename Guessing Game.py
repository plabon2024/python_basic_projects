import random
print("""Welcome to the Number Guessing Game!
Try to guess the number between 1 and 100.""")
index=0
main_num = random.randint(1, 100)
while True:
    try:
        user_num = int(input("Enter your guess: "))
        index = index + 1
        if not (1 <= user_num <= 100):
            print("Try useing a number between 1 and 100.")
        elif user_num < main_num:
            print('Too low!')
        elif user_num > main_num:
            print('Too high!')
        elif main_num == user_num:
            print("Congratulations! You've guessed the number in ", index, " attempts.")
            break
    except Exception as e:
        print('Sorry use a number between 1 and 100.')
        index = index + 1
        continue
