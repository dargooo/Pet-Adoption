import sys
import requests
import json
import mysql.connector
from random import seed
from random import random
from random import choice

# curl -d "grant_type=client_credentials&client_id=w47BEjTrqDXNg0WDEqVCpmQtiYUWaIrhmg9HenATYrbSKWFmr4&client_secret=X7KbzXt1VN8TeXTOhat6LAaGvDLmrMtwNZ3a8AyW" https://api.petfinder.com/v2/oauth2/token
api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJ3NDdCRWpUcnFEWE5nMFdERXFWQ3BtUXRpWVVXYUlyaG1nOUhlbkFUWXJiU0tXRm1yNCIsImp0aSI6IjZmZGIzYTU1ODU0Mjc3YzU0NzM0NTE5ZTAwNzhiNDlkYjdhOGQ1YzM0YzYwYjRlYzVjZTExODUwNTc5ZDllNWU5NTViMmUzMjU3OGE0YjllIiwiaWF0IjoxNTg0MTQ5NTUyLCJuYmYiOjE1ODQxNDk1NTIsImV4cCI6MTU4NDE1MzE1Miwic3ViIjoiIiwic2NvcGVzIjpbXX0.cR14_WHAiaZ53ixdE9GtYy1uy8y5c_McGakLvHt-SOQ28puhQkG-tEqsFBdN04cQylqrkyGDlTrqwlXMC5HeeswsospN3PTZ4SWJ4XiBh5qJIxgmnMfOhnYkikgaUo77KTKySkodSnZWGxOeiiZz1Vmf0feS_ooz-tABc7TErjNOBCGuM5mnNfqCicl4VQdbSjKvkX6eVcaeHbY21WCNnd4pcbRD6EMO9Ewdm1LFzbUITX1hU0qvNlpu8nhu6tnaoGeKG3MVuwkuYGaSmsYxXKw0n5RvWBH5ijDNqfMVl9rx6e4JKXtAtLqvT9d_Om33BiBPrObtRTdRtBbpc4oRkw'
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

    if count > 200:
        return

    pages = [1, 2, 3, 4, 5]
    for page in pages:
        api_url = api_url_base + '/animals?breed=' + breed_name + '\&page=' + page
        print(api_url)
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            seed(1)
            pet_list = json.loads(response.content.decode('utf-8'))['animals']
            print(len(pet_list))
            insert_query = "INSERT INTO pet VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            for x in pet_list:
    
                age = round(random() * 15, 1)
    
                gender = x['gender']
    
                if age < 1:
                    weight = round(age * (3.5 + random()) + 2, 1)
                else:
                    weight = round(age * (0.8 + random() * 0.4) + 5, 1)
    
                personality_list = ['sweet', 'stubborn', 'proud', 'quite', 'cute', 'rotal', 'independent', 'happy', 'shy', 'adaptable', 'intelligent', 'anxious', 'brave', 'crazy', 'wild', 'needy']
                personality = choice(personality_list)
    
                color_list = ['white', 'brown', 'black', 'orange', 'gray', 'mix']
                color = choice(color_list)
    
                photo_list = x['photos']
                photo = "NULL"
                if (len(photo_list) > 0):
                    photo = photo_list[0]['full']
    
                hair_list = ['none', 'short', 'medium', 'long']
                hair = x['coat']
                if not hair:
                    hair = choice(hair_list)
    
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


