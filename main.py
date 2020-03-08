from flask import Flask, abort
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:EwFDKfkwfnyh@localhost/coasttocoast_petadoptionapp'
db = SQLAlchemy(app)
admin = Admin(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
species = Base.classes.species
breed = Base.classes.breed
user = Base.classes.user
pets = Base.classes.pets
posts = Base.classes.posts

admin.add_view(ModelView(species, db.session))
admin.add_view(ModelView(breed, db.session))
admin.add_view(ModelView(user, db.session))
admin.add_view(ModelView(pets, db.session))
admin.add_view(ModelView(posts, db.session))

@app.route('/')
def main():
    abort(403)

if __name__ == '__main__':
    app.run()