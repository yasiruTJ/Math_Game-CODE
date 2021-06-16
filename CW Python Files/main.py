
# List variable declaration

queslist = [] # List that contains generated questions
canslist = []# List that contains correct answers
uanslist = []# List that contains users' answers
m_operators = ["+","-"]
h_operators = ["+","-","*"]

# Creating and initializing variables

count = 0
name = 0
dflevel = 0
qneed = 0
uans = 0
correctcount = 0

# Basic game menu

print("================================================================================")
print('''
                 |---------------------------------------------------|
                 |                   MATHMANIA                       |
                 |---------------------------------------------------|

      ''')
print("================================================================================")
for i in range (20):        
    from menu import game_menu
    game_menu()
    # Showing user the message to input his/her option
    option = input("\t\n* Enter your option : ")
    # User choosing the option Exit
    if (option == "Exit"):
        eop = input("\n* Are you sure You want to exit (Y/N) : ")#eop stands for exit option
        if eop == "Y":
            print('''

               ====================================================
              |                                                    |
              | Good Bye!!!. Come Again When you are ready to play |
              |                                                    |
               ====================================================    

            ''')
            break
        print("================================================================================")
    # User choosing the option quick game
    elif option == "Quick game":
        # Calling the q_quick function which is in qgame module in quickgame package
        import Quickgame.qgame
        Quickgame.qgame.q_quick()
        print("================================================================================")

    # User choosing the option Custom game
    elif option == "Custom game":
        import Customgame.welcome
        Customgame.welcome.custom_welcome()
        dflevel = input("\n* Select your difficulty level (Easy / Medium / Hard) : ")# dflevel stands for difficlty level
        if dflevel == "Easy":
            import Customgame.easy
            Customgame.easy.easy_mode()
            print("================================================================================")
        elif dflevel == "Medium":
            import Customgame.medium
            Customgame.medium.medium_mode()
            print("================================================================================")
        elif dflevel == "Hard":
            import Customgame.hard
            Customgame.hard.hard_mode()
            print("================================================================================")

    elif (option == "Past game details"):
        fetchreq = input("\n* What is the game type( Quick game / Custom game ) : ")
        if fetchreq == "Quick game":
            import results.quickgame
            results.quickgame.data_qgame()
            print("================================================================================")
        elif fetchreq == "Custom game":
            mode = input("\n* What is the game mode (Easy / Medium / Hard) :")
            import results.customgame
            # A Welcome message to the user
            print('''

                 ==============================================
                |                                              |
                |        Welcome to Past Game Details!!!       |
                |                                              |
                 ==============================================    

            ''')
            print("\t\t\t\t Game Play")
            if (mode == "Easy"):
                results.customgame.data_easy()
            elif(mode == "Medium"):
                results.customgame.data_medium()
            elif(mode == "Hard"):
                results.customgame.data_hard()
            print("================================================================================")  
        else:
            import exitoption.exitop
            exitoption.exitop.exit()
            print("================================================================================")
    # User leaves the option without inputing anything or by inputing an invalid character
    else:
        import exitoption.exitop
        exitoption.exitop.exit()
        print("================================================================================")


