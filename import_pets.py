import sys
import requests
import json
import mysql.connector

# curl -d "grant_type=client_credentials&client_id=w47BEjTrqDXNg0WDEqVCpmQtiYUWaIrhmg9HenATYrbSKWFmr4&client_secret=X7KbzXt1VN8TeXTOhat6LAaGvDLmrMtwNZ3a8AyW" https://api.petfinder.com/v2/oauth2/token
api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJ3NDdCRWpUcnFEWE5nMFdERXFWQ3BtUXRpWVVXYUlyaG1nOUhlbkFUWXJiU0tXRm1yNCIsImp0aSI6IjUzOWIzYThjMTc3ZjhlNDZiZTllYTYyZmZiZWM4Mzg5MzcyMjNkZmI1MWQyYThhOThlMWJkNjgxNzNkMzJhZDg1ZWViZDdmNjdhYzNjZWE0IiwiaWF0IjoxNTgzNjU0MDQ2LCJuYmYiOjE1ODM2NTQwNDYsImV4cCI6MTU4MzY1NzY0Niwic3ViIjoiIiwic2NvcGVzIjpbXX0.cmDulNEI6W-qrRBu_rwtWAISWBE78iXBV82GrVkGPNAKvp_OXHU1Y52Uc5d7bOpMcXjsRIjv-1B6RIBPDoIKD9POfEZCIOzZQaCVl9WnenDgV9SPt7eEkR9MBTr_YRfhbqZUkjC0AdJpJ8WIucWwN9ccA7McFXG5mqLJw7pcikSRh2DDH8Xx78fxhwSFnHhBZQeCQzSKOuGHFXS3qdhEb0ndxQpwTZCvR1pAK9VrXuREEdGxZdOY8IcTwv56BNROOPbh5fIpvGCXfZovEzSe1ReYR1ictpk_1ROzA39h7Bw4dU_hIzSiVeSkM9k5UvWQzKkoo085D7-MlhqWsfh-0g'
api_url_base = 'https://api.petfinder.com/v2'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}
breeds = ['cockapoo']
count = 1

try:
    cnx = mysql.connector.connect(user='coasttocoast_yijun', password='sql41149.',
                                  host='localhost', database='coasttocoast_petadoptionapp')
    cursor = cnx.cursor()
except:
    print("Log in mysql db failed!")


def get_data(i):
    global count
    x = breeds[i]
    api_url = api_url_base + '/animals?breed=' + x
    print(api_url)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        pet_list = json.loads(response.content.decode('utf-8'))['animals']
        print(len(pet_list))
        insert_query = "INSERT INTO pets VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        for x in pet_list:
            c = x['colors']
            g = x['gender']
            p = x['photos'][0]
            query_data = (count, x['name'], 2.5, g[0], 7.7, x['status'], x['tags'], c['primary'], p['full'], x['coat'], 76, "NULL", "NULL")
            count += 1
            cursor.execute(insert_query, query_data)
    else:
        print("Failed to connect to " + api_url)


def main(argv):
    for i in range(0, len(breeds)):
        get_data(i)
    cnx.commit()
    cursor.close()
    cnx.close()
 

if __name__=="__main__":
    main(sys.argv)


