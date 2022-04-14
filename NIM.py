import random
start = True
pulse = False
beat = False

print("                   NIM")
print("============================================")
print("The goal of the game is to be the player who")
print("takes the last game piece. You do this by")
print("taking 1, 2 or 3 pieces during your turn.")
print("============================================")

while start:

    winner = False
    win = True
    left = 12
    ai = random.choice([1,2,3])

    config = input("Do you wish to configure the game?(y/n) ")
    while not (config == "y" or config == "Y" or config == "n" or config == "N"):
        config = input("Do you wish to configure the game?(y/n) ")
    print()

    if config == "y" or config == "Y":
        save = abs(int(input("Please input the number of pieces you wish to use: ")))
        left = save
        ai = save % 4
        if ai == 0:
            ai = random.choice([1,1,2,3])
        print()

    game = input("Do you wish to play first or second?: ")
    while not (game == "first" or game == "First" or game == "second" or game == "Second"):
        game = input("\nDo you wish to play first or second?: ")
        
    if game == "first" or game == "First":
        pulse = True
    elif game == "second" or game == "Second":
        beat = True

    print()

    print(left, "Pieces remain.")
    print("=============================")

    while pulse:
        user = int(input("Please choice 1, 2 or 3: "))

        while not (user == 1 or user == 2 or user == 3):
            user = int(input("Please choice 1, 2 or 3: "))

        if (left - user) == 0 and win:
            winner = True
            win = False

        left = left - user
        print(left, "Pieces remain.")

        print("=============================")

        if left != 0:
            bot = left % 4
            if bot == 0:
                bot = random.choice([1,1,2,3])
            left = left - bot
            print("The computer took", bot, "piece(s).")
            print(left, "Pieces remain.")

            print("=============================")

        if left == 0:
            if winner:
                print("         **You Win**")
            else:
                print("    **The Computer Wins**")
            pulse = False


    while beat:
        if (left - ai) == 0 and win:
            winner = True
            win = False
            
        left = left - ai
        print("The computer took", ai, "piece(s).")
        print(left, "Pieces remain.")

        print("=============================")

        if left != 0:
            player = int(input("Please choice 1, 2 or 3: "))

            while not (player == 1 or player == 2 or player == 3):
                player = int(input("Please choice 1, 2 or 3: "))

            if (left - player) == 0 and win:
                winner = False
                win = False

            left = left - player
            print(left, "Pieces remain.")

            print("=============================")

        ai = left % 4
        if ai == 0:
            ai = random.choice([1,1,2,3])

        if left == 0:
            if winner:
                print("    **The Computer Wins**")
            else:
                print("         **You Win**")
            beat = False

    print()
    
    end = input("Do you want to play again?(y/n) ")
    while not (end == "y" or end == "Y" or end == "n" or end == "N"):
        end = input("Do you want to play again?(y/n) ")
    print()

    if end == "n" or end == "N":
        print("Thanks for playing NIM!")
        start = False
