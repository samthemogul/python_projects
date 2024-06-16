from sqlalchemy import select
from sqlalchemy.orm import selectinload
from models import Product, Brand, Category


class Queries:
    PER_PAGE = 40

    def __init__(self, db):
        self.db = db

    def select_product_with_details(self, id):
        q = (
            select(Product)
            .filter(Product.id == id)
            .options(selectinload(Product.categories))
            .options(selectinload(Product.brands))
            .options(selectinload(Product.images))
        )
        return self.db.session.scalars(q).first()

    def search_products(self, params):
        q = select(Product)

        if params["q"]:
            q = q.filter(Product.name.like(f"%{params['q']}%"))

        if params["price_max"]:
            q = q.filter(Product.discounted_price < params["price_max"])

        if params["price_min"]:
            q = q.filter(Product.discounted_price > params["price_min"])

        

        if params["ratings"]:
            for rating in params["ratings"]:
                q = q.filter(Product.rating > rating)

        if params["fk_advantage"] in ["on", "true", "checked"]:
            q = q.filter(Product.flipkart_advantage == "true")

        if params["categories"]:
            q = q.join(Product.categories)
            for category in params["categories"]:
                
                q = q.filter(Category.name.like(f"%{category}%"))

        # order the results
        if params["sort"]:
            q = self._order_results(q, params["sort"])

       
        q = (
            q.options(selectinload(Product.categories))
            .options(selectinload(Product.brands))
            .options(selectinload(Product.images))
        )

        if params["brands"]:
            q = q.join(Product.brands)
            for brand in params["brands"]:
                # filter where brand param is LIKE the brand name
                q = q.filter(Brand.name.like(f"%{brand}%"))

        # paginate the results
        # limit of 40 items PER_PAGE
        
        return self.db.paginate(q, per_page=Queries.PER_PAGE)

    def _order_results(self, q, sort_method):
        if sort_method == "relevance":
            return q.order_by(Product.id.asc())
        elif sort_method == "rating":
            return q.order_by(Product.rating.desc())
        elif sort_method == "discount":
            return q.order_by(Product.discount.desc())
        elif sort_method == "price-low":
            return q.order_by(Product.discounted_price.asc())
        elif sort_method == "price-high":
            return q.order_by(Product.discounted_price.desc())
