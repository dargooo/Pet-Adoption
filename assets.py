from flask_assets import Bundle, Environment
from main import app

bundles = {
    'present_css': Bundle(
        'css/present.css',
        output='gen/present.css')
}

assets = Environment(app)
assets.register(bundles)
