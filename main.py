# import "packages" from flask
from flask import Flask, render_template, request
from algorithms.image import image_data
from api.webapi import api_bp
# create a Flask instance
app = Flask(__name__)

@app.route('/rgb/', methods=["GET", "POST"])
def rgb():
    rawList = image_data()
    colorList = []
    grayList = []
    for img in rawList:
        colorList.append(img['base64'])
        grayList.append(img['base64_GRAY'])

    return render_template('rgb.html', images=rawList, colored=colorList, grayed=grayList)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render Trending.html
@app.route('/Trending/')
def Trending():
    return render_template("Trending.html")


@app.route('/Walruses/')
def Walruses ():
    return render_template("Walruses.html")


@app.route('/Movies/')
def Movies():
    return render_template("Movies.html")

@app.route('/logic_gates/')
def logic_gates():
    return render_template("logic_gates.html")

@app.route('/Binary/', methods=['GET', 'POST'])
def Binary():
    if request.form:
        bit_size_k = request.form.get("bit_size_k")
        if len(bit_size_k) != 0:  # input field has content
            return render_template("Binary.html", bit_size_k=int(bit_size_k))
    # starting and empty input default
    return render_template("Binary.html", bit_size_k=8)

@app.route('/m_lab/')
def m_lab():
    return render_template("m_lab.html")

@app.route('/krish_abt/')
def krish_abt():
    return render_template("krish_abt.html")

@app.route('/krish_alt/')
def krish_alt():
    return render_template("krish_alt.html")

@app.route('/sam_abt/')
def sam_abt():
    return render_template("sam_abt.html")

@app.route('/kamryn_abt/')
def kamryn_abt():
    return render_template("kamryn_abt.html")

@app.route('/comments/')
def comments():
    attrib_names = [
        {'labelName': "Movie:", "textAreaName": "movie", "placeholderName": "Title", "rows": "1", "cols": "32"},
        {'labelName': "Rating:", "textAreaName": "rating", "placeholderName": "1-5", "rows": "1", "cols": "32"},
        {'labelName': "Comment:", "textAreaName": "comment", "placeholderName": "Review!", "rows": "10", "cols": "32"},
    ]
    return render_template("comments.html", attrib_names=attrib_names)


@app.route('/div_abt/')
def div_abt():
    return render_template("div_abt.html")

# Defining the Greet function for the Greet Minilab
@app.route('/krishL/', methods=['GET', 'POST'])
def krish():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("krishL.html", name=name)
    # starting and empty input default
    return render_template("krishL.html", name="World")

@app.route('/video0/')
def video0():
    return render_template("video0.html")

@app.route('/Binary_math/', methods=['GET', 'POST'])
def Binary_math():
    if request.form:
        bit_size_k = request.form.get("bit_size_k")
        if len(bit_size_k) != 0:  # input field has content
            return render_template("Binary_math.html", bit_size_k=int(bit_size_k))
    # starting and empty input default
    return render_template("Binary_math.html", bit_size_k=8)

@app.route('/Binary_signed/', methods=['GET', 'POST'])
def Binary_signed():
    if request.form:
        bit_size_k = request.form.get("bit_size_k")
        if len(bit_size_k) != 0:  # input field has content
            return render_template("Binary_signed.html", bit_size_k=int(bit_size_k))
    # starting and empty input default
    return render_template("Binary_signed.html", bit_size_k=8)

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

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("login.html", name=name)
    # starting and empty input default
    return render_template("login.html", name="World")


@app.route('/div/', methods=['GET', 'POST'])
def div():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("div.html", name=name)
    # starting and empty input default
    return render_template("div.html", name="World")

@app.route('/sam_binary/', methods=['GET', 'POST'])
def sam_binary():
        if request.form:
            bit_size_s = request.form.get("bit_size_s")
            if len(bit_size_s) != 0:  # input field has content
                return render_template("sam_binary.html", bit_size_s=int(bit_size_s))
        # starting and empty input default
        return render_template("sam_binary.html", bit_size_s=8)



@app.route('/div_binary/', methods=['GET', 'POST'])
def div_binary():
    if request.form:
        bit_size_d = request.form.get("bit_size_d")
        if len(bit_size_d) != 0:  # input field has content
            return render_template("div_binary.html", bit_size_d=int(bit_size_d))
    # starting and empty input default
    return render_template("div_binary.html", bit_size_d=8)

@app.route('/joke/', methods=['GET', 'POST'])
def joke():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/joke"
    """
    url = "http://localhost:5000/api/joke"
    response = requests.request("GET", url)
    return render_template("joke.html", joke=response.json())

app.register_blueprint(api_bp)

@app.route('/colorcodes/', methods=['GET', 'POST'])
def colorcodes():
    # submit button has been pushed
    if request.form:
        bit_size_3 = request.form.get("bit_size_3")
        if len(bit_size_3) != 0:  # input field has content
            return render_template("colorcodes.html", bit_size_3=int(bit_size_3))
    # starting and empty input default
    return render_template("colorcodes.html", bit_size_3=8)


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)

