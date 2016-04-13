from entities.rentalitem import RentalItem
from entities.shopitem import ShopItem


class ShopService:
    def __init__(self, database):
        self.database = database
        self.rental_items = self.init_rental_items()
        self.shop_items = self.init_shop_items()

    @staticmethod
    def init_rental_items():
        # this should come from database: MAX - number of active rentals
        currently_rented_1 = 1
        available_package_1 = 10 - currently_rented_1
        currently_rented_2 = 2
        available_package_2 = 13 - currently_rented_2
        currently_rented_3 = 1
        available_package_3 = 17 - currently_rented_3
        currently_rented_4 = 5
        available_package_4 = 8 - currently_rented_4
        currently_rented_5 = 0
        available_package_5 = 11 - currently_rented_5
        rental_items = [RentalItem("rental1", "Pakke 1", "pakke1.jpg", 100, 200, 300, "Dette er pakke 1", available_package_1),
                        RentalItem("rental2", "Pakke 2", "pakke2.jpg", 200, 300, 400, "Dette er pakke 2", available_package_2),
                        RentalItem("rental3", "Pakke 3", "pakke3.jpg", 300, 500, 700, "Dette er pakke 3", available_package_3),
                        RentalItem("rental4", "Pakke 4", "pakke4.jpg", 1000, 1500, 2000, "Dette er pakke 4", available_package_4),
                        RentalItem("rental5", "Pakke 5", "pakke5.jpg", 1100, 1600, 2100, "Dette er pakke 5", available_package_5)]
        return rental_items

    def get_rental_items(self):
        return self.rental_items

    @staticmethod
    def init_shop_items():
        shop_items = [ShopItem("shop1", "Dagskort", "heiskort.jpg", 50, 100, "Heiskort for en dag"),
                      ShopItem("shop2", "Ukekort", "heiskort.jpg", 250, 450, "Heiskort for en uke"),
                      ShopItem("shop3", "Sesongkort", "heiskort.jpg", 500, 800, "Heiskort for en sesong")]
        # consider using different images for days / weeks / season?
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

