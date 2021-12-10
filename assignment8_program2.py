print("Hulaan mo, Juan! Number Guesser.")

HulaJuan = True

while HulaJuan:
    from random import randint
    num = randint(0, 100)
    guess = int(input("Enter your guess: "))

    while guess != num:
        if guess > num:
            guess = int(input("Status: Greater than, try again.\nEnter your guess: "))
        elif guess < num:
            guess = int(input("Status: Less than, try again.\nEnter your guess: "))

    if num == guess:
        print("Congratulations, you guessed the random number.")

    ans = input("Do you want to play again (y/n)? ").lower()
    if ans[0] == "y":
        HulaJuan = True
    else:
        HulaJuan = False