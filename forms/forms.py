from wtforms import Form, validators, StringField, IntegerField


class ShopFormBuy(Form):
    email = StringField('Email Address', [validators.required(), validators.Length(min=6, max=35)])
    name = StringField('Navn pa korteier', [validators.required(), validators.Length(min=2, max=35)])
    card = IntegerField('Kortnummer', [validators.required()])
    date_year = IntegerField('Dato Y', [validators.required()])
    date_month = IntegerField('Dato M', [validators.required()])
    cvc = IntegerField('CVC', [validators.required()])
    priceOpt = StringField('Pris kategori', [validators.required()])


class ShopFormRental(Form):
    email = StringField('Email Address', [validators.required(), validators.Length(min=6, max=35)])
    name = StringField('Navn pa korteier', [validators.required(), validators.Length(min=2, max=35)])
    card = IntegerField('Kortnummer', [validators.required()])
    date_year = IntegerField('Dato Y', [validators.required()])
    date_month = IntegerField('Dato M', [validators.required()])
    cvc = IntegerField('CVC', [validators.required()])
    priceOpt = StringField('Pris kategori', [validators.required()])
    priceOptNum = StringField('Antall', [validators.required()])
