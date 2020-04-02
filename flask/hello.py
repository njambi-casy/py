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


#This funcion passes an ordinary html file in templates
#@app.route("/1")
#def html():
#    return render_template("index.html")



#This function passes a variable contained in the index.html file that is defined in python
@app.route("/2")
def variable():
    headline = "Breaking News"#givin the variable headline a value
    return render_template("index.html", headline=headline)
    #first headline is the variable declared in the index.html file with double curly braces

@app.route("/3")
def happiness():
    headline = "Be happy"#givin the variable headline a value
    return render_template("index.html", headline=headline)
