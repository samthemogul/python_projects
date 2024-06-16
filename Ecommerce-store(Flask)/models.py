from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Text, Boolean, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
import json

db = SQLAlchemy()

ProductCategory = db.Table(
    "product_categories",
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("category_id", ForeignKey("categories.id"), primary_key=True),
)

ProductBrand = db.Table(
    "product_brands",
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("brand_id", ForeignKey("brands.id"), primary_key=True),
)


class Product(db.Model):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    retail_price = Column(Integer)
    discounted_price = Column(Integer)
    flipkart_advantage = Column(Boolean)
    rating = Column(Integer)
    product_specifications = Column(Text)
    categories = relationship(
        "Category",
        secondary=ProductCategory,
        lazy="raise_on_sql",
        back_populates="products",
    )
    brands = relationship(
        "Brand", secondary=ProductBrand, lazy="raise_on_sql", back_populates="products"
    )
    images = relationship("Image", lazy="raise_on_sql", back_populates="product")
    discount = retail_price / discounted_price

    def get_discount(self):
        if self.retail_price and self.discounted_price:
            return (
                round(float(self.discounted_price) / float(self.retail_price), 2) * 100
            )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "retail_price": self.retail_price,
            "discounted_price": self.discounted_price,
            "flipkart_advantage": self.flipkart_advantage,
            "rating": self.rating,
            "product_specifications": self.product_specifications,
            "discount": self.get_discount(),
            "categories": [category.name for category in self.categories],
            "brands": [brand.name for brand in self.brands],
            "images": [image.url for image in self.images],
        }


class Category(db.Model):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    products = relationship(
        "Product",
        secondary=ProductCategory,
        lazy="raise_on_sql",
        back_populates="categories",
    )


class Image(db.Model):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    product_id = Column("product_id", ForeignKey("products.id"), primary_key=True)
    product = relationship("Product", lazy="raise_on_sql", back_populates="images")
    url = Column(Text)


class Brand(db.Model):
    __tablename__ = "brands"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    products = relationship(
        "Product", secondary=ProductBrand, lazy="raise_on_sql", back_populates="brands"
    )
