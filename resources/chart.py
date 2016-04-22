from flask import abort, jsonify, Blueprint

chart_resource = Blueprint('chart_resource', __name__, template_folder='templates')


@chart_resource.route('/api/user-chart-data')
def get_chart_resource_users():
    item = ChartData(2, 17, 3, 25)
    print(item)
    if item is None:
        abort(404)
    return jsonify({'item': item.serialize()})


@chart_resource.route('/api/sales-chart-data')
def get_chart_resource_sales():
    item = ChartData(1, 2, 3, None)
    print(item)
    if item is None:
        abort(404)
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
