print("LottoJuan! Bumoto para manalo! (THREE NUMBER LOTTO)")

LottoJuan = True

while LottoJuan:
    from random import randint
    def getRandomInt():
        num1 = randint(0, 9)
        num2 = randint(0, 9)
        num3 = randint(0, 9)
        return num1, num2, num3

    def getInput():
        num1 = int(input("Enter a first number (0-9): "))
        num2 = int(input("Enter a second number (0-9): "))
        num3 = int(input("Enter a third number (0-9): "))
        return num1, num2, num3

    Points = 0
    num1, num2, num3 = getInput()
    Lnum1, Lnum2, Lnum3 = getRandomInt()

    for l in Lnum1, Lnum2, Lnum3:
        if l == num1:
            Points = Points + 1
        else:
            Points = Points + 0
            if l == num2:
                Points = Points + 1
            else:
                Points = Points + 0
                if l == num3:
                    Points = Points + 1
                else:
                    Points = Points + 0

    print(f"\nYou're numbers are the following:\n{num1:>5}{num2:>5}{num3:>5}\n")
    print(f"The winning numbers are the following:\n{Lnum1:>5}{Lnum2:>5}{Lnum3:>5}\n")
        
    if Points == 3:
        print("Congratulations, you won!\n")
    else:
        print("Unfortunately, you loss.\n")

    ans = input("Do you want to play again (y/n)? ").lower()
    if ans[0] == "y":
        LottoJuan = True
    else:
        LottoJuan = False