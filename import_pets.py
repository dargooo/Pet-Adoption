import sys
import requests
import json
import mysql.connector
from random import seed
from random import random
from random import choice

# curl -d "grant_type=client_credentials&client_id=w47BEjTrqDXNg0WDEqVCpmQtiYUWaIrhmg9HenATYrbSKWFmr4&client_secret=X7KbzXt1VN8TeXTOhat6LAaGvDLmrMtwNZ3a8AyW" https://api.petfinder.com/v2/oauth2/token
# curl -d "grant_type=client_credentials&client_id=N8BLOQ6rTPmlvJzWQqE7uI7u2kyAI27R1D8xUpYLJ4xU3VM69J&client_secret=rwluttBir6FAtwUHlvesD6a8rhOfx33kXb9r6whp" https://api.petfinder.com/v2/oauth2/token
api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJ3NDdCRWpUcnFEWE5nMFdERXFWQ3BtUXRpWVVXYUlyaG1nOUhlbkFUWXJiU0tXRm1yNCIsImp0aSI6IjVhMzFmODc2YTQ0NDkyNmQ0YjE0MmNmMzRlMjhlYTYxZTdlOWRlZGQxYmQxNjc2MmY2YmUyMTEyNjM4YWUwYzYzZWExMzhkMWI2Yjg5MmUyIiwiaWF0IjoxNTg0NzU1MDk2LCJuYmYiOjE1ODQ3NTUwOTYsImV4cCI6MTU4NDc1ODY5Niwic3ViIjoiIiwic2NvcGVzIjpbXX0.lmTtEjGIwvy4nQ-xLv0pNj-8Dq-Is2xraw5dvTl3NFVyDR31brj9luCrZzDhgyuvspG4mbnaDp6WfTjxpoc_cLHLH6Zmee4Idt5Oc1nN3BZqdMkpe3ggCuySjh6Co1Q8fj1fuLFRlatDil6HD-m9hsKTJisj0Ht_yNQUDe93uHmcXDpb0mlS7D22NuosJ37WNGYPE-XH1Rlk5TeBbXMw09gbX1_eBhz1T4Gg5f7LCK808Lk8_GzEZdZRPEMBp1iW81Ish09ZYF7Wk6l5UjYYOROfxVuiL9ZqkOsOYQ-gkfuhs-0k-56icnBhbrCTfSeYBPuMButW23hDJ-RVIYE7Zw'
api_url_base = 'https://api.petfinder.com/v2'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}
count = 27219

try:
#    cnx = mysql.connector.connect(user='root', password='Ms41149.',
    cnx = mysql.connector.connect(user='coasttocoast_yijun', password='sql41149.',
                                  host='localhost', database='coasttocoast_petadoptionapp')
    cursor = cnx.cursor()
except:
    print("Log in mysql db failed!")

writer = open("datafile/post_info.txt", "a")


def get_data(breed_id, breed_name):
    global count

#    pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pages = [11, 12, 13, 14, 15]
    for page in pages:
        api_url = api_url_base + '/animals?breed=' + breed_name + '&page=' + str(page)
        print(api_url)
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            seed(1)
            pet_list = json.loads(response.content.decode('utf-8'))['animals']
            print(len(pet_list))

            insert_query = "INSERT INTO pet VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            for x in pet_list:
                
                name = x['name'].split(" ")[0]
    
                age = round(random() * 15, 1)
    
                gender = x['gender']
    
                if age < 1: weight = round(age * (3.5 + random()) + 2, 1)
                else:       weight = round(age * (0.8 + random() * 0.4) + 5, 1)
    
                personality_list = ['sweet', 'stubborn', 'proud', 'quite', 'cute', 'royal', 'independent', 'happy', 'shy', 'adaptable', 'intelligent', 'anxious', 'brave', 'crazy', 'wild', 'needy']
                personality = choice(personality_list)
    
                color_list = ['white', 'brown', 'black', 'orange', 'gray', 'mix']
                color = choice(color_list)
    
                photo_list = x['photos']
                photo = "NULL"
                if (len(photo_list) > 0): photo = photo_list[0]['full']
    
                hair_list = ['none', 'short', 'medium', 'long']
                hair = x['coat']
                if not hair: hair = choice(hair_list)
 
                # write open_time, title, description into post_info.txt
                open_time = x['published_at']
                if open_time is None:
                    open_time = '0000-00-00 00:00:00'
                else:
                    date = open_time.split("T")[0]
                    time = open_time.split("T")[1].split("+")[0]
                    open_time = date + " " + time

                title_list = ['Cute %s!', 'Come to %s', '%s loves you!', 'Best pet ever - %s', '%s is waiting for you!', '%s does not want to be alone.', '%s wants to be with you', 'Poor %s looking for new owner', 'Say hello to %s', '%s']
                title = choice(title_list) % (name)

                description = x['description']
                if description is None: description = "No description."
                else:                   description = description.split("\n")[0]

                writer.write(str(count) + "|" + open_time + "|" + title + "|" + description + "\n")
    
                query_data = (count, name, age, gender[0], weight, x['status'], personality, color, photo, hair, breed_id, None, None)
                cursor.execute(insert_query, query_data)
                cnx.commit()
               
                count += 1

            # no more pets for this breed:
            if len(pet_list) < 20: break
        else:
            print("Failed to connect to " + api_url)
            exit(0)


def main(argv):
    select_query = "SELECT id AS breed_id, name AS breed_name FROM breed"
    cursor.execute(select_query)
    result = cursor.fetchall()
    for (breed_id, breed_name) in result:
        if breed_id > 0:
            get_data(breed_id, breed_name)
    cursor.close()
    cnx.close()
 

if __name__=="__main__":
    main(sys.argv)


