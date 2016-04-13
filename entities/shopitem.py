class ShopItem:
    def __init__(self, id, name, image_url, price_child, price_adult, description):
        self.id = id
        self.name = name
        self.image_url = image_url
        self.price_child = price_child
        self.price_adult = price_adult
        self.description = description

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image_url': self.image_url,
            'price_child': self.price_child,
            'price_adult': self.price_adult,
            'description': self.description
        }
