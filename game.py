print("Welcome To the game")
print(
    """ DESCRIPTION of the game - This a game where you enter a choice i.e. rock, paper, scissors.
Then the computer will also make a choice""")
print("Press p for playing")
x = "p"
z = str(input("Wanna play:"))
user_scored = 0
comp_scored = 0
while z == x:
    a = ["rock", "paper", "scissors"]
    b1 = str(input("Enter your choice: "))
    user_pick = b1.lower()
    import random
    comp_pick = random.choice(a)
    if user_pick == "rock" or user_pick == "paper" or user_pick == "scissors":
        print("your choice =", b1)
        print("computer choice =", comp_pick .lower())
    else:
      print("\033[1;31;40m invalid: choose any one -- rock, paper, scissors    \033[0m  \n") 
      comp_score = 0
      user_score = 0
    if user_pick == comp_pick:
        print('\033[1;37;40m Tie,you both select same \033[0m  \n')
        comp_score = 0
        user_score = 0
    elif user_pick == 'rock' and comp_pick == 'paper':
        comp_score = 1
        user_score = 0
        print('\033[1;33;40m You loose,computer select paper \033[0m  \n')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        user_score = 1
        comp_score = 0
        print('\033[1;32;40m You win,computer select scissors \033[0m  \n')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        comp_score = 1
        user_score = 0
        print('\033[1;33;40m You loose,computer select scissors \033[0m  \n')
    elif user_pick == 'paper' and comp_pick == 'rock':
        user_score = 1
        comp_score = 0
        print('\033[1;32;40m You win,computer select rock \033[0m  \n')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        comp_score = 1
        user_score = 0
        print('\033[1;33;40m You loose,computer select rock \033[0m  \n')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        user_score = 1
        comp_score = 0
        print('\033[1;32;40m You win ,computer select paper \033[0m  \n')
    
      
    user_scored = user_scored + user_score
    comp_scored = comp_scored + comp_score
    results = "\033[1;34;40m Your score:" + str(user_scored) +", Computer score:" + str(comp_scored) + "\033[0m  \n"
    print(results)
