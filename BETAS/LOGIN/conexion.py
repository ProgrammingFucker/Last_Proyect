import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
                                    user="root",
                                    password="root",
                                    database="user",
                                    port="3306")
                                
    if conn.is_connected():
        db = conn.get_server_info()
        print("Connec to DB is okay", db)
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchall()
        print("Okay, np", record)

except Error as e:
    print("Error connecting",e )


sql = "Insert into login(name, email, password) values (%s, %s, %s)"
value = ("Jose","app@icloud.com", "12hghbn")   

cursor.execute(sql, value)

conn.commit();

print("Saved dates")



