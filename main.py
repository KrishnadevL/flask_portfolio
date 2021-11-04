# import "packages" from flask
from flask import Flask, render_template, request, redirect, url_for
from algorithms.image import image_data
import random
import requests
import pickle
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

@app.route('/netflix/')
def netflix():
    return render_template("netflix.html")

@app.route('/hulu/')
def hulu():
    return render_template("hulu.html")


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

@app.route('/review/')
def review():
    return render_template("review.html")

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

@app.route('/login/', methods=['GET', 'POST'])
def login():
    #kdf = open('KammyDebug.txt', 'wt+')
    if request.form:
        username = request.form.get("username")
        password = request.form.get("password")

    passwordsFilePathName = 'passwords.bin'
    filePwd = open(passwordsFilePathName, 'rb+')
    filePwd.seek(0)

    AllowAccess = False
    try:
        # If this is first time (i.e. empty file), then will generate exception
        # and create the file.
        userDatabase = pickle.load(filePwd)

        for curUser in userDatabase:
            if curUser['username'] == username:
                # Username found,... now check password
                if curUser['password'] == password:
                    AllowAccess = True
                    break

        if not AllowAccess:
            # If not match was found, ask user to add new credentials to list
            userDatabase.append({'username':username, 'password':password})
            filePwd.seek(0)
            pickle.dump(userDatabase, filePwd)
    except:
        # Create new database here, as empty list
        userDatabase = []
        pickle.dump(userDatabase, filePwd)

    filePwd.close()


    if AllowAccess:
        #kdf.writelines('Allowing Access...\n')
        #kdf.close()
        #return redirect("/comments",)
        return redirect(url_for('.comments', user_name=username))
        #return redirect(request.referrer)
    else:
        #kdf.close()
        return render_template("login.html", pwFilePathName=passwordsFilePathName)

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

@app.route('/mov_rand/', methods=['GET', 'POST'])
def mov_rand():
    if request.form:
        genre_choice = request.form.get("genre_choice")
        if len(genre_choice) != 0:  # input field has content
            genre = str(genre_choice).capitalize()

            # Link to public API, gets movie data by genre
            url = ("https://data-imdb1.p.rapidapi.com/movie/byGen/"+ genre +"/")

            querystring = {"page_size":"50"}

            headers = {
                'x-rapidapi-host': "data-imdb1.p.rapidapi.com",
                'x-rapidapi-key': "b399060d5cmshdde5a342e03dbfap1a4d84jsn99009368a5f2"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)
            # Pulls results form data to then be sorted
            movie_list = []
            results = response.json().get('results')
            # determines if there is a value within the list
            if len(results) == 0:
                movie_list.append("Sorry, it looks like there arent any movies in that genre. "
                                  "Maybe check your spelling or try another one")
            else:
                for movie in results:
                    test = movie["title"]
                    movie_list.append(test)
            # randomly selects a movie for the generator
            movie_choice = random.choice(movie_list)
            print(movie_list)
            return render_template("mov_rand.html", movie_choice=movie_choice)
    return render_template("mov_rand.html", movie_choice="Enter a genre!")

@app.route('/famous_icons/', methods=['GET', 'POST'])
def famous_icons():
    if request.form:
        mov_star_name = request.form.get("mov_star_name")
        if len(mov_star_name) != 0:  # input field has content
            star_name = str(mov_star_name).capitalize()

            # Link to public API, gets movie data by genre
            url = ("https://data-imdb1.p.rapidapi.com/actor/imdb_id_byName/" + star_name + "/")

            querystring = {"page_size":"150"}

            headers = {
                'x-rapidapi-host': "data-imdb1.p.rapidapi.com",
                'x-rapidapi-key': "b399060d5cmshdde5a342e03dbfap1a4d84jsn99009368a5f2"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)
            # Pulls results form data to then be sorted
            movie_list = []
            results = response.json().get('results')
            # determines if there is a value within the list
            if len(results) == 0:#no star found if user enters name
                movie_choice = "Sorry, it looks like there arent any movie actor with that name." \
                               "Maybe check your spelling or try another one"
            elif len(results) > 1: #multiple stars found with that name
                star_name = []
                movie_choice = "Multiple star found with the name entered."\
                               "Please enter full name of one of the Star."
                for movie in results:
                    temp = movie["name"]
                    star_name.append(temp)
                movie_choice += ",".join(star_name)
            else:
                for id in results:
                    star_imbd_id = id["imdb_id"]
                star_movie_url = ("https://data-imdb1.p.rapidapi.com/actor/id/" + star_imbd_id + "/movies_knownFor/")
                response_movies = requests.request("GET", star_movie_url, headers=headers, params=querystring)
                results_movies = response_movies.json().get('results')
                for movie in results_movies:
                    temp = movie[0]["title"]
                    movie_list.append(temp)
                movie_choice = "List of Movies for " + star_name + ": " + ", ".join(movie_list)


            print(response.text)
            return render_template("famous_icons.html", movie_choice=movie_choice)
    return render_template("famous_icons.html", movie_choice="Enter a Famous actor or actress!")



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

