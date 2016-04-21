# coding=utf-8
import datetime
from flask import render_template, Blueprint
from flask.ext.login import login_required, current_user

from service.shop import ShopService
from entities.user import User
from entities.receipt import RentalReceipt, BuyReceipt, ReceiptItem

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
    rental_receipts_active = RentalReceipt.query.filter(RentalReceipt.user_email == registered_user.email,
                                                        RentalReceipt.until_time >= now).all()
    rental_receipts_not_active = RentalReceipt.query.filter(RentalReceipt.user_email == registered_user.email,
                                                            RentalReceipt.until_time < now).all()
    buy_receipts_active = BuyReceipt.query.filter(BuyReceipt.user_email == registered_user.email,
                                                  BuyReceipt.until_time >= now).all()
    buy_receipts_not_active = BuyReceipt.query.filter(BuyReceipt.user_email == registered_user.email,
                                                      BuyReceipt.until_time < now).all()

    rental_active = []
    for item in rental_receipts_active:
        rental_active.append(ReceiptItem(item, shop_service.get_rental_item(item.rental_id)))

    rental_not_active = []
    for item in rental_receipts_not_active:
        rental_not_active.append(ReceiptItem(item, shop_service.get_rental_item(item.rental_id)))

    buy_active = []
    for item in buy_receipts_active:
        buy_active.append(ReceiptItem(item, shop_service.get_shop_item(item.buy_id)))

    buy_not_active = []
    for item in buy_receipts_not_active:
        buy_not_active.append(ReceiptItem(item, shop_service.get_shop_item(item.buy_id)))

    return render_template('profile.html', page="profile",
                           rental_receipts_active=rental_active,
                           rental_receipts_not_active=rental_not_active,
                           buy_receipts_active=buy_active,
                           buy_receipts_not_active=buy_not_active)


@main_resource.route('/shop')
def shop():
    user_id = current_user.get_id()
    registered_user = User.query.filter_by(id=user_id).first()
    rental_items = shop_service.get_rental_items()
    shop_items = shop_service.get_shop_items()
    return render_template('shop.html', user=registered_user, rental_items=rental_items, shop_items=shop_items, page="shop")
