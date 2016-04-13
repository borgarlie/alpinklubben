# coding=utf-8
from flask import render_template, Blueprint
from flask.ext.login import login_required

from service.shop import ShopService

from entities.shared import db

main_resource = Blueprint('main_resource', __name__, template_folder='templates')

shop_service = ShopService(db)


@main_resource.route('/information')
def information():
    return render_template('information.html', page="information")


@main_resource.route('/profile')
@login_required
def profile():
    return render_template('profile.html', page="profile")


# should this be GET only?
@main_resource.route('/shop', methods=['GET', 'POST'])
def shop():
    rental_items = shop_service.get_rental_items()
    shop_items = shop_service.get_shop_items()
    return render_template('shop.html', rental_items=rental_items, shop_items=shop_items, page="shop")
