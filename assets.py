from flask_assets import Bundle, Environment
from main import app

bundles = {
    'search_js': Bundle(
        'js/search.js',
        output='gen/search.js'),
    'present_css': Bundle(
        'css/present.css',
        output='gen/present.css'),
    'present_js': Bundle(
        'js/present.js',
        output='gen/present.js')
}

assets = Environment(app)
assets.register(bundles)
