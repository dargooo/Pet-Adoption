from api import *
from assets import *
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
message = Base.classes.message

admin.add_view(ModelView(species, db.session))
admin.add_view(ModelView(breed, db.session))
admin.add_view(ModelView(user, db.session))
admin.add_view(ModelView(pet, db.session))
admin.add_view(ModelView(posts, db.session))
admin.add_view(ModelView(message, db.session))

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
api.add_resource(Posts, '/posts')
api.add_resource(Reviews, '/reviews')
api.add_resource(Messages, '/messages')

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/home')
def home():
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

@app.route('/present-dog/<int:pet_id>')
def present_dog(pet_id):
    return render_template('present-dog.html', pet_id=pet_id)

@app.route('/userpage/<username>')
def user_page(username):
    return render_template('user.html', username=username)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dialogs')
def dialogs():
    return render_template('message.html')


########## user logged in ###########

@app.route('/home/login/<login>')
def home2(login):
    return render_template('home.html', login=login)

@app.route('/find/login/<login>')
def find2(login):
    return render_template('find.html', login=login)

@app.route('/find-dog/login/<login>')
def find_dog2(login):
    return render_template('find-dog.html', login=login)

@app.route('/post/login/<login>')
def post2(login):
    return render_template('post.html', login=login)

@app.route('/post-dog/login/<login>')
def post_dog2(login):
    return render_template('post-dog.html', login=login)

@app.route('/present-dog/<int:pet_id>/login/<login>')
def present_dog2(pet_id, login):
    return render_template('present-dog.html', pet_id=pet_id, login=login)

@app.route('/userpage/<username>/login/<login>')
def user_page2(username, login):
    return render_template('user.html', username=username, login=login)

@app.route('/edit-dog/<int:pet_id>/login/<login>')
def edit_dog(pet_id, login):
    return render_template('edit-dog.html', pet_id=pet_id, login=login)


if __name__ == '__main__':
    app.run()

