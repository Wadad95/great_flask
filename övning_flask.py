from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
    return render_template("homepage.html",title=homepage, test="Hello A")

@skills_app.route("/about")
def about():
    return render_template("about.html", pagettle="About Us", test="Hello B")


if __name__=="__main__":
    skills_app.run()
