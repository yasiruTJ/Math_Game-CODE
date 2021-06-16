def data_qgame():
     # A Welcome message to the user
     print('''

                 ==============================================
                |                                              |
                |        Welcome to past game details!!!       |
                |                                              |
                 ==============================================    

     ''')
     print("\t\t\t\t Game Play") 
     import mysql.connector
     db = mysql.connector.connect(user="Useradmin",password="user123456",
                                   host="127.0.0.1",database="game")
     cursor = db.cursor()
     # Extracting information from the table in the database using queries
     cursor.execute("SELECT Name FROM quick_game")
     data1 = cursor.fetchall()
     cursor.execute("SELECT Total_Questions FROM quick_game")
     data2 = cursor.fetchall()
     cursor.execute("SELECT Correct_Answers FROM quick_game")
     data3 = cursor.fetchall()
     cursor.execute("SELECT Score FROM quick_game")
     data4 = cursor.fetchall()
     # Calling prettytable module to display a table to the user 
     from prettytable import PrettyTable
     x = PrettyTable()
     # Creating columns in the table
     column_names = ["Name", "Total Questions","Correct Answers","Score"]
     # Adding data from the database to the table
     x.add_column(column_names[0],data1)
     x.add_column(column_names[1],data2)
     x.add_column(column_names[2],data3)
     x.add_column(column_names[3],data4)
     # Displaying the table
     print(x)
     db.close()
    
