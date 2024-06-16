import unittest
from gradescope_utils.autograder_utils.decorators import weight
from app import *


class TestProductAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    @weight(20)
    def test_api_show_product(self):
        response = self.client.get("/api/products/4717")
        assert response.status == "200 OK"
        assert response.json["id"] == 4717
        assert (
            response.json["name"]
            == "Smiledrive Car Rear View Mirror Phone Hanger - Multi-Purpose Stand"
        )
        assert response.json["retail_price"] == 599
        assert response.json["discounted_price"] == 299
        assert response.json["flipkart_advantage"] == True
        assert response.json["rating"] == "No rating available"
        self.assertAlmostEqual(response.json["discount"], 50)
        assert response.json["categories"] == [
            "Automotive",
            "Accessories & Spare parts",
            "Car Electronics & Accessories",
            "Car Mobile Accessories",
            "Car Mobile Holders",
        ]
        assert response.json["brands"] == ["Smiledrive"]
        assert response.json["images"] == [
            "http://img6a.flixcart.com/image/car-cradle/6/h/y/smiledrive-car-rear-view-mirror-phone-hanger-multi-purpose-stand-original-imae7ndmxnaruezf.jpeg",
            "http://img5a.flixcart.com/image/car-cradle/6/h/y/smiledrive-car-rear-view-mirror-phone-hanger-multi-purpose-stand-original-imae7ndmxnaruezf.jpeg",
            "http://img5a.flixcart.com/image/car-cradle/6/h/y/smiledrive-car-rear-view-mirror-phone-hanger-multi-purpose-stand-original-imae7ndmwmebruvd.jpeg",
        ]

    @weight(20)
    def test_api_search_products(self):
        response = self.client.get(
            "/api/search?q=Ruchiworld%20Marble%20Pot%20Showpiece"
        )
        assert response.status == "200 OK"
        assert len(response.json) == 1
        assert response.json[0]["id"] == 4719
        assert response.json[0]["name"] == "Ruchiworld Marble Pot Showpiece  -  4 cm"

    @weight(10)
    def test_api_search_price_max(self):
        response = self.client.get("/api/search?q=case&max-price=200")
        assert response.status == "200 OK"
        assert len(response.json) == 2
        assert response.json[0]["id"] == 3390
        assert (
            response.json[0]["name"]
            == "Aptron Premium manicure kit in leatherette case - Small"
        )
        assert response.json[1]["id"] == 10940
        assert response.json[1]["name"] == "Bling Book Case for iPad 2 / 3"

    @weight(10)
    def test_api_search_brands(self):
        response = self.client.get("api/search?q=leather&brand=Durian")
        assert response.status == "200 OK"
        assert len(response.json) == 19
        assert response.json[0]["id"] == 11141
        assert response.json[1]["id"] == 11173
        assert response.json[-1]["id"] == 11669

    @weight(10)
    def test_api_order_price_high(self):
        response = self.client.get("api/search?q=2+seater+sofa&sort=price-high")
        assert response.status == "200 OK"
        assert len(response.json) == 12
        assert response.json[0]["id"] == 11630
        assert response.json[1]["id"] == 11463
        assert response.json[2]["id"] == 11141
        assert response.json[3]["id"] == 11413
        assert response.json[4]["id"] == 11553
        assert response.json[5]["id"] == 11632
        assert response.json[6]["id"] == 11631
        assert response.json[7]["id"] == 11527
        assert response.json[8]["id"] == 11497
        assert response.json[9]["id"] == 11719
        assert response.json[10]["id"] == 11168
        assert response.json[11]["id"] == 11367

    @weight(10)
    def test_api_order_price_low(self):
        response = self.client.get("/api/search?q=wallet&sort=price-low")
        assert response.status == "200 OK"
        assert len(response.json) == 14
        assert response.json[0]["id"] == 7796
        assert response.json[1]["id"] == 9690
        assert response.json[2]["id"] == 9692
        assert response.json[3]["id"] == 9693
        assert response.json[4]["id"] == 9694
        assert response.json[-2]["id"] == 9706
        assert response.json[-1]["id"] == 10389


if __name__ == "__main__":
    unittest.main()
