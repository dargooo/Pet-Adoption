import sys
import requests
import json
import mysql.connector

# curl -d "grant_type=client_credentials&client_id=w47BEjTrqDXNg0WDEqVCpmQtiYUWaIrhmg9HenATYrbSKWFmr4&client_secret=X7KbzXt1VN8TeXTOhat6LAaGvDLmrMtwNZ3a8AyW" https://api.petfinder.com/v2/oauth2/token
api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJ3NDdCRWpUcnFEWE5nMFdERXFWQ3BtUXRpWVVXYUlyaG1nOUhlbkFUWXJiU0tXRm1yNCIsImp0aSI6IjMzNGNjMDhmMTcyOGExODAwYzc5Y2IzN2NlN2ZhOTZmMzJlZGE4MmE1NWZjY2ExYmNkMzQyMTFhMWI3N2M1ODk5MjU0ZTkxMDk0YzU3Yzk1IiwiaWF0IjoxNTgzNjU3Nzc1LCJuYmYiOjE1ODM2NTc3NzUsImV4cCI6MTU4MzY2MTM3NSwic3ViIjoiIiwic2NvcGVzIjpbXX0.g40ewlW34YynSAEMrn4cBHoBQ3eJc2kbtsaS8ncBK9MKiXu8qVa5V8wVGQlq1cCqO9EGs-vRG0ud9UsqVovc3n9OPyAWDR-qt-nX1KfoAdxhKJr-rGMejzLvHxvo9y6jjX2xmxfTgOxeeloACiSkAEaLQNappHiYVCKT1Z3xAaOtvdkC27AUf8BsQsWPYlUDqWdaTJYbJshcASn-ZVhbq-knHb6_8yIuG5t8dxCCsCzgGv-pnXr6EMuB-jrgqEmMttG-JpJ_1diWf1kW5hlhLfAKvSqqHbWqS-vCSqkZoHDPx5EbxsnaquLRMemjyOi7iz8d6ZNguz9SZUB6vQadJw'
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
        pet_list = json.loads(response.content.decode('utf-8'))['animals']
        print(len(pet_list))
        insert_query = "INSERT INTO pets VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        for x in pet_list:
            c = x['colors']
            g = x['gender']
            photo_list = x['photos']
            photo = "NULL"
            if (len(photo_list) > 0):
                photo = photo_list[0]['full']
            t = x['tags']
            query_data = (count, x['name'], 2.5, g[0], 7.7, x['status'], ','.join(t), c['primary'], photo, x['coat'], breed_id, "NULL", "NULL")
            count += 1
            cursor.execute(insert_query, query_data)
    else:
        print("Failed to connect to " + api_url)


def main(argv):
    select_query = "SELECT id, name FROM breed"
    cursor.execute(select_query)
    for (breed_id, breed_name) in cursor:
        get_data(breed_id, breed_name)
    cnx.commit()
    cursor.close()
    cnx.close()
 

if __name__=="__main__":
    main(sys.argv)


