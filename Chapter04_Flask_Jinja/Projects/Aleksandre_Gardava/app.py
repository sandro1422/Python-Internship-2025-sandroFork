from flask import Flask, render_template

app = Flask(__name__)
products = [
    {
        "id" :0,
        "name": "Anker Nano 4 Charger 30W",
        "price": "69.00",
        "img": "/static/anker nano4.jpg"
    },
    {
        "id" :1,
        "name": "HP LaserJet MFP M141w",
        "price": "499.00",
        "img": "/static/HP LaserJet MFP M141w.jpg"
    },
    {
        "id" :2,
        "name": "Intel Core i3-12100",
        "price": "529.00",
        "img": "/static/Intel Core i3-12100.jpg"
    }
]
@app.route('/')
def index():
    return render_template("index.html",  products=products)

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/view_product/<int:product_id>')
def view_product(product_id):
    return render_template("view_product.html", product=products[product_id])

if __name__ == '__main__':
    app.run(debug=True)