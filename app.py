import os

from flask import (Flask, redirect, render_template, request, abort,
                   send_from_directory, url_for)

projects = [
    
    {
        "name" : "Abstract",
        "thumb": "/img/headshot.png",
        "hero": "",
        "categories":["Abstract","Portrait", "Landscape"],
        "slug": "abstract-photography",
        "prod": "https://udemy.com",
    },
    {
        "name" : "Germany",
        "thumb": "/img/germany_subway.png",
        "hero": "",
        "categories":["Deutschland","Berlin", "Darmstadt"],
        "slug": "germany-photography",
        "prod": "https://udemy.com",
    },
    {
        "name" : "India",
        "thumb": "/img/nandi_temple.png",
        "hero": "",
        "categories":["Culture","Colours","People"],
        "slug": "india-photography",
        "prod": "https://udemy.com",
    },
    {
        "name" : "Technology",
        "thumb": "/img/projects_main_thumb.png",
        "hero": "img/svg/habit-tracking-hero.png",
        "categories":["Programming"],
        "slug": "tech_projects",
        "prod": "https://github.com/kalathiln/msdocs-python-flask-webapp-quickstart",
    },
    {
        "name" : "Shop",
        "thumb": "/img/giraffe_small.png",
        "hero": "",
        "categories":["The K&K Psylosophy"],
        "slug": "myshop",
        "prod": "https://www.redbubble.com/de/people/KremserKalathil/shop?asc=u",
    }

]

slug_to_project = {project["slug"]:project for project in projects}

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"] )
def home():
    return render_template("home.html", projects = projects)

@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"{slug}.html",
                            project=slug_to_project[slug])

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html") , 404

if __name__ == '__main__':
   app.run()
