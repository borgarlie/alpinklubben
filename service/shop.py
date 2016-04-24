# coding=utf-8
import datetime

from entities.receipt import RentalReceipt
from entities.rentalitem import RentalItem
from entities.shopitem import ShopItem


class ShopService:
    def __init__(self):
        self.rental_items = self.init_rental_items()
        self.shop_items = self.init_shop_items()

    @staticmethod
    def init_rental_items():
        # TODO: this should come from database: MAX - number of active rentals
        now = datetime.datetime.utcnow()
        currently_rented_1 = RentalReceipt.query.filter(RentalReceipt.until_time >= now,
                                                            RentalReceipt.rental_id == "rental1").count()
        available_package_1 = 10 - currently_rented_1
        currently_rented_2 = RentalReceipt.query.filter(RentalReceipt.until_time >= now,
                                                            RentalReceipt.rental_id == "rental2").count()
        available_package_2 = 4 - currently_rented_2
        currently_rented_3 = RentalReceipt.query.filter(RentalReceipt.until_time >= now,
                                                            RentalReceipt.rental_id == "rental3").count()
        available_package_3 = 17 - currently_rented_3
        currently_rented_4 = RentalReceipt.query.filter(RentalReceipt.until_time >= now,
                                                            RentalReceipt.rental_id == "rental4").count()
        available_package_4 = 8 - currently_rented_4
        currently_rented_5 = RentalReceipt.query.filter(RentalReceipt.until_time >= now,
                                                            RentalReceipt.rental_id == "rental5").count()
        available_package_5 = 11 - currently_rented_5
        rental_items = [RentalItem("rental1", "Basic", "pakke1.jpg", 100, 200, 300,
                                   "Dette er pakken for nybegynnere", available_package_1),
                        RentalItem("rental2", "Viderekomne", "pakke2.jpg", 200, 300, 400,
                                   "Dette er pakken for viderekomne", available_package_2),
                        RentalItem("rental3", "Alpin pakken", "pakke3.jpg", 300, 500, 700,
                                   u"Dette er den berømte alpin pakken", available_package_3),
                        RentalItem("rental4", "Snowboard", "pakke4.jpg", 1000, 1500, 2000,
                                   "Dette er snowboard pakken", available_package_4),
                        RentalItem("rental5", "Den ultimate", "pakke5.jpg", 1100, 1600, 2100,
                                   "Dette er den ultimate pakken", available_package_5)]
        return rental_items

    def get_rental_items(self):
        return self.rental_items

    @staticmethod
    def init_shop_items():
        shop_items = [ShopItem("shop1", "Dagskort", "heiskort.jpg", 50, 100, "Heiskort for en dag"),
                      ShopItem("shop2", "Ukekort", "heiskort.jpg", 250, 450, "Heiskort for en uke"),
                      ShopItem("shop3", "Sesongkort", "heiskort.jpg", 500, 800, "Heiskort for en sesong")]
        return shop_items

    def get_shop_items(self):
        return self.shop_items

    def get_rental_item(self, item_id):
        item = None
        for rental_item in self.rental_items:
            if rental_item.id == item_id:
                item = rental_item
                break
        return item

    def get_shop_item(self, item_id):
        item = None
        for shop_item in self.shop_items:
            if shop_item.id == item_id:
                item = shop_item
                break
        return item
