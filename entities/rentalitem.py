class RentalItem:
    def __init__(self, id, name, image_url, price_hour, price_daily, price_weekly, description, available):
        self.id = id
        self.name = name
        self.image_url = image_url
        self.price_hour = price_hour
        self.price_daily = price_daily
        self.price_weekly = price_weekly
        self.description = description
        self.available = available

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image_url': self.image_url,
            'price_hour': self.price_hour,
            'price_daily': self.price_daily,
            'price_weekly': self.price_weekly,
            'description': self.description,
            'available': self.available
        }
