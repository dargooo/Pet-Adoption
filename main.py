from api import *
from flask import Flask, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.ext.automap import automap_base
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://coasttocoast_admin:EwFDKfkwfnyh@localhost/coasttocoast_petadoptionapp'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ms41149.@localhost/coasttocoast_petadoptionapp'
db = SQLAlchemy(app)
admin = Admin(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
species = Base.classes.species
breed = Base.classes.breed
user = Base.classes.user
pet = Base.classes.pet
posts = Base.classes.posts

admin.add_view(ModelView(species, db.session))
admin.add_view(ModelView(breed, db.session))
admin.add_view(ModelView(user, db.session))
admin.add_view(ModelView(pet, db.session))
admin.add_view(ModelView(posts, db.session))

api = Api(app)
CORS(app)
api.add_resource(Pet, '/pet')
api.add_resource(Image, '/image')
api.add_resource(PetByUser, '/pet/user/<string:username>')
api.add_resource(User, '/user')
api.add_resource(Breed, '/breed')
api.add_resource(Status, '/status')
api.add_resource(CountPet, '/count/pet')
api.add_resource(CountUser, '/count/user')

@app.route('/home')
def main():
    return render_template('home.html')

@app.route('/find')
def find():
    return render_template('find.html')

@app.route('/find-dog')
def find_dog():
    return render_template('find-dog.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/post-dog')
def post_dog():
    return render_template('post-dog.html')

if __name__ == '__main__':
    app.run()

