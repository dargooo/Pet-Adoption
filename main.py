from api import *
from flask import Flask, abort
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://coasttocoast_admin:EwFDKfkwfnyh@localhost/coasttocoast_petadoptionapp'
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
api.add_resource(Pet, '/pet')
api.add_resource(User, '/user')
api.add_resource(Breed, '/breed')
api.add_resource(Status, '/status')

@app.route('/')
def main():
    abort(403)

if __name__ == '__main__':
    app.run()

