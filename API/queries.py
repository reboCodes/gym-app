import mysql.connector

cnx = mysql.connector.connect(user='rebo', password='password', host='127.0.0.1', database='gym_app')



cnx.close()