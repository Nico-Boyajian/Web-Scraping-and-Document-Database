from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
import mars_scrape
import os

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")

@app.route("/")
def home():
    mars_info = mongo.db.mars_info.find_one()
    
    return render_template("index.html", mars_info=mars_info)

@app.route("/scrape")
def scrape():

    mars_info = mongo.db.mars_info

    mars_data = mars_scrape.scrape_mars_news()
    mars_data = mars_scrape.scrape_mars_image()
    mars_data = mars_scrape.scrape_mars_weather()
    mars_data = mars_scrape.scrape_mars_facts()
    mars_data = mars_scrape.scrape_mars_hems()
    
    mars_info.update({}, mars_data, upsert=True)

    return redirect("/", code=302)





if __name__ == "__main__":
    app.run(debug=True)