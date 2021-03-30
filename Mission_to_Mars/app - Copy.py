import pymongo
from flask import Flask, render_template, redirect
from scrape_mars import scrape

# Create an instance of Flask
app = Flask(__name__)

# Use pymongo to establish Mongo connection
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.mars_app
collection = db.mars_scraped_data

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars = collection.find()

    # Return template and data
    return render_template('index.html', mars=mars)


# Route that will trigger the scrape function
# @app.route("/scrape")
# def scrape_all():

#     # Run the scrape function
#     mars = scrape()
#     collection.drop()
#     # Update the Mongo database using update and upsert=True
#     collection.insert_one(mars)

#     # Redirect back to home page
#     return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
