# This is what's going to happen if the user chooses Quick game option

def q_quick():
    # A Welcome message to the user
    print('''

                 ==============================================
                |                                              |
                | Welcome to Quick Game.Let's have some fun!!! |
                |                                              |
                 ==============================================    

    ''')
    print("\t\t\t\t Game Play")
    
    # Calling variables and lists that are needed for the functioning of this module

    queslist = [] # List that contains generated questions
    canslist = []# List that contains correct answers
    uanslist = []# List that contains users' answers
    count = 0
    correctcount = 0
    score = 0
    
    # Asking user to input his/her name

    name = input("\n* Enter your name :")
    
    # Giving user 5 questions to answer using while loops

    print("\n\t\t\t Answer these questions!!!")
    for x in range (5):
        import random
        rand1 = random.randrange(0,11)
        rand2 = random.randrange(0,11)
        ques = (f'{rand1} + {rand2} = ' )# Creating question as a variable using f strings
        queslist.append(ques)# Input the generated questions to the list
        print("\t",rand1 , "+" , rand2, "?",end=" ")
        uans = input()
        if uans != "" :
            count += 1
        else:
            pass
        uanslist.append(uans)# Input the users' answer into the list
        cans = str(rand1 + rand2)
        canslist.append(cans)# Input the correct answer into the list

    # Displaying game results

    print("\n\t\t\t\t Game results ")
    print('''
          *************************************************************
          |                        WELLDONE!!!                        |
          |                                                           |
          |              Let's see how well you have played           |
          |                                                           |
          |                                                           |
          *************************************************************
        ''')
    
    
    # Showing user the data like his name, difficulty level and no.of questions he/she answered

    print("* Your name is ",name)
    print("* You answered ",count, "Questions\n")
    for y in range (5):
        if canslist[y] == uanslist[y]:
            correctcount += 1
            print("\t\t" f' {queslist[y]}{uanslist[y]} (Answer{canslist[y]})[correct]')# Printing the output with the created lists
        else:
            print("\t\t" f' {queslist[y]}{uanslist[y]} (Answer{canslist[y]})[Incorrect]' )
    print("\n* you have provided correct answers for ", correctcount, "questions")
    score = correctcount/5 * 100 
    print("\n* your score is ", score )

    # Establishing connection with the database

    import mysql.connector
    db = mysql.connector.connect(user="Useradmin",password="user123456",
                                     host="127.0.0.1" ,database="game")
    cursor = db.cursor()
    sqltext = "INSERT INTO Quick_game(Name,Total_Questions, Correct_Answers, Score ) VALUES(%s,%s,%s,%s)"
    myvalues = (name, 5 , correctcount , score )
    cursor.execute(sqltext,myvalues)
    db.commit()
    db.close()                       
   


         
