from flask import abort, jsonify, request, Blueprint

from resources.main import shop_service
from service.forms import ShopFormRental, ShopFormBuy

shop_resource = Blueprint('shop_resource', __name__, template_folder='templates')


@shop_resource.route('/api/menu-item-buy/<string:menu_id>', methods=['GET'])
def get_menu_item_buy(menu_id):
    item = shop_service.get_shop_item(menu_id)
    print(item)
    if item is None:
        abort(404)
    return jsonify({'item': item.serialize()})


@shop_resource.route('/api/menu-item-rental/<string:menu_id>', methods=['GET'])
def get_menu_item_rental(menu_id):
    item = shop_service.get_rental_item(menu_id)
    print(item)
    if item is None:
        abort(404)
    return jsonify({'item': item.serialize()})


@shop_resource.route('/api/menu-item-buy/item/<string:menu_id>', methods=['POST'])
def purchase_item_buy(menu_id):
    print(menu_id)
    print(request.form)
    form = ShopFormBuy(request.form)
    if form.validate():
        # do the insertion logic
        # still return false if the insertion fails
        return "true"
    return "false"


@shop_resource.route('/api/menu-item-rental/item/<string:menu_id>', methods=['POST'])
def purchase_item_rental(menu_id):
    print(menu_id)
    print(request.form)
    form = ShopFormRental(request.form)
    if form.validate():
        # do the insertion logic
        # still return false if the insertion fails
        return "true"
    return "false"