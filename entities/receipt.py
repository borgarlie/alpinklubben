import datetime
from entities.shared import db


class RentalReceipt(db.Model):
    __tablename__ = "rental_receipt"
    id = db.Column('rental_receipt_id', db.Integer, primary_key=True)
    user_email = db.Column('user_email', db.String(50), index=True)
    rental_id = db.Column('rental_id', db.String(20))
    buy_type = db.Column('buy_type', db.String(20))
    num = db.Column('num', db.Integer)
    buy_time = db.Column('buy_time', db.DateTime)
    until_time = db.Column('until_time', db.DateTime)

    # type is hours, days, weeks
    def __init__(self, user_email, rental_id, buy_type, num):
        self.user_email = user_email
        self.rental_id = rental_id
        self.buy_type = buy_type
        self.num = int(num)
        self.buy_time = datetime.datetime.utcnow()
        self.until_time = self.get_last_usable_date()

    def get_last_usable_date(self):
        until_time = self.buy_time
        if self.buy_type == "daily":
            until_time += datetime.timedelta(days=self.num)
        elif self.buy_type == "weekly":
            until_time += datetime.timedelta(weeks=self.num)
        else:
            until_time += datetime.timedelta(hours=self.num)
        return until_time

    def __repr__(self):
        return '<user_email %r, rental_id %r, buy_type %r, num %r, buy_time %r, until_time %r>' % \
               (self.user_email, self.rental_id, self.buy_type, self.num, self.buy_time, self.until_time)


class BuyReceipt(db.Model):
    __tablename__ = "buy_receipt"
    id = db.Column('buy_receipt_id', db.Integer, primary_key=True)
    user_email = db.Column('user_email', db.String(50), index=True)
    buy_id = db.Column('buy_id', db.String(20))
    buy_type = db.Column('buy_type', db.String(20))
    buy_time = db.Column('buy_time', db.DateTime)
    until_time = db.Column('until_time', db.DateTime)

    # type is child or adult
    def __init__(self, user_email, buy_id, buy_type):
        self.user_email = user_email
        self.buy_id = buy_id
        self.buy_type = buy_type
        self.buy_time = datetime.datetime.utcnow()
        self.until_time = self.get_last_usable_date()

    def get_last_usable_date(self):
        until_time = self.buy_time
        if self.buy_id == "shop1":
            until_time += datetime.timedelta(days=1)
        elif self.buy_id == "shop2":
            until_time += datetime.timedelta(weeks=1)
        else:
            until_time += datetime.timedelta(weeks=10)
        return until_time

    def __repr__(self):
        return '<user_email %r, buy_id %r, buy_type %r buy_time %r, until_time %r>' % \
               (self.user_email, self.buy_id, self.buy_type, self.buy_time, self.until_time)


class ReceiptItem:
    def __init__(self, receipt, item):
        self.receipt = receipt
        self.item = item
