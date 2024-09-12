import os

from flask import (Flask, redirect, render_template, request, abort,
                   send_from_directory, url_for)

projects = [
    
    {
        "name" : "Photography in Abstract",
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
        "categories":["Landscape","Wald" , "subway" ],
        "slug": "germany-photography",
        "prod": "https://udemy.com",
    },
    {
        "name" : "India",
        "thumb": "/img/nandi_temple.png",
        "hero": "",
        "categories":["India","people", "culture"],
        "slug": "india-photography",
        "prod": "https://udemy.com",
    },
    {
        "name" : "Technology",
        "thumb": "/img/projects_main_thumb.png",
        "hero": "img/svg/habit-tracking-hero.png",
        "categories":["Programming", "Tech", "Apps"],
        "slug": "tech_projects",
        "prod": "https://github.com/kalathiln",
    },
    {
        "name" : "Shop",
        "thumb": "/img/giraffe_small.png",
        "hero": "",
        "categories":["K&K", "Ganesha", "Psylosophy"],
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

    # return render_template("project_"+slug+".html")
    return render_template(f"{slug}.html",
                            project=slug_to_project[slug])

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html") , 404
# @app.route('/')
# def index():
#    print('Request for index page received')
#    return render_template('index.html')

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

# @app.route('/hello', methods=['POST'])
# def hello():
#    name = request.form.get('name')

#    if name:
#        print('Request for hello page received with name=%s' % name)
#        return render_template('hello.html', name = name)
#    else:
#        print('Request for hello page received with no name or blank name -- redirecting')
#        return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
