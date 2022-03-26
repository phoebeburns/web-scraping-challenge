#!/usr/bin/env python
# coding: utf-8


from bs4 import BeautifulSoup
from splinter import Browser
from pprint import pprint
from webdriver_manager.chrome import ChromeDriverManager
import pymongo as pg
import pandas as pd



mars_all = {}

mars_all["homework"] = "web-scraping-challenge"


def scrape():

## Mars news scrape

# browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    marsheadline = soup.find("div","content_title").get_text()
    marscopy = soup.find("div","article_teaser_body").get_text()

    # Close the browser after scraping
    browser.quit()


    mars_all["title"] = marsheadline
    mars_all["story"] = marscopy


## Mars space images featued image

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://spaceimages-mars.com"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    relative_image_path = soup.find_all('img')[1]["src"]

    featured_img = url + relative_image_path

    # Close the browser after scraping
    browser.quit()

    mars_all["feat_img"] = featured_img


##Mars fact table sraping

    mars_facts_url = "https://galaxyfacts-mars.com"

    table = pd.read_html(mars_facts_url)

    df = table[1]
    df.columns = ["Fact", "Value"]
    df.set_index(["Fact"], inline=True)

    facts_html = df.to_html()
    facts_html = facts_html.replace("\n","")

    mars_all["mars_html"] = facts_html


##Mars Hemisphere image scraping

    hemi_images = []

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://marshemispheres.com/cerberus.html"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    cerberus_title = soup.find("h2", class_="title").get_text()

    cerb_desc = soup.find_all('dd')

    cerberus_img = cerb_desc[1].find('a')['href']

    cerberus_image_path = url + "/" + cerberus_img

    print(cerberus_image_path)

    # Close the browser after scraping
    browser.quit()

    cerberus_hemi = {"Title": cerberus_title, "url": cerberus_image_path}

    hemi_images.append(cerberus_hemi)


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://marshemispheres.com/schiaparelli.html"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    schiaparelli_title = soup.find("h2", class_="title").get_text()

    sch_desc = soup.find_all('dd')

    sch_img = sch_desc[1].find('a')['href']

    sch_image_path = url + "/" + sch_img

    # print(sch_image_path)

    # Close the browser after scraping
    browser.quit()

    sch_hemi = {"Title": schiaparelli_title, "url": sch_image_path}

    hemi_images.append(sch_hemi)


## Syrtis Major hemisphere

# browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://marshemispheres.com/syrtis.html"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    syrtis_title = soup.find("h2", class_="title").get_text()

    syrtis_desc = soup.find_all('dd')

    syrtis_img = syrtis_desc[1].find('a')['href']

    syrtis_image_path = url + "/" + syrtis_img

    # Close the browser after scraping
    browser.quit()

    syrtis_hemi = {"Title": syrtis_title, "url": syrtis_image_path}

    hemi_images.append(syrtis_hemi)


## Valles Marineris hemisphere

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://marshemispheres.com/valles.html"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    valles_title = soup.find("h2", class_="title").get_text()

    valles_desc = soup.find_all('dd')

    valles_img = valles_desc[1].find('a')['href']

    valles_image_path = url + "/" + valles_img

    # Close the browser after scraping
    browser.quit()

    valles_hemi = {"Title": valles_title, "url": valles_image_path}

    hemi_images.append(valles_hemi)

    mars_all["hemispheres"] = hemi_images

    return mars_all
