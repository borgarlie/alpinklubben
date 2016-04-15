# coding=utf-8
import datetime
from flask import render_template, Blueprint
from flask.ext.login import login_required, current_user

from service.shop import ShopService
from entities.user import User
from entities.receipt import RentalReceipt, BuyReceipt

from entities.shared import db

main_resource = Blueprint('main_resource', __name__, template_folder='templates')

shop_service = ShopService(db)


@main_resource.route('/information')
def information():
    return render_template('information.html', page="information")


@main_resource.route('/profile')
@login_required
def profile():
    user_id = current_user.get_id()
    registered_user = User.query.filter_by(id=user_id).first()

    now = datetime.datetime.utcnow()

    # query those before now vs those after now

    rental_receipts = RentalReceipt.query.filter_by(user_email=registered_user.email).all()
    # print("receipts:::")
    # for receipt in rental_receipts:
    #     print(receipt)
    #     # print(receipt.buy_time)
    #     # print(receipt.rental_id)
    #     print(receipt.get_last_usable_date())
    # print("end receipts :::")
    buy_receipts = BuyReceipt.query.filter_by(user_email=registered_user.email).all()
    # print("buy receipts:::")
    # for receipt in buy_receipts:
    #     print(receipt.buy_time)
    #     print(receipt.buy_id)
    #     print(receipt.get_last_usable_date())
    # print("end buy receipts :::")


    return render_template('profile.html', page="profile", rental_receipts=rental_receipts, buy_receipts=buy_receipts)


# should this be GET only?
@main_resource.route('/shop', methods=['GET', 'POST'])
def shop():
    rental_items = shop_service.get_rental_items()
    shop_items = shop_service.get_shop_items()
    return render_template('shop.html', rental_items=rental_items, shop_items=shop_items, page="shop")
