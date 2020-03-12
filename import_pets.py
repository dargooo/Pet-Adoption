import sys
import requests
import json
import mysql.connector
import random
from random import seed
from random import random

# curl -d "grant_type=client_credentials&client_id=w47BEjTrqDXNg0WDEqVCpmQtiYUWaIrhmg9HenATYrbSKWFmr4&client_secret=X7KbzXt1VN8TeXTOhat6LAaGvDLmrMtwNZ3a8AyW" https://api.petfinder.com/v2/oauth2/token
api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJ3NDdCRWpUcnFEWE5nMFdERXFWQ3BtUXRpWVVXYUlyaG1nOUhlbkFUWXJiU0tXRm1yNCIsImp0aSI6ImNlYjk0MThlYzEzMThjMDdkYWU4ODMyZWIwZDdjMWZiNjA4MTQ0NjNmOTAxMWExYWI4ODI1OGQwYzA4ZmU1YzU0ODYzZjdlZDllNWRiMGJlIiwiaWF0IjoxNTgzOTg5NzU1LCJuYmYiOjE1ODM5ODk3NTUsImV4cCI6MTU4Mzk5MzM1NSwic3ViIjoiIiwic2NvcGVzIjpbXX0.zY3SZkMei_pOvGGYo-316RUfMcUf7PaBzcfB2nkJnfm2P-LKm709Y1LYeG4ussltPSGcimYI0k9si3sUSukdYvW2GZ8b9vp0xGSbjv7T7C82R9X66C7CPm3_HZ_pXK55pKqo_KB1_GoBnQqK-Oh-hoE5yelNQmAlhPug5fQMhd4i3H7_KBlfr7l2xPqWiWZaI1KopaAbLgilBemYcbbq6EFcwRgEAf2x4xv2hVg5myjEBQ2_f3ZjMMbxSSvuvinzE0GtS7GaEbS2lJkPAl8SclPNVLqSL3lanDrZMvhOvjgNWd3MRQdgjvhrX0-BJDvIn3MYLUHdAsCLrVIdgwJx7g'
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

            ######
            if count > 100:
                break
            #####

            age = round(random() * 15, 1)

            gender = x['gender']

            if age < 1:
                weight = round(age * (3.5 + random()) + 2, 1)
            else:
                weight = round(age * (0.8 + random() * 0.4) + 5, 1)

            personality_list = ['sweet', 'stubborn', 'proud', 'quite', 'cute', 'rotal', 'independent', 'happy', 'shy', 'adaptable', 'intelligent', 'anxious', 'brave', 'crazy', 'wild', 'needy']
            personality = random.choice(personality_list)

            color_list = ['white', 'brown', 'black', 'orange', 'gray', 'mix']
            color_result = x['colors']
            if len(color_result) > 0:
                color = color_resul['primary']
            else:
                color = random.choice(color_list)

            photo_list = x['photos']
            photo = "NULL"
            if (len(photo_list) > 0):
                photo = photo_list[0]['full']

            hair_list = ['none', 'short', 'medium', 'long']
            hair = x['coat']
            if not hair:
                hair = random.choice(hair_list)

            query_data = (count, x['name'], age, gender[0], weight, x['status'], personality, color, photo, hair, breed_id, "NULL", "NULL")
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


