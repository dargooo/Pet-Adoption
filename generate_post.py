import sys
import string
import mysql.connector
from random import randint

try:
#    cnx = mysql.connector.connect(user='root', password='Ms41149.',
    cnx = mysql.connector.connect(user='coasttocoast_yijun', password='sql41149.',
                                  host='localhost', database='coasttocoast_petadoptionapp')
    cursor = cnx.cursor()
except:
    print("Log in mysql db failed!")

post_reader = open("datafile/post_info.txt")

def generate_post(username, is_person):
    insert_query = "INSERT INTO posts VALUES (%s, %s, %s, %s, %s, %s)"

    if is_person: num = randint(1, 3)
    else: num = randint(3, 15)

    for i in range(1, num + 1):
        line = post_reader.readline().split('\n')[0].split('|')
        if len(line) < 4: exit(0)
        pet_id      = line[0]
        open_time   = line[1]
        title       = line[2]
        description = line[3]
        query_data = (pet_id, username, title, open_time, None, description)
        cursor.execute(insert_query, query_data)
        cnx.commit()


def main(argv):
    select_query = "SELECT username, is_person FROM user"
    cursor.execute(select_query)
    result = cursor.fetchall()
    for (username, is_person) in result:
        generate_post(username, is_person)
    cursor.close()
    cnx.close()
 

if __name__=="__main__":
    main(sys.argv)
