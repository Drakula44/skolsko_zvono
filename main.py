from flask import Flask
from flask import render_template
from flask_assets import Environment, Bundle

bundles = {

    'raspored_js': Bundle(
        'scripts/addNew.js',
        'scripts/jquery-3.6.0.min.js',
        output='gen/home.js',
        filters='jsmin'),

    'raspored_css': Bundle(
        'styles/raspored.css',
        output='gen/home.css',
        filters='cssmin'),
}

app = Flask(__name__)
assets = Environment(app)
assets.register(bundles)

days_in_week = ['Ponedeljak','Utorak','Sreda','Četvrtak','Petak','Subota','Nedelja']

@app.route('/raspored')
def hello_world():
    name = 'Nikola'
    return render_template('raspored.html',name=name,raspored=[[1,2,3],[4,5,6],[7,8,9]],diw=days_in_week)

@app.route('/')
def main():
    return 'Hello, World!'