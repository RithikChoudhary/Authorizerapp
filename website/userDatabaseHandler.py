from os import uname
from sqlite3 import Error, connect
from hashlib import md5

con = connect('authorizer.db', check_same_thread=False)

def insertRow(fName, lName, email, password):
    try:
        cursorObj = con.cursor()
        cursorObj.execute(f"INSERT INTO USERS VALUES('{fName}', '{lName}', '{email}', '{md5(password.encode()).hexdigest()}')")
        cursorObj.close()

        con.commit()
    except Error as e:
        print(e)



def getData(fName=None, lName=None, email=None, password=None):
    result = []

    try:
        cursorObj = con.cursor()

        if fName:
            cursorObj.execute(f"SELECT * FROM USERS WHERE fName=='{fName}'")
        elif lName:
            cursorObj.execute(f"SELECT * FROM USERS WHERE lName=='{lName}'")
        elif email:
            cursorObj.execute(f"SELECT * FROM USERS WHERE email=='{email}'")
        else:
            cursorObj.execute(f"SELECT * FROM USERS;")
        
        result = cursorObj.fetchall()
        cursorObj.close()

    except Error as e:
        print(e)
    
    return result


def checkPassword(email, password):
    user = getData(email=email)
    
    if len(user)>0: user=user[0]

    return f"{user[0].lower()}_{user[1].lower()}"
