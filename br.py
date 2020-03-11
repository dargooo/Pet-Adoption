import sys
import requests
import json
import mysql.connector

# curl -d "grant_type=client_credentials&client_id=w47BEjTrqDXNg0WDEqVCpmQtiYUWaIrhmg9HenATYrbSKWFmr4&client_secret=X7KbzXt1VN8TeXTOhat6LAaGvDLmrMtwNZ3a8AyW" https://api.petfinder.com/v2/oauth2/token
api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJ3NDdCRWpUcnFEWE5nMFdERXFWQ3BtUXRpWVVXYUlyaG1nOUhlbkFUWXJiU0tXRm1yNCIsImp0aSI6IjUzY2UwZDAwOGZhNTI1NTBjMjYzOTFkOTQ3YzBmNDEzN2ZhYTEwMDM5ODc1OGU5MzQxOTFhOGFjYTZhYjllMjExYWRhNWJjYjQzMWZiZjQ5IiwiaWF0IjoxNTgzODk2NDI4LCJuYmYiOjE1ODM4OTY0MjgsImV4cCI6MTU4MzkwMDAyOCwic3ViIjoiIiwic2NvcGVzIjpbXX0.Mxn2KwexHZEUIosm8HEH5WHvfsj5Ukor5yf4n-N4zQFWBt_2_5QxgqR-TaRux34yPVYmnjAlmrbfeTyzMU2Ajt8yUPLwdCEbG6i6_dbvYEbGzT1wtteW1cMtGdY4AEB6xLeXOnT2QlHABdN4UDgcPLFJ3rsNimZqORZLPAO-rNrxIRv1cMZY69n_gBsamQEepEPljnCHvUliVboFCY6fP8-tEYPrGa96k7CFURy3-QcIjtq4BEgySZleDkMYHijCDgtCB8nc7Cw7s5PNnvqZnQtw0MFuOkssggry3yJYBZ0o0IriXanz3revet7Qy3ztJJSzyBsn1tENgj0e6zyftg'
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

def query_breeds():
    select_query = "SELECT * FROM breed"
    cursor.execute(select_query)
    result = cursor.fetchall()
    print(result)

def main(argv):
    query_breeds()
    cursor.close()
    cnx.close()
 

if __name__=="__main__":
    main(sys.argv)


