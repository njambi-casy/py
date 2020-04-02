from flask import Flask, render_template


app = Flask(__name__)
#app.config.from_envvar('APP_SETTINGS')

@app.route("/")
def index():
    return "Hello world!"

#This route returns a greeting with a customizes value of name which has been passed from the url
#@app.route("/<string:name>")
#def default(name):
    #name = request.form.post(name)
#    return f"<h1>Hey, {name}</h1>"

@app.route("/1")
def html():
    return render_template("index.html")
