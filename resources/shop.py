from flask import abort, jsonify, request, Blueprint

from service.forms import ShopFormRental, ShopFormBuy
from entities.receipt import BuyReceipt, RentalReceipt

from entities.shared import db
from service.shop import ShopService

shop_resource = Blueprint('shop_resource', __name__, template_folder='templates')


@shop_resource.route('/api/menu-item-buy/<string:menu_id>', methods=['GET'])
def get_menu_item_buy(menu_id):
    shop_service = ShopService()
    item = shop_service.get_shop_item(menu_id)
    print(item)
    if item is None:
        abort(404)
    return jsonify({'item': item.serialize()})


@shop_resource.route('/api/menu-item-rental/<string:menu_id>', methods=['GET'])
def get_menu_item_rental(menu_id):
    shop_service = ShopService()
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
        receipt = BuyReceipt(request.form['email'], menu_id, request.form['priceOpt'])
        db.session.add(receipt)
        db.session.commit()
        # still return false if the insertion fails
        return "true"
    return "false"


@shop_resource.route('/api/menu-item-rental/item/<string:menu_id>', methods=['POST'])
def purchase_item_rental(menu_id):
    print(menu_id)
    print(request.form)
    form = ShopFormRental(request.form)
    if form.validate():
        shop_service = ShopService()
        if shop_service.get_rental_item(menu_id).available > 0:
            receipt = RentalReceipt(request.form['email'], menu_id, request.form['priceOpt'],
                                    request.form['priceOptNum'])
            db.session.add(receipt)
            db.session.commit()
            # still return false if the insertion fails
            return "true"
        return "none"
    return "false"
