import sys
import requests
import json
import mysql.connector

api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJ3NDdCRWpUcnFEWE5nMFdERXFWQ3BtUXRpWVVXYUlyaG1nOUhlbkFUWXJiU0tXRm1yNCIsImp0aSI6ImQyNmIxNGYxMDIwZmYwN2I1NjMwZmFhNzNmNmNjZTlmNzc1OWMwYmQ3NWMwNDRlY2MwMTQ5OTUxMGYxNGVhYjRkNzNkMjA0MmRhNjdhZGQxIiwiaWF0IjoxNTgzNjExMjAyLCJuYmYiOjE1ODM2MTEyMDIsImV4cCI6MTU4MzYxNDgwMiwic3ViIjoiIiwic2NvcGVzIjpbXX0.Noieg1XMQrIU8GzkxCfYKERqeuPsjEKE-3TBywZ94n-fbiu1TlSg0xyaWMKc1lHCbt3V0_OpknDKmDcL7qG6prPzBmERrrIFYthHDZWqZg9wlZp-S7gJXW2RZhi4tTRYCt5VTvO_6gDDWMAearXoE0E1BjQqmUgSMvyNpjk3-lgffMKSaAw4pcw1H3aGQtBtClo_xBMzRJ0Oj3HzoNq5CF8RRuRLk9UPpxE3ULtcjKF9d0yl0-vQhiz9twcCRJJR9hkQRUd1MCuudxAws-f4YPGUD-q7cGSvUKeozRlqVySbCwSF_4FdTt16m_3eE9lPld2yL8DPFvEXZqD83NoPrA'
api_url_base = 'https://api.petfinder.com/v2'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}
species = ['dog', 'cat']

cnx = mysql.connector.connect(user='coasttocoast_yijun', password='sql41149.',
                                host='localhost', database='coasttocoast_petadoptionapp')
cursor = cnx.cursor()


def get_json(i):
    x = species[i]
    api_url = api_url_base + '/types/%s/breeds' % x
    print(api_url)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        breed_list = json.loads(response.content.decode('utf-8'))['breeds']
        insert_query = "INSERT INTO breed VALUES (%s, %s, %s)"
        index = 1
        for x in breed_list:
            query_data = (++index, i, x['name'])
            cursor.execute(insert_query, query_data)
        cnx.commit()
        cursor.close()
        cnx.close()
    else:
        return None


def main(argv):
    for x in range(1, len(species) + 1):
        get_json(x)
main(sys.argv)


