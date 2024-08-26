import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def check_administrator(current_user):
    is_administrator = mongo.db.users.find_one({"username": current_user})
    return is_administrator["administrator"]


@app.route("/")
@app.route("/index")
def index():
    posts = list(mongo.db.posts.find({}).sort("_id", -1).limit(2))
    return render_template("index.html", posts=posts)


@app.route("/get_posts")
def get_posts():
    posts = list(mongo.db.posts.find())
    return render_template("posts.html", posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "administrator": "no"
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("get_posts"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if hashed password is equal to inputted password
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                if session["user"]:
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for("index"))
            else:
                # password does not match
                flash("Incorrect Username or Password")
                return redirect(url_for("login"))

        else:
            # username does not exist in database
            flash("Incorrect Username or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for('login'))


@app.route("/add_post", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        post = {
            "post_title": request.form.get("post_title"),
            "category_name": request.form.get("category_name"),
            "artist_name": request.form.get("artist_name"),
            "venue": request.form.get("venue"),
            "concert_date": request.form.get("concert_date"),
            "favourite_song": request.form.get("favourite_song"),
            "post_description": request.form.get("post_description"),
            "created_by": session["user"],
            "post_image": request.form.get("post_image")
        }
        mongo.db.posts.insert_one(post)
        flash("Post Successfully Added")
        return redirect(url_for("get_posts"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_post.html", categories=categories)


@app.route("/edit_post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    if request.method == "POST":
        submit_post = { "$set": {
            "post_title": request.form.get("post_title"),
            "category_name": request.form.get("category_name"),
            "artist_name": request.form.get("artist_name"),
            "venue": request.form.get("venue"),
            "concert_date": request.form.get("concert_date"),
            "favourite_song": request.form.get("favourite_song"),
            "post_description": request.form.get("post_description"),
            "created_by": session["user"],
            "post_image": request.form.get("post_image")
        }}
        mongo.db.posts.update_one({"_id": ObjectId(post_id)}, submit_post)
        flash("Post Edited Successfully")
        return redirect(url_for("get_posts"))

    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_post.html", post=post, categories=categories)


@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    mongo.db.posts.delete_one({"_id": ObjectId(post_id)})
    flash("Post Deleted Successfully")
    return redirect(url_for("get_posts"))


@app.route("/display_post/<post_id>")
def display_post(post_id):
    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template("display_post.html", post=post)


@app.route("/get_categories")
def get_categories():
    admin = ""
    current_user = session.get('user')
    if current_user:
        admin = check_administrator(current_user)
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories, admin=admin)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    current_user = session.get('user')
    if current_user:
        admin = check_administrator(current_user)
        if admin == "yes":
            if request.method == "POST":
                category = {
                    "category_name": request.form.get("category_name")
                }
                mongo.db.categories.insert_one(category)
                flash("Category Added Successfully")
                return redirect(url_for("get_categories"))
            return render_template("add_category.html")
        return redirect(url_for("get_posts"))
    return redirect(url_for("login"))


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    current_user = session.get('user')
    if current_user:
        admin = check_administrator(current_user)
        if admin == "yes":
            if request.method == "POST":
                submit_category = { "$set": {
                    "category_name": request.form.get("category_name")
                }}
                mongo.db.categories.update_one({"_id": ObjectId(category_id)}, submit_category)
                flash("Category Edited Successfully")
                return redirect(url_for("get_categories"))

            category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
            return render_template("edit_category.html", category=category)
        return redirect(url_for("get_posts"))
    return redirect(url_for("login"))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    current_user = session.get('user')
    if current_user:
        admin = check_administrator(current_user)
        if admin == "yes":
            mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
            flash("Category Deleted Successfully")
            return redirect(url_for("get_categories"))
        return redirect(url_for("get_posts"))
    return redirect(url_for("login"))


@app.route("/get_posts_by_category/<category_name>")
def get_posts_by_category(category_name):
    posts = list(mongo.db.posts.find({"category_name": category_name}))
    return render_template("posts.html", posts=posts, category_name=category_name)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
