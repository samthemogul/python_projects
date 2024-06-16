from flask import Flask, render_template, request, abort
from queries import Queries
from models import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../products.db"


db.init_app(app)
queries = Queries(db)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/products/<product_id>")
def show_product(product_id):
    product = queries.select_product_with_details(product_id)
    if not product:
        abort(404, "No product with that id")
    return render_template("product.html", product=product)


@app.get("/search")
def search():
    params = {
        "q": request.values.get("q"),
        "brands": request.values.getlist("brand"),
        "categories": request.values.getlist("category"),
        "fk_advantage": request.values.get("fk-advantage"),
        "ratings": request.values.getlist("ratings"),
        "price_min": request.values.get("min-price"),
        "price_max": request.values.get("max-price"),
        "sort": request.values.get("sort"),
    }
    products = queries.search_products(params)
    return render_template("search.html", products=products, params=params)

@app.get("/api/products/<product_id>")
def show_product_json(product_id):
    product = queries.select_product_with_details(product_id)
    if not product:
        abort(404, "No product with that id")
    return product.to_dict()

@app.get("/api/search")
def search_json():
    params = {
        "q": request.values.get("q"),
        "brands": request.values.getlist("brand"),
        "categories": request.values.getlist("category"),
        "fk_advantage": request.values.get("fk-advantage"),
        "ratings": request.values.getlist("ratings"),
        "price_min": request.values.get("min-price"),
        "price_max": request.values.get("max-price"),
        "sort": request.values.get("sort"),
    }
    products = queries.search_products(params)
    return [p.to_dict() for p in products]