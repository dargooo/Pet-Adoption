import sys
import requests
import json
import mysql.connector
from random import seed
from random import random

# curl -d "grant_type=client_credentials&client_id=w47BEjTrqDXNg0WDEqVCpmQtiYUWaIrhmg9HenATYrbSKWFmr4&client_secret=X7KbzXt1VN8TeXTOhat6LAaGvDLmrMtwNZ3a8AyW" https://api.petfinder.com/v2/oauth2/token
api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJ3NDdCRWpUcnFEWE5nMFdERXFWQ3BtUXRpWVVXYUlyaG1nOUhlbkFUWXJiU0tXRm1yNCIsImp0aSI6ImJmYzA4ZWU5NDBiMmQ1NGFmNjEwOTZhMTk5ZmI5NmY0ZDc0NDA5Zjc3YTIyZDI4MDM1ZGNlMDhjNDMwYmZkYzcwNTgyMjcxM2ZiMDkxMjVjIiwiaWF0IjoxNTgzOTU2Mjc5LCJuYmYiOjE1ODM5NTYyNzksImV4cCI6MTU4Mzk1OTg3OSwic3ViIjoiIiwic2NvcGVzIjpbXX0.Js-QTupiGn4w84kNyt3niJXWg6g8A3L5IV__53LAORiXiiYzBQdZ46t5zHe7mG56V7la85tSgPPmRl0dp34cPx3iwq4Lep9752TYaLs0lBznRdpNv9XrpMV5lkqgk9Uc0pSWBDl0dxIeu4tsR9mPVYd5DS0YZnzjUzYG0W8Sv1Ld5KQP_Q5cJaTqZgAi4Ob4xXwmmnOhrhIMyENEf3mCc30yBxJeuMqp-SpRTE2-YunXlFXScBtRQKQMMuxDt2NOXX5WXR6ax-G7FKWicpQcmkuGuaR4GmyJv_nEStBhJ8TbRsDec7pMoGBLUQhYEyPsVF72QB2c6VnxvioAyzaUtg'
api_url_base = 'https://api.petfinder.com/v2'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}
breeds = ['cockapoo', 'Siberian','tiger', 'Persian']
count = 1

try:
    cnx = mysql.connector.connect(user='coasttocoast_yijun', password='sql41149.',
                                  host='localhost', database='coasttocoast_petadoptionapp')
    cursor = cnx.cursor()
except:
    print("Log in mysql db failed!")

def get_data(breed_id, breed_name):
    global count
    api_url = api_url_base + '/animals?breed=' + breed_name
    print(api_url)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        seed(1)
        pet_list = json.loads(response.content.decode('utf-8'))['animals']
        print(len(pet_list))
        insert_query = "INSERT INTO pets VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        for x in pet_list:
            color = x['colors']
            gender = x['gender']
            photo_list = x['photos']
            photo = "NULL"
            if (len(photo_list) > 0):
                photo = photo_list[0]['full']
            tag = x['tags']
            age = random() * 15
            weight
            if age < 1:
                weight = age * (3.5 + random()) + 2
            else:
                weight = age * (0.8 + random() * 0.4) + 5
            query_data = (count, x['name'], age, gender[0], weight, x['status'], ','.join(tag), color['primary'], photo, x['coat'], breed_id, "NULL", "NULL")
            count += 1
            cursor.execute(insert_query, query_data)
    else:
        print("Failed to connect to " + api_url)


def main(argv):
    select_query = "SELECT id AS breed_id, name AS breed_name FROM breed"
    cursor.execute(select_query)
    result = cursor.fetchall()
    for (breed_id, breed_name) in result:
        get_data(breed_id, breed_name)
    cnx.commit()
    cursor.close()
    cnx.close()
 

if __name__=="__main__":
    main(sys.argv)


