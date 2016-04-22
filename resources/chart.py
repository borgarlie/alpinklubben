from flask import abort, jsonify, Blueprint

from entities.receipt import BuyReceipt
from entities.user import User

chart_resource = Blueprint('chart_resource', __name__, template_folder='templates')


@chart_resource.route('/api/user-chart-data')
def get_chart_resource_users():
    first = User.query.filter(User.year_born >= 1996).count()
    second = User.query.filter(User.year_born < 1996, User.year_born >= 1986).count()
    third = User.query.filter(User.year_born < 1986, User.year_born >= 1976).count()
    forth = User.query.filter(User.year_born < 1976).count()
    item = ChartData(first, second, third, forth)
    return jsonify({'item': item.serialize()})


@chart_resource.route('/api/sales-chart-data')
def get_chart_resource_sales():
    first = BuyReceipt.query.filter(BuyReceipt.buy_id == "shop1").count()
    second = BuyReceipt.query.filter(BuyReceipt.buy_id == "shop2").count()
    third = BuyReceipt.query.filter(BuyReceipt.buy_id == "shop3").count()
    item = ChartData(first, second, third, None)
    return jsonify({'item': item.serialize()})


class ChartData:
    def __init__(self, first, second, third, forth):
        self.first = first
        self.second = second
        self.third = third
        self.forth = forth

    def serialize(self):
        return {
            'first': self.first,
            'second': self.second,
            'third': self.third,
            'forth': self.forth
        }
