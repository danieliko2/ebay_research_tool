from math import prod
import requests
from bs4 import BeautifulSoup
import re

from traitlets import CInt

def myfunc():
    URL = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=wireless+earbuds&_sacat=0&LH_TitleDesc=0&_odkw=anker+earbuds&_osacat=0"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser") # new soup

    results = soup.select('li[class*="item s-item__pl"]') # select all items in search
    products = []

    for result in results:
        top_rated = result.find("span", class_= "s-item__etrs-text") # select top rated to remove
        if top_rated == None: # filter top rated sellers
            hotness = result.find("span", {"class" : re.compile('s-item__hotness.*')}) # select hotness
            if(hotness != None):
                hotness_text = hotness.text
                hotness_arr = hotness_text.split(" ")
                if(hotness_arr[1] == "sold"): # select sold
                    solds = hotness_arr[0].replace(',', '').replace('+', '') # format number
                    solds = int(solds)
                    if(1 <= solds <= 200): # filter results between 1 and 200
                        print(hotness_text)
                        product = [result.find("h3", class_="s-item__title").text, result.find("a", class_="s-item__link", href=True)['href']] # get title and link of product
                        print(product)
                        products.append(product)

    for product in products:
        URL = product[1]
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser") # new soup

        seller_info = soup.find("div", class_="vim x-about-this-seller")
        seller_stars = int(seller_info.find("span", class_="ux-textspans ux-textspans--PSEUDOLINK").text)
        print(seller_stars)
        products_f1 = []
        if(15 <= seller_stars <= 300): # check for seller stars
            sold_feedback = soup.find("span", class_="soldwithfeedback")
            try:
                solds = sold_feedback.find("a", class_= re.compile('vi-.*'), href=True)['href']
            except:
                print("try1")
            # try:
                sold_feedback = soup.find("span", class_= re.compile('qtyTxt.*'), href=True)['href']
                solds = sold_feedback.find("a", class_= re.compile('vi-.*'), href=True)['href']
            # except:
            #     print("try2")
            print(solds)
            solds 
            solds = int(solds.split(" ")[0].replace(',', ''))
            if(solds >= 10):
                print(solds)
                product.append(seller_stars)
                product.append(solds)
                products_f1.append(product)
        
        print(products_f1) # products after filter1



def testFilter():
    product = ["soundcore airbuds", "https://www.ebay.com/itm/294053273191?epid=2312617599&hash=item4476f0de67:g:bU8AAOSwGOtgRqat"]
    URL = product[1]
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser") # new soup

    seller_info = soup.find("div", class_="vim x-about-this-seller")
    seller_stars = seller_info.find("span", class_="ux-textspans ux-textspans--PSEUDOLINK").text
    print(seller_stars)
    products_f1 = []
    if(15 <= int(seller_stars) <= 300): # check for seller stars
        sold_feedback = soup.find("span", class_="soldwithfeedback")
        feedback = sold_feedback.find("a", class_= re.compile('vi-.*')).text
        print(feedback)
        feedback = int(feedback.split(" ")[0].replace(',', ''))
        if(feedback >= 10):
            print(feedback)
            product.append(seller_stars)
            products_f1.append(product)
    
    print(products_f1) # products after filter1


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
    
# testfunc()
myfunc()
# testFilter()
# job_elements = results.find_all("li", class_="card-content" + )

# for job_element in job_elements:
#     print(job_element, end="\n"*2)
