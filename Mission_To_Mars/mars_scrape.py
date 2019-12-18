# Import Dependecies 
from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 
import requests
from selenium import webdriver
import time

# Initialize browser
def init_browser(): 
    # Replace the path with your actual path to the chromedriver

    #Mac Users
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)


mars_info = {}

#SCRAPE NEWS
def scrape_mars_news():

    try:
        

        browser = init_browser()
        #INTERACT WITH URL WITH SPLINTER
        url = 'https://mars.nasa.gov/news'
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        news_title = soup.find('div', class_ ='content_title').find('a').text
        news_p = soup.find('div',class_ ='article_teaser_body').text

        mars_info['news_title'] = news_title
        mars_info['news_text'] = news_p

        return mars_info

    
    finally:
        browser.quit()

def scrape_mars_image():
    
    try:
        browser = init_browser()

        image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(image_url)

        browser.click_link_by_partial_text('FULL IMAGE')
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        browser.click_link_by_partial_text('more info')

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        main_url = 'https://www.jpl.nasa.gov'
        featured_image_url = soup.find('figure', class_='lede').a['href']

        featured_image_url = main_url + featured_image_url

        mars_info['featured_url'] = featured_image_url

        return mars_info

    finally:
        browser.quit()

def scrape_mars_weather():
    try:
        browser = init_browser()
        twitter_url = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(twitter_url)
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')

        mars_weather = soup.find('p',class_ = 'TweetTextSize').text
        mars_info['weather'] = mars_weather

        return mars_info

    finally:
        browser.quit()

def scrape_mars_facts():
    try:
        browser = init_browser()
        facts_url = 'https://space-facts.com/mars/'

        mars_facts = pd.read_html(facts_url)
        mars_df = mars_facts[1]
        mars_df.columns = ['Fact','Value']
        mars_df = mars_df.set_index('Fact')
        
        mars_facts = mars_df.to_html()

        mars_info['facts'] = mars_facts

        return mars_info
    
    finally:
        browser.quit()

def scrape_mars_hems():
    try:
        
        browser = init_browser()
        hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hem_url)

        main_url = 'https://astrogeology.usgs.gov'
        titles = []
        URL = []

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        hemispheres = soup.find_all('div', class_ = 'item')

        for hemisphere in hemispheres:
                title = hemisphere.find('h3').text
                titles.append(title)
                image_path = hemisphere.find('a', class_ = 'itemLink')['href']
                image_url = main_url + image_path
                browser.visit(image_url)
                html = browser.html
                soup = BeautifulSoup(html,'html.parser')
                url = soup.find('div', class_ = 'downloads').a['href']
                URL.append(url)
       
        mars_info['image'] = titles
        mars_info['url'] = URL

        return mars_info

    finally:
        browser.quit()






        