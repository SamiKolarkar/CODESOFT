import random
def play():
    print(">Enter \nr-for rock\ns-for scissors\np-for paper")
    player=input(">Enter your choice: ")
    computer=random.choice(['r','s','p'])
    print(f">Computer choose:{computer}")
    if computer=='p' and player=='r':
        print(">Sorry!,you lost.")
    elif computer=='s' and player=='p':
        print(">Sorry!,you lost.")
    elif computer=='r' and player=='s':
        print(">Sorry!,you lost.")
    elif computer==player:
        print(">It's a tie.")
    else:print(">You won!")
if __name__=="__main__":
    play()
