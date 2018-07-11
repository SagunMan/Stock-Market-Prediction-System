To execute the program, 

*first import the 'stockmarket.sql' file on your MySQL database.

*configure database connection properties on 'input.py' line number 6

edit the line
conn = MySQLdb.connect(host = "localhost", 
                                   user = "root", 
                                   passwd = "", 
                                   db = "stockmarket")

*set the following:
	host = "your hostname"
	user = "your username"
	passwd = "your password"

*execute app.py to run the program