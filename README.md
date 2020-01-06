# Web-Scraping-and-Document-Database


Flask web application that scrapes various websites for data related to the Mars Mission and displays the information in a single HTML page.

# Scrape Materials
- Latest Mars news and text blurb
- Featured JPL image
- Mars twitter account to receive latest data of weather
- Information regarding the planet such as mass and diameter
- Mars hemispheres from USGS Astrogeology site

This application relies on MongoDB as a database tool and communicates to the server via Flask

# Requirements

- pandas==0.23.3
- splinter==0.9.0
- pymongo==3.7.1
- numpy==1.15.0
- Flask==1.0.2
- requests==2.18.4
- beautifulsoup4==4.6.3
- gunicorn==19.9.0
- lxml==4.2.5
- Jinja2==2.10
- beautifulsoup4==4.6.3
- bs4==0.0.1
- Flask-PyMongo==2.1.0