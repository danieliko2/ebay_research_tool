from flask import Flask
from flask import render_template, request
app = Flask(__name__)
from search_utls import scrap2

@app.route('/')
def hello_world():
    return 'Hello, World!'

    
@app.route("/home", methods=['GET', 'POST'])
def listen():
    if request.method == 'GET':
        return render_template("home.html") # currently showing all ips
    if request.method == "POST":
        product = request.form["productName"]
        print(product)
        found_products = scrap2(product)
        print("founds:")
        print(found_products)
        return render_template("home.html", products=found_products)