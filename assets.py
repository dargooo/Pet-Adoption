from flask_assets import Bundle, Environment
from main import app

bundles = {
    'img': Bundle(
        'img',
        output='gen/img'),
    'login_css': Bundle(
        'css/login.css',
        output='gen/login.css'),
    'login_js': Bundle(
        'js/login.js',
        output='gen/login.js'),
    'post_js': Bundle(
        'js/post.js',
        output='gen/post.js'),
    'search_js': Bundle(
        'js/search.js',
        output='gen/search.js'),
    'present_css': Bundle(
        'css/present.css',
        output='gen/present.css'),
    'present_js': Bundle(
        'js/present.js',
        output='gen/present.js'),
    'user_css': Bundle(
        'css/user.css',
        output='gen/user.css'),
    'user_js': Bundle(
        'js/user.js',
        output='gen/user.js')
}

assets = Environment(app)
assets.register(bundles)
