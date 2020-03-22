from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from datetime import datetime
import mysql.connector
import json

app = Flask(__name__)
api = Api(app)
try:
    cnx = mysql.connector.connect(user='root', password='Ms41149.',
#    cnx = mysql.connector.connect(user='coasttocoast_yijun', password='sql41149.',
                                  host='localhost', database='coasttocoast_petadoptionapp')
    cursor = cnx.cursor()
except: print("Log in mysql db failed!")

# convert mysql result to json
def sql_2_json(cursor):
    fields = [x[0] for x in cursor.description]
    result = cursor.fetchall()
    json_data = []
    for row in result:
        json_data.append(dict(zip(fields, row)))
    return jsonify(json_data)


###########################  Pet  ###########################
class Pet(Resource):
    def get(self):
        # | id | name | age | gender | weight | adopt_status | personality | color | image | hair | breed_id | adopt_user | adopt_time |
        parser = reqparse.RequestParser()
        parser.add_argument('min_age',     type=float)
        parser.add_argument('max_age',     type=float)
        parser.add_argument('gender',      type=str)
        parser.add_argument('personality', type=str)
        parser.add_argument('color',       type=str)
        parser.add_argument('hair',        type=str)
        parser.add_argument('breed_id',    type=int)
        args = parser.parse_args()
        print(args)

        query = "SELECT * FROM pet"
        where = " WHERE "
        if args['min_age']:
            print(str(args['min_age']))
            query = query + where + "age >= " + str(args['min_age'])
            where = " AND "
        if args['max_age']:
            query = query + where + "age <= " + str(args['max_age'])
            where = " AND "
        if args['gender']:
            query = query + where + "gender = \'" + args['gender'] + "\'"
            where = " AND "
        if args['personality']:
            query = query + where + "personality IN (" + args['personality'] + ")"
            where = " AND "
        if args['color']:
            query = query + where + "color = \'" + args['color'] + "\'"
            where = " AND "
        if args['hair']:
            query = query + where + "hair = \'" + args['hair'] + "\'"
            where = " AND "
        if args['breed_id']:
            query = query + where + "breed_id = " + str(args['breed_id'])
            where = " AND "

        print(query)
        cursor.execute(query)
        return sql_2_json(cursor)


    def post(self):
        # | id | name | age | gender | weight | adopt_status | personality | color | image | hair | breed_id | adopt_user | adopt_time |
        parser = reqparse.RequestParser()
        parser.add_argument('name',        type=str,   required=True)
        parser.add_argument('age',         type=float, required=True)
        parser.add_argument('gender',      type=str,   required=True)
        parser.add_argument('weight',      type=float, required=True)
        parser.add_argument('personality', type=str)
        parser.add_argument('color',       type=str,   required=True)
        parser.add_argument('image',       type=str)
        parser.add_argument('hair',        type=str,   required=True)
        parser.add_argument('breed_id',    type=int,   required=True)
        # | pet_id | username | title | open_time | close_time | description |
        parser.add_argument('username',    type=str,   required=True)
        parser.add_argument('title',       type=str,   required=True)
        parser.add_argument('description', type=str,   default='No description')
        args = parser.parse_args()
        print(args)

        # insert into pet table
        cursor.execute("SELECT MAX(id) FROM pet")
        pet_id      = cursor.fetchone()[0] + 1
        insert_query = "INSERT INTO pet VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        query_data = (pet_id, args['name'], args['age'], args['gender'], args['weight'], 'adoptable', args['personality'], args['color'], args['image'], args['hair'], args['breed_id'], None, None)
        cursor.execute(insert_query, query_data)

        # insert into posts table
        open_time   = str(datetime.now()).split('.')[0]
        insert_query = "INSERT INTO posts VALUES (%s, %s, %s, %s, %s, %s)"
        query_data = (pet_id, args['username'], args['title'], open_time, None, args['description'])
        cursor.execute(insert_query, query_data)
        cnx.commit()
###########################  Pet  ###########################

########################### User  ###########################
class User(Resource):
    def get(self):
        # | username | password | name | avatar | email | address | zipcode | is_person |
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        args = parser.parse_args()
        cursor.execute("SELECT * FROM user WHERE username=" + args['username'])
        return sql_2_json(cursor)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',  type=str, required=True)
        parser.add_argument('password',  type=str, required=True)
        parser.add_argument('name',      type=str, required=True)
        parser.add_argument('avatar',    type=str, required=True)
        parser.add_argument('email',     type=str, required=True)
        parser.add_argument('address',   type=str)
        parser.add_argument('zipcode',   type=int, required=True)
        parser.add_argument('is_person', type=bool, required=True)
        args = parser.parse_args()
        insert_query = "INSERT INTO user VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        query_data = (args['username'], args['password'], args['name'], args['avatar'], args['email'], args['address'], args['zipcode'], args['is_person'])
        cursor.execute(insert_query, query_data)
        cnx.commit()
########################### User  ###########################

########################### Breed ###########################
class Breed(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('species_id', type=int, required=True)
        args = parser.parse_args()
        cursor.execute("SELECT * FROM breed WHERE species_id=" + str(args['species_id']))
        return sql_2_json(cursor)

    def post(self):
        # | id | species_id | name |
        parser = reqparse.RequestParser()
        parser.add_argument('species_id', type=int, required=True)
        parser.add_argument('breed',      type=str, required=True)
        args = parser.parse_args()

        cursor.execute("SELECT MAX(id) FROM breed")
        breed_id      = cursor.fetchone()[0] + 1
        insert_query = "INSERT INTO breed VALUES (%s, %s, %s)"
        query_data = (breed_id, args['species_id'], args['breed'])
        cursor.execute(insert_query, query_data)
        cnx.commit()
########################### Breed  ###########################

########################### Status ###########################
class Status(Resource):
    def put(self):
        # | id | name | age | gender | weight | adopt_status | personality | color | image | hair | breed_id | adopt_user | adopt_time |
        # | pet_id | username | title | open_time | close_time | description |
        parser = reqparse.RequestParser()
        parser.add_argument('pet_id',     type=int, required=True)
        parser.add_argument('status',     type=str, required=True)
        parser.add_argument('adopt_user', type=str)
        args = parser.parse_args()

        cursor.execute("UPDATE pet SET adopt_status = \'" + args['status'] + "\' WHERE id = " + str(args['pet_id']))
        if args['status'] == 'adopted':
            cur_time = str(datetime.now()).split('.')[0]
            cursor.execute("UPDATE pet SET adopt_user = \'" + args['adopt_user'] + "\', adopt_time = \'" + cur_time + "\' WHERE id = " + str(args['pet_id']))
            cursor.execute("UPDATE posts SET close_time = \'" + cur_time + "\' WHERE pet_id = " + str(args['pet_id']))
        cnx.commit()
########################### Status ###########################



api.add_resource(Pet, '/pet')
api.add_resource(User, '/user')
api.add_resource(Breed, '/breed')
api.add_resource(Status, '/status')

if __name__ == '__main__':
    app.run(debug=True)
