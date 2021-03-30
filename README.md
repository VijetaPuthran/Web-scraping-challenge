# Web-scraping-challenge

![mission_to_mars](Images/Mission_to_mars.jpg)


The assignment involves building a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. Thetask includes the following steps:


## Step 1 - Scraping

The initial scraping is conducted using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* A Jupyter Notebook file called `mission_to_mars.ipynb` is created and is used to complete all of the scraping and analysis tasks. The following information is scraped from various links.

### NASA Mars News

* The Mars News Site [Mars News Site](https://redplanetscience.com/) is scraped and the latest News Title and Paragraph Text are collected and the same is assigned to variables that can be referenced later.

### JPL Mars Space Images - Featured Image

* The url that is used for the Featured Space Image site is [here](https://spaceimages-mars.com).

* splinter is used to navigate the site and to find the image url for the current Featured Mars Image and the url string is assigned to a variable called `featured_image_url`.

* The image url to the full size `.jpg` image is located.

* Then the complete url string for this image is saved using a variable.


### Mars Facts

* The Mars Facts webpage that was used is [here](https://galaxyfacts-mars.com) and Pandas was used to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Pandas was also used to convert the data to a HTML table string.

### Mars Hemispheres

* The astrogeology site that was used is [here](https://marshemispheres.com/) to obtain high resolution images for each of Mar's hemispheres.

* This process involved clicking on each of the links to the hemispheres in order to find the image url to the full resolution image.

* The image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name was saved. Then a Python dictionary was used to store the data using the keys `img_url` and `title`.

* The dictionary was appended with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


## Step 2 - MongoDB and Flask Application

MongoDB is used with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* This task involved converting the Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, a route is created called `/scrape` that will import the`scrape_mars.py` script and call the`scrape` function.

* The return value is stored in Mongo as a Python dictionary.

* A root route is created `/` that will query the Mongo database and pass the mars data into an HTML template to display the data.

* A template HTML file is created called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 

![final_app_part1.png](Images/final_app.png)


