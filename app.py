import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.errors import InvalidId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("This COOKIO! username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if the username it already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure that hashed password is matching  input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("The Username and/or Password are incorrect")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("The Username and/or Password are incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    user = mongo.db.users.find_one(
        {"username": session["user"]})

    if request.method == "POST":
        user["first_name"] = request.form.get("first_name")
        user["last_name"] = request.form.get("last_name")
        user["date_of_birth"] = request.form.get("date_of_birth")

        mongo.db.users.update({"_id": user["_id"]}, user)
        flash("Your Profile has been Updated!")

    first_name = user.get("first_name", "")
    last_name = user.get("last_name", "")
    date_of_birth = user.get("date_of_birth", "")

    if session["user"]:
        return render_template("profile.html", username=user["username"],
                               first_name=first_name, last_name=last_name,
                               date_of_birth=date_of_birth)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove the user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        is_vegetarian = "on" if request.form.get("is_vegetarian") else "off"
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "is_vegetarian": is_vegetarian,
            "created_by": session.get("user")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Your Cookio has been added!")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        is_vegetarian = "on" if request.form.get("is_vegetarian") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "is_vegetarian": is_vegetarian,
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Your Cookio has been Updated!")
    try:
        recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    except InvalidId:
        return render_template("404.html")

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):

    try:
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    except Exception:
        return render_template("404.html")

    flash("Recipe successfully deleted")
    return redirect(url_for("get_recipes"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("Category Added!")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Updated")
        return redirect(url_for("get_categories"))

    try:
        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    except InvalidId:
        return render_template("404.html")
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    try:
        mongo.db.categories.remove({"_id": ObjectId(category_id)})
    except Exception:
        return render_template("404.html")

    flash("Category Removed")
    return redirect(url_for("get_categories"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "127.0.0.1"),
            port=int(os.environ.get("PORT", 3000)),
            debug=False)
