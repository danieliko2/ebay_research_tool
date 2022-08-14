from math import prod
import requests
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import random

def scrap2(product):
    product = product.split(" ")
    search = ""
    for word in product:
        search = search + word + "+"
    
    URL = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={search}&_sacat=0"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser") # new soup

    div = soup.find("div", id = "srp-river-results")
    results = div.find_all("li", class_=re.compile('s-item s-item__pl.*')) # select all items in search
    products = []
    print("length: " + str(len(results)))
    # print(results)    
    for result in results:
        top_rated = result.find("span", class_= "s-item__etrs.*") # select top rated to remove
        if top_rated == None: # filter top rated sellers
            product = [result.find("h3", class_="s-item__title").text, result.find("a", class_="s-item__link", href=True)['href']] # get title and link of product
            products.append(product)

            hotness = result.find("span", {"class" : re.compile('s-item__hotness.*')}) # select hotness
            if(hotness != None):
                hotness_text = hotness.text
                hotness_arr = hotness_text.split(" ")
                if(hotness_arr[1] == "sold"): # select sold
                    solds = hotness_arr[0].replace(',', '').replace('+', '') # format number
                    solds = int(solds)
                    print(solds)
                    if(1 <= solds <= 200): # filter results between 1 and 200
                        print(hotness_text)
                        product = [result.find("h3", class_="s-item__title").text, result.find("a", class_="s-item__link", href=True)['href']] # get title and link of product
                        print(product)
                        product.append(solds)
                        products.append(product)

    products_f1 = []

    for product in products:
        try:
                
            time.sleep(random.uniform(0.05, 0.3))
            print(product)
            URL = product[1]
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser") # new soup

            seller_info = soup.find("div", class_="vim x-about-this-seller")
            seller_stars = int(seller_info.find("span", class_="ux-textspans ux-textspans--PSEUDOLINK").text) # find seller stars
            print(seller_stars)
            if(15 <= seller_stars <= 300): # check for seller stars
                # sold_feedback = soup.find("span", class_="soldwithfeedback")
                # try:
                #     solds = int(sold_feedback.find("a", class_= re.compile('vi-.*'), href=True)['href'])
                # except:
                try:
                    print("try1 : ")
                    sold_feedback = soup.find("div", id="mainContent")
                    # print(sold_feedback.prettify)
                    solds = sold_feedback.find("a", class_= re.compile('vi-txt-und.*')).text.split(" ") # find how many sold
                    print("solds: " + solds[0])
                    print(solds)
                    solds = int(solds[0])
                    if(5<= solds <= 300):
                        print(solds)
                        product.append(solds)
                        product.append(seller_stars)
                        products_f1.append(product)
                except:
                    print("error with product information")
                    continue
        except:
            print("error with product")
            continue

    print(products_f1)
    return products_f1



def myfunc(product):
    product = product.split(" ")
    search = ""
    for word in product:
        search = search + word + "+"

    URL = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={search}&_sacat=0"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser") # new soup

    results = soup.select("li", class_=re.compile('s-item.*')) # select all items in search
    products = []

    for result in results:
        top_rated = result.find("span", class_= "s-item__etrs.*") # select top rated to remove
        if top_rated == None: # filter top rated sellers
            hotness = result.find("span", {"class" : re.compile('s-item__hotness.*')}) # select hotness
            if(hotness != None):
                hotness_text = hotness.text
                hotness_arr = hotness_text.split(" ")
                if(hotness_arr[1] == "sold"): # select sold
                    solds = hotness_arr[0].replace(',', '').replace('+', '') # format number
                    solds = int(solds)
                    print(solds)
                    if(1 <= solds <= 200): # filter results between 1 and 200
                        print(hotness_text)
                        product = [result.find("h3", class_="s-item__title").text, result.find("a", class_="s-item__link", href=True)['href']] # get title and link of product
                        print(product)
                        product.append(solds)
                        products.append(product)
    products_f1 = []

    for product in products:
        time.sleep(random.uniform(0.05, 0.3))
        URL = product[1]
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser") # new soup

        seller_info = soup.find("div", class_="vim x-about-this-seller")
        seller_stars = int(seller_info.find("span", class_="ux-textspans ux-textspans--PSEUDOLINK").text)
        print(seller_stars)
        if(15 <= seller_stars <= 300): # check for seller stars
            sold_feedback = soup.find("span", class_="soldwithfeedback")
            try:
                solds = sold_feedback.find("a", class_= re.compile('vi-.*'), href=True)['href']
            except:
                print("try1")
                sold_feedback = soup.find("div", id="mainContent")
                print(sold_feedback.prettify)
                solds = sold_feedback.find("a", class_= re.compile('vi-txt.*'), href=True)['href']


            print(solds)
            product.append(seller_stars)
            products_f1.append(product)
        
    print(products_f1)
    return products_f1 # products after filter1

    # for product in products_f1:
    #     URL = product[4]
    #     page = requests.get(URL)
    #     soup = BeautifulSoup(page.content, "html.parser") # new soup

    #     rows = soup.find("tr", class_="app-table__row")
    #     for row in rows:
    #         item = row.find("td")[3].text

# myfunc("earbuds")
def testFilter():
    product = ["soundcore airbuds", "https://www.ebay.com/itm/294053273191?epid=2312617599&hash=item4476f0de67:g:bU8AAOSwGOtgRqat"]

    URL = "https://www.ebay.com/bin/purchaseHistory?item=393978297005&rt=nc&_trksid=p2047675.l2564"

    page = requests.get(URL)
    page.ok
    soup = BeautifulSoup(page.content, "html.parser") # new soup
    print(soup.findAll("div"))



def testfunc():
    ids = ["1234", "12345", "325", "12654", "1236"]
    pattern = re.compile("123.*")
    for id in ids:
        print(id)
        print(pattern.findall(id))

    x = "4,250"
    y = 100
    z = int(x.replace(',', '')) + y
    print(z)

print("hw")
# testfunc()
# myfunc()
# testFilter()
