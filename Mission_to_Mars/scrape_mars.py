#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    
    return Browser('chrome', **executable_path, headless=False)

mars_all={}


def scrape_all():
    mars_all["Homework"] = "Web Scraping Challenge"
    scrape_news()
    scrape_feat_img()
    scrape_facts()
    scrape_hemis()
    return mars_all

def scrape_news():

    browser = init_browser()
 
    url = "https://redplanetscience.com/"
    browser.visit(url)
    soup = bs(browser.html, "html.parser")

    time.sleep(3)

    marsheadline = soup.find("div","content_title").get_text()
    marscopy = soup.find("div","article_teaser_body").get_text()

    mars_all["title"] = marsheadline
    mars_all["story"] = marscopy
    
    browser.quit()
    
    return


def scrape_feat_img():
    browser = init_browser()

    url = "https://spaceimages-mars.com"
    browser.visit(url)
    soup = bs(browser.html, "html.parser")

    relative_image_path = soup.find_all('img')[1]["src"]

    featured_image_url = url + "/" + relative_image_path

    mars_all["feat_img"] = featured_image_url

    browser.quit()

    return


def scrape_facts():
    mars_facts_url = "https://galaxyfacts-mars.com"

    table = pd.read_html(mars_facts_url)

    df = table[1]
    df.columns = ["Fact", "Value"]
    df.set_index(["Fact"], inplace = True)
    
    facts_html = df.to_html()
    facts_html = facts_html.replace("\n","")

    mars_all["mars_html"] = facts_html
   
    return


def scrape_hemis():

    browser = init_browser()

    url = "https://marshemispheres.com/"
    browser.visit(url)
    soup = bs(browser.html, "html.parser")

    links = soup.find_all("a", "itemLink product-item", href=True)

    html_list = []

    for link in links:
        if url + link['href'] not in html_list:
            if link['href'] != '#':
                html_list.append(url + link['href'])


    # print(html_list)
    hemi_images=[]

    for img_html in html_list:
        browser.visit(img_html)
        soup = bs(browser.html, "html.parser")
        ls = soup.find_all('a', href = True, text = True)
        img_title = soup.find('h2','title').get_text()
        for l in ls:
            if url + link['href'] not in hemi_images:
                if l.text == 'Sample':
                    hemi_images.append({"Title": img_title, "img_url": url + l['href']})

    mars_all["hemispheres"] = hemi_images

    browser.quit()

    return mars_all