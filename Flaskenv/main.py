# import markdown
from flask import Flask
from flask import render_template
# from __init__ import app
# from flask_login import current_user
# from usercrud.query import user_by_id

# from usercrud.app_crud import app_crud

# app.register_blueprint(app_crud)

# create a Flask instance
app = Flask(__name__)

# this is a test i am not used to vs code

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("layouts/index.html")


@app.route('/aboutelimin8')
def aboutelimin8():
    return render_template("aboutus/aboutelimin8.html")


@app.route('/partners')
def partners():
    return render_template("aboutus/partners.html")

    
@app.route('/founders')
def founders():
    return render_template("aboutus/founders.html")


@app.route('/getinvolved')
def getinvolved():
    return render_template("getinvolved/getinvolved.html")


@app.route('/login')
def login():
    return render_template("getinvolved/login.html")


@app.route('/register')
def register():
    return render_template("getinvolved/register.html")


@app.route('/donation/')
def donation():
    return render_template("donation.html")


@app.route('/contact/')
def contact():
    return render_template("contact.html")


@app.errorhandler(404)
def error(e):
    return render_template("404.html"), 404


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
