from flask import Flask
from flask import render_template
from flask import request
from random import randint
from flask import redirect

# Create the app
app = Flask(__name__)

# home page - loading a static page
@app.get("/")
def home():
    return render_template('pages/home.jinja')

# about page - loading a static page
@app.get("/about/")
def about():
    return render_template('pages/about.jinja')

# ----------------------------------------------------
#  random number page - passing a value into template
@app.get("/random/")
def random():
    randNum = randint(1, 1000000000000000)
    return render_template('pages/random.jinja', number=randNum)
# -----------------------------------------------------
# number - getting a value from route
#          and passing it on template
@app.get("/number/<int:num>")
def analyseNumber(num):
    print(f"You entered: {num}")
    return render_template('pages/number.jinja', number=num)


# ---------------------------------------------------
# Form page - static page with form!
@app.get("/form/")
def form():
    return render_template('pages/form.jinja')



@app.post("/processForm")
def processForm():
    print(f"Form data: $ {request.form}")
    return render_template(
        "pages/formData.jinja",
         name = request.form["name"],
         age = request.form["age"]
    )


@app.errorhandler(404)
def notfound(e):
    return render_template('pages/404.jinja')