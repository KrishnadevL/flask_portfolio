# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render Trending.html
@app.route('/Trending/')
def Trending():
    return render_template("Trending.html")


@app.route('/Tv Shows/')
def Walruses ():
    return render_template("Walruses.html")


@app.route('/Movies/')
def Movies():
    return render_template("Movies.html")


@app.route('/Binary/')
def Binary():
    return render_template("Binary.html")


@app.route('/m_lab/')
def m_lab():
    return render_template("m_lab.html")


@app.route('/sam_abt/')
def sam_abt():
    return render_template("sam_abt.html")

@app.route('/kamryn_abt/')
def kamryn_abt():
    return render_template("kamryn_abt.html")

# Defining the Greet function for the Greet Minilab
@app.route('/krishL/', methods=['GET', 'POST'])
def krish():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("krishL.html", name=name)
    # starting and empty input default
    return render_template("krishL.html", name="World")


@app.route('/sam/', methods=['GET', 'POST'])
def sam():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("sam.html", name=name)
    # starting and empty input default
    return render_template("sam.html", name="World")


@app.route('/kamryn/', methods=['GET', 'POST'])
def kamryn():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("kamryn.html", name=name)
    # starting and empty input default
    return render_template("kamryn.html", name="World")


@app.route('/div/', methods=['GET', 'POST'])
def div():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("div.html", name=name)
    # starting and empty input default
    return render_template("div.html", name="World")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)

