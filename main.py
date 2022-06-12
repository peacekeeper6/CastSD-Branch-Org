# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("layouts/index.html")

@app.route('/ourstatement/')
def ourstatement():
    return render_template("ourstatement.html")

# @app.route('/getinvolved/')
# def getinvolved():
#     return render_template("getinvolved.html")

@app.errorhandler(404)
def error(e):
    return render_template("404.html"), 404

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
