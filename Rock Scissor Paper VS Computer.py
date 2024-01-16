import random
def intro():
    print("\\"*7,"WELCOME TO ROCK SCISSOR GAME","/"*7,"\n")
    input("tab [ Enter ] to start")
    print(" ")
    print("as usual, you need to choose [ Rock ],[ Paper ] or [ Scissor ] \n"
          "to against the computer")
    print("tab [ Enter ] after you type your choose !!! \n")
intro()
def RockScissorPaper():
    lst = ['Rock', 'Paper', 'Scissor']
    w = input("Choose [Rock/Paper/Scissor]:")
    x = w.capitalize()
    print(" ")
    y = random.choice(lst)

    if x not in lst:
        print("please input the right keyword!!! \n")
        RockScissorPaper()
    else:
        print(f"   {'-'*8}you choose [{x}]{'-'*8}")
        print(f"{'-'*8}computer choose [{y}]{'-'*8}\n")
        if x == y:
            print("/"*7," You got Drew ","\\"*7)
        elif x == 'Rock' and y == 'Paper':
            print("/"*7," you lose ","\\"*7)
        elif x == 'Rock' and y == 'Scissor':
            print("/"*7," you win ","\\"*7)
        elif x == 'Scissor' and y == 'Paper':
            print("/"*7," you win ","\\"*7)
        elif x == 'Scissor' and y == 'Rock':
            print("/"*7,' you lose ',"\\"*7)
        elif x == 'Paper' and y == 'Scissor':
            print("/"*7," you lose ","\\"*7)
        elif x == 'Paper' and y == 'Rock':
            print("/"*7," you win ","\\"*7)

    print(" ")
    print("Tab [ Enter ] after answer")


    end = input("Do you want to play again? [y/n] :")

    while end != "y":
        print(" ")
        print("Thankyou for play the game!!! \n")
        print("Credit : Danieka")
        break

    if end == "y":
        print(" ")
        RockScissorPaper()
RockScissorPaper()