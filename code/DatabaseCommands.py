import mysql.connector


def DBInsertRequest(ReqText):

    database = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="dbone"
    )

    cursor = database.cursor()

    try:

        insert_string = ("INSERT INTO request (Description) VALUES ('") + ReqText + ("');")
        cursor.execute(insert_string)

    except mysql.connector.Error as error:
        print("Fehler:", error)

    finally:
        database.commit()
        cursor.close()
        database.close()