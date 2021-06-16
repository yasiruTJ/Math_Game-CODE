
# Easy mode query to gather data from the database

def data_easy():
     import mysql.connector
     db = mysql.connector.connect(user="Useradmin",password="user123456",
                                   host="127.0.0.1",database="customgame")
     cursor = db.cursor()
     # Extracting information from the table in the database using queries
     cursor.execute("SELECT Name FROM easy_mode")
     data1 = cursor.fetchall()
     cursor.execute("SELECT Total_Questions FROM easy_mode")
     data2 = cursor.fetchall()
     cursor.execute("SELECT Correct_Answers FROM easy_mode")
     data3 = cursor.fetchall()
     cursor.execute("SELECT Score FROM easy_mode")
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

# Medium mode query to gather data from the database

def data_medium():
     import mysql.connector
     db = mysql.connector.connect(user="Useradmin",password="user123456",
                                   host="127.0.0.1",database="customgame")
     cursor = db.cursor()
     # Extracting information from the table in the database using queries
     cursor.execute("SELECT Name FROM medium_mode")
     data1 = cursor.fetchall()
     cursor.execute("SELECT Total_Questions FROM medium_mode")
     data2 = cursor.fetchall()
     cursor.execute("SELECT Correct_Answers FROM medium_mode")
     data3 = cursor.fetchall()
     cursor.execute("SELECT Score FROM medium_mode")
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

# Hard mode query to gather data from the database

def data_hard():
     import mysql.connector
     db = mysql.connector.connect(user="Useradmin",password="user123456",
                                   host="127.0.0.1",database="customgame")
     cursor = db.cursor()
     # Extracting information from the table in the database using queries
     cursor.execute("SELECT Name FROM hard_mode")
     data1 = cursor.fetchall()
     cursor.execute("SELECT Total_Questions FROM hard_mode")
     data2 = cursor.fetchall()
     cursor.execute("SELECT Correct_Answers FROM hard_mode")
     data3 = cursor.fetchall()
     cursor.execute("SELECT Score FROM hard_mode")
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
