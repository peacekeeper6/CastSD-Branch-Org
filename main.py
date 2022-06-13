import markdown
from flask import render_template
from __init__ import app
from flask_login import current_user
from usercrud.query import user_by_id

from usercrud.app_crud import app_crud

app.register_blueprint(app_crud)

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("layouts/index.html")

@app.route('/aboutkoinonia')
def aboutkoinonia():
    return render_template("aboutus/aboutkoinonia.html")

@app.route('/getinvolved')
def getinvolved():
    return render_template("getinvolved.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.errorhandler(404)
def error(e):
    return render_template("404.html"), 404

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
