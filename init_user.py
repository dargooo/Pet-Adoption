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

u_reader = open("datafile/38650-username-sktorrent.txt", "rb")
p_reader = open("datafile/38650-password-sktorrent.txt", "rb")
a_reader = open("datafile/53962-address.csv", "rt") 
n_reader = open("datafile/30000-user.csv", "rt")

def init_user(i):
    insert_query = "INSERT IGNORE INTO user VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    username = u_reader.readline().split()[0]
    password = p_reader.readline().split()[0]
    if (not all(c in string.printable for c in username)) or (not all(c in string.printable for c in password)): return

    num = randint(1, 101)
    avatar = "ava" + str(num) + ".png"

    addr_line = a_reader.readline().split(',')
    zipcode = addr_line[0]
    city    = addr_line[2]
    state   = addr_line[3]

    mix_line = n_reader.readline().rstrip('\n').split(',')
    street   = mix_line[0]
    fullname = mix_line[1]
    email    = mix_line[2]

    addr = street + ", " + city + ", " + state

    # possibility - person : shelter = 5 : 1
    num = randint(1, 7)
    if (num < 6):
        is_person = True
    else:
        is_person = False
    
    query_data = (username, password, fullname, avatar, email, addr, zipcode, is_person)
    cursor.execute(insert_query, query_data)


def main(argv):
    for i in range(1, 20000):
        init_user(i)
    cnx.commit()
    cursor.close()
    cnx.close()
 

if __name__=="__main__":
    main(sys.argv)
