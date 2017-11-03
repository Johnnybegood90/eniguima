from flask import Flask , render_template , request , redirect 
import os 

#import rethinkdb as r 


app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
app.config.update(
    DEBUG=False,
    TEMPLATES_AUTO_RELOAD=True
)
@app.route("/test")
def test():
    return render_template("test.html")
@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html" , header=render_template("header.html"))
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")
@app.route("/public")
def public():
    return render_template("publique.html")
@app.errorhandler(500)
def page_error(error): 
    return render_template("500.html")
@app.route("/login" , methods=["POST"])
def connexion():
    if request.form["password"] == "admin":
        return redirect("/staff" , code=302)
    elif request.form["password"] == "team": 
        return redirect("/team" , code=302)
@app.route("/team")
def teampanel():
    return render_template("team.html")
@app.route("/staff")
def staffpanel():
    return render_template("staff.html")
@app.route("/error")
def error_make():
    return fakevariable
app.run()
