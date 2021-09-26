# NOTE :: THIS PROGRAMME OF STONE PAPER AND SCISSOR IS FOR BEGINNERS WHO ARE JUST INTRODUCED TO PYTHON PROJECT WORKS ....
# SO I JUST USED VARIABLES INSTEAD OF STRING JUST FOR YOUR CONVINEINCE BUT YOU CAN USE WORDS IT WONT BE A BIG PROBLEM!!!!!
# THE MAIN THING I WANT TO BRING IN LIGHT IS THAT YOU CAN EVEN TRY OUT [3 HUMAN PLAYERS] OR [2 HUMAN AND 1 BOT]
# OR [2 BOT AND 1 HUMAN] WITH THE METHOD I DISCUSSED OR CODED BELOW BY COMBINING THEM!! BUT REMEMBER THAT USER GIVE THE
# PERFECT INPUT REGARDING 0,1,2 OR STONE, PAPER AND SCISSOR
class Game:
    import random
    print("********WELCOME TO THE WORLD OF STONE-PAPER-SCISSOR*********")
    print(" ")
    print("DO YOU WANT TO PLAY WITH COMPUTER OR ANOTHER PLAYER !? CHOOSE WISELY :^")  # THIS IS FOR CHOICE OF USER
    print(" ")
    user_input = input(
        "PRESS 'b' TO PLAY WITH BOT OR PRESS 'p' TO PLAY WITH OTHER PLAYER : ").lower()  # I USED THE CONDITION JUST TO MAINTAIN CASES , IT IS NOT NECESSARY
    print(" ")
    if user_input == "b":
        print("ENTER ROUNDS YOU WANT TO PLAY StOnE-PaPeR-ScIsSoR")  # ROUND IS TAKEN AS LOOP
        print(" ")
        a = int(input())
        x = 0
        y = 0
        for i in range(1, a + 1):
            print("ENTER ANY ONE NUMBER AMONG 0,1 AND 2 FOR STONE , PAPER AND SCISSOR RESPECTIVELY!!")
            print(" ")
            print("PLAYER : ENTER YOUR CHOICE")
            print(" ")
            k = int(input())
            n = int(random.randint(0, 2))  # ITS THE MAIN THING IF YOU PLAY WITH BOT
            print("COMPUTER GIVES : %d" % n)
            print(" ")
            if (k != 0 and k != 1 and k != 2):  # IT IS NECESSARY TO KEEP CHECK THAT USER INPUT IS CORRECT OR NOT
                print("UH-OH SORRY ! ITS NOT WORKING!!")
            else:
                if k == 1 and n == 0:
                    print("PLAYER WINS!!")
                    print(" ")
                    x += 1
                elif k == 2 and n == 1:
                    print("PLAYER WINS")
                    print(" ")
                    x += 1
                elif k == 0 and n == 2:
                    print("PLAYER WINS")
                    print(" ")
                    x += 1
                else:
                    print("YOU LOSE!!")
                    print(" ")
                    y += 1
        if (x > y):
            print(" ")
            print("YOU WON MAN!! YOU WON FOR HUMANITY BRUH!! CHEERUP")
        else:
            print(" ")
            print("YOU LOOSE MAN!! BETTER LUCK NEXT TIME")

    elif user_input == "p":
        print(
            "ENTER ANY ONE NUMBER AMONG 0,1 AND 2 FOR STONE , PAPER AND SCISSOR RESPECTIVELY!!")  # SAME THING AS I DISCUSSED EARLIER
        print(" ")
        print("     !!!!!!!!!!!!!!!!!!!!!!DO NOT CHEAT AMONG YOURSELF!!!!!!!!!!!!!!!!!!!!!!     ")
        print(" ")
        print("ENTER ROUNDS YOU WANT TO PLAY StOnE-PaPeR-ScIsSoR")
        print(" ")
        o = int(input())
        for j in range(1, o + 1):
            n = 0
            m = 0
            print("PLAYER 1 : ENTER YOUR CHOICE")
            t = int(input())
            print("PLAYER 2 : ENTER YOUR CHOICE")
            v = int(input())
            if (t != 0 and v != 0 and t != 1 and v != 1 and t != 2 and v != 2):
                print("UH-OH SORRY ! ITS NOT WORKING!!")
            else:
                if t == 1 and v == 0:
                    print("PLAYER 1 WINS!!")
                    print(" ")
                    n += 1
                elif t == 2 and v == 1:
                    print("PLAYER 1 WINS")
                    print(" ")
                    n += 1
                elif t == 0 and v == 2:
                    print("PLAYER 1 WINS")
                    print(" ")
                    n += 1
                else:
                    print("PLAYER 2 WINS")
                    print(" ")
                    m += 1
        if (n > m):
            print(" ")
            print("!!PLAYER 1 WINS THE GAME!!")
        else:
            print(" ")
            print("!!PLAYER 2 WINS THE GAME!!")
    else:
        print(" ")
        print("## READ THE INSTRUCTIONS PROPERLY AND THEN CLICK THE RIGHT OPTION ##")


