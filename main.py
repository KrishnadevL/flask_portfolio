# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")

@app.route('/krish/')
def krish():
    return render_template("KrishL.html")

@app.route('/sam/')
def sam():
    return render_template("sam.html")

@app.route('/kamryn/')
def kamryn():
    return render_template("kamryn.html")

@app.route('/div/')
def div():
    return render_template("div.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
