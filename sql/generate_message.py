import sys
import string
import mysql.connector
from random import randint
from random import choice
from random import random
from datetime import datetime, timedelta

try:
    cnx = mysql.connector.connect(user='root', password='Ms41149.',
#    cnx = mysql.connector.connect(user='coasttocoast_yijun', password='sql41149.',
                                  host='localhost', database='coasttocoast_petadoptionapp')
    cursor = cnx.cursor()
except:
    print("Log in mysql db failed!")

review_reader = open("../datafile/reviews.csv")
count = 1

def generate_message(user, talkers):
    global count
    insert_query = "INSERT INTO message VALUES (%s, %s, %s, %s, %s, %s)"

    start = datetime(2019,1,1)
    end   = datetime(2020,5,1)

    num = randint(2, 5)
    for i in range(1, num + 1):
        talker = choice(talkers)[0]
        diags = randint(0, 5)
        diag_start = start + (end - start) * random()
        diag_end = diag_start + timedelta(days=10) 
        for j in range(1, diags + 1):
            if j % 2 == 0:
                sender = user
                receiver = talker
            else:
                sender = talker
                receiver = user

            time = (diag_start + (diag_end - diag_start) * random()).strftime("%Y-%m-%d %H:%M:%S")
            content = review_reader.readline().split('\n')[0]
            query_data = (count, sender, receiver, time, content, False)
            cursor.execute(insert_query, query_data)
            count += 1
        if count % 3 != 0:
            # last message - unread
            content = review_reader.readline().split('\n')[0]
            query_data = (count, talker, user, diag_end.strftime("%Y-%m-%d %H:%M:%S"), content, True)
            cursor.execute(insert_query, query_data)
            count += 1
        cnx.commit()


def main(argv):
    query_1 = "SELECT DISTINCT username FROM posts"
    cursor.execute(query_1)
    users = cursor.fetchall()

    query_2 = "SELECT username FROM user WHERE username NOT IN (SELECT username FROM posts)"
    cursor.execute(query_2)
    talkers = cursor.fetchall()

    for (user) in users:
        generate_message(user[0], talkers)

    cursor.close()
    cnx.close()
 

if __name__=="__main__":
    main(sys.argv)
