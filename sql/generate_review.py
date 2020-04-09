import sys
import string
import mysql.connector
from random import randint
from random import choice

try:
    cnx = mysql.connector.connect(user='root', password='Ms41149.',
#    cnx = mysql.connector.connect(user='coasttocoast_yijun', password='sql41149.',
                                  host='localhost', database='coasttocoast_petadoptionapp')
    cursor = cnx.cursor()
except:
    print("Log in mysql db failed!")

review_reader = open("../datafile/reviews.csv")
count = 1

def generate_review(reviewee, reviewers):
    global count
    insert_query = "INSERT INTO review VALUES (%s, %s, %s, %s, %s)"

    num = randint(1, 10)

    for i in range(1, num + 1):
        reviewer = choice(reviewers)[0]
        content = review_reader.readline().split('\n')[0]
        # possibility - good : bad = 5 : 1
        num = randint(1, 7)
        if (num < 6):
            recommand = True
        else:
            recommand = False

        query_data = (count, reviewer, reviewee, content, recommand)
        cursor.execute(insert_query, query_data)
        cnx.commit()
        count += 1


def main(argv):
    query_1 = "SELECT DISTINCT username FROM posts"
    cursor.execute(query_1)
    reviewees = cursor.fetchall()

    query_2 = "SELECT username FROM user WHERE username NOT IN (SELECT username FROM posts)"
    cursor.execute(query_2)
    reviewers = cursor.fetchall()

    for (reviewee) in reviewees:
        generate_review(reviewee[0], reviewers)

    cursor.close()
    cnx.close()
 

if __name__=="__main__":
    main(sys.argv)
