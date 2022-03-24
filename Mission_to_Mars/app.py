from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Use flask_pymongo to set up mongo connection
app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# # route
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()

    return render_template("index.html", mars = mars)

@app.route("/scrape")
def scrape():
    
    mars = mongo.db.mars
    mars_all = scrape_mars.scrape()
    mars.update({}, mars_all, upsert=True)
    

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)