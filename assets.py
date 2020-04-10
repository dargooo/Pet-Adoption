from flask_assets import Bundle, Environment
from main import app

bundles = {
    'img': Bundle(
        'img',
        output='gen/img'),
    'css': Bundle(
        'css',
        output='gen/css'),
    'js': Bundle(
        'js',
        output='gen/js')
}

assets = Environment(app)
assets.register(bundles)
