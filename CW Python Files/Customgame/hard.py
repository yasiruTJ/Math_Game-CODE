def hard_mode():

# Hard Mode
    # Taking the user's name, difficlty level and number of questions he/she wants to answer as an input to enter to the database when saving

    name = input("\n* Enter your name : " )
    qneed = int(input("\n* How many questions you need to answer : "))# qneed stands for questions need to answer

    # Calling variables and lists that are needed for the functioning of this module

    queslist = [] # List that contains generated questions
    canslist = []# List that contains correct answers
    uanslist = []# List that contains users' answers
    m_operators = ["+","-"]
    h_operators = ["+","-","*"]
    count = 0
    correctcount = 0

    # Giving user questions according to his inputs 

    print("\n\t\t\t Think Well And Answer these questions!!!")
    for x in range(qneed):
        import random
        rand1 = random.randrange(0,101)
        rand2 = random.randrange(0,101)
        rand3 = random.choice(h_operators)# In here i am going to use random.choice  
        if(rand3 == "+"):
            ques = (f'{rand1} + {rand2} = ')# Creating question as a variable using f strings
            queslist.append(ques)# Input the generated questions to the list
            print("\t",rand1 , "+" , rand2, "?" ,end=" ")
            uans = input()
            if uans != "" :
                count += 1
            else:
                pass
            uanslist.append(uans)# Input the users' answer into the list
            cans = str(rand1 + rand2)
            canslist.append(cans)# Input the correct answer into the list
        elif(rand3 == "-"):
            ques = (f'{rand1} - {rand2} = ')# Creating question as a variable using f strings
            queslist.append(ques)# Input the generated questions to the list
            print("\t",rand1 , "-" , rand2, "?" ,end=" ")
            uans = input()
            if uans != "" :
                count += 1
            else:
                pass
            uanslist.append(uans)# Input the users' answer into the list
            cans = str(rand1 - rand2)
            canslist.append(cans)# Input the correct answer into the list
        elif(rand3 == "*"):
            ques = (f'{rand1} * {rand2} = ')# Creating question as a variable using f strings
            queslist.append(ques)# Input the generated questions to the list
            print("\t",rand1 , "*" , rand2, "?" ,end=" ")
            uans = input()
            if uans != "" :
                count += 1
            else:
                pass
            uanslist.append(uans)# Input the users' answer into the list
            cans = str(rand1 * rand2)
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
    
    print("* Your name is ", name,"\n")
    print("* You played the game with Hard mode\n")
    print("* There were ",qneed, "Questions generated\n")
    print("* You answered ",count, "Questions\n")
    for y in range(qneed):
        if canslist[y] == uanslist[y]:
                correctcount += 1
                print("\t\t" f'{queslist[y]}{uanslist[ y ]} (Answer {canslist[y]})[correct]')# Printing the output with the created lists
        else:
                print("\t\t" f'{queslist[y]}{uanslist[ y ]} (Answer {canslist[y]})[Incorrect]' )      
    print("\n* you have provided correct answers for ", correctcount, "questions")
    score = correctcount/qneed * 100
    print("\n* your score is ", score ,"%")

    # Establishing connection with the database

    import mysql.connector
    db = mysql.connector.connect(user="Useradmin",password="user123456",
                                     host="127.0.0.1",database="customgame")
    cursor = db.cursor()
    sqltext = "INSERT INTO Hard_mode (Name,Total_Questions,Correct_Answers,Score)VALUES (%s,%s,%s,%s)"
    myvalues = (name,qneed,correctcount,score)
    cursor.execute(sqltext,myvalues)
    db.commit()
    db.close()


    

    
    
    
    

    
        
    
        
        
    
            
    
    

