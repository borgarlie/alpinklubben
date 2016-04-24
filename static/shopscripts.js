var modal_rental = $('#shop_modal_rental');
var modal_buy = $('#shop_modal_buy');
var last_opened_rental = null;
var last_opened_buy = null;
var temp_modal_buy_html = modal_buy.find('.modal-body').html();
var temp_modal_buy_html_footer = modal_buy.find('.modal-footer').html();
var temp_modal_rental_html = modal_rental.find('.modal-body').html();
var temp_modal_rental_html_footer = modal_rental.find('.modal-footer').html();
var purchase_complete_buy = false;
var purchase_complete_rental = false;

$('.open-shopDialog-rental').click(function(){
    if (purchase_complete_rental) {
        modal_rental.find('.modal-body').html(temp_modal_rental_html);
        purchase_complete_rental = false;
    }
    modal_rental.find('.modal-footer').html(temp_modal_rental_html_footer);
    last_opened_rental = $(this).data('id');
    $.ajax({
        type: "GET",
        url: '/api/menu-item-rental/'+$(this).data('id'),
        dataType: 'json',
        success: function(data){
            var item = data.item;
            modal_rental.find('.modal-body #nameRental').html(item.name);
            var priceOption = "<select name='priceOpt' id='priceOptRental'><option value='hourly'>Timer</option>";
            priceOption += "<option value='daily'>Dager</option>" ;
            priceOption += "<option value='weekly'>Uker</option></select>";
            modal_rental.find('.modal-body #priceOptionRental').html(priceOption);
            var selectPriceOptions = "<select name='priceOptNum' id='num'>";
            for(var i = 1; i <= 10; i++) {
                selectPriceOptions += "<option value="+i+">"+i+"</option>";
            }
            selectPriceOptions += "</select>";
            modal_rental.find('.modal-body #selectPriceInfoRental').html(selectPriceOptions);
            $("#priceOptRental").change(function() {
                newPrice();
            });
            $('#selectPriceInfoRental').change(function(){
               newPrice();
            });
            var newPrice = function() {
                var type = $( "#priceOptRental" ).val();
                var num = $( "#num" ).val();
                var price = 0;
                if (type == "daily") {
                    price = num * item.price_daily
                }
                else if (type == 'weekly') {
                    price = num * item.price_weekly
                }
                else {
                    price = num * item.price_hour
                }
                modal_rental.find('.modal-body #priceRental').html(price);
            };
            newPrice();
        }
    });
});

$('.open-shopDialog-buy').click(function(){
    if (purchase_complete_buy) {
        modal_buy.find('.modal-body').html(temp_modal_buy_html);
        purchase_complete_buy = false;
    }
    modal_buy.find('.modal-footer').html(temp_modal_buy_html_footer);
    last_opened_buy = $(this).data('id');
    $.ajax({
        type: "GET",
        url: '/api/menu-item-buy/'+$(this).data('id'),
        dataType: 'json',
        success: function(data){
            console.log(data);
            var item = data.item;
            modal_buy.find('.modal-body #name').html(item.name);
            var priceOption = "<select name='priceOpt' id='priceOpt'><option value='adult'>Voksen</option>";
            priceOption += "<option value='child'>Barn</option>" ;
            modal_buy.find('.modal-body #priceOption').html(priceOption);
            $("#priceOpt").change(function() {
                newPrice();
            });
            var newPrice = function() {
                var type = $( "#priceOpt" ).val();
                var price = 0;
                if (type == "child") {
                    price = item.price_child
                }
                else {
                    price = item.price_adult
                }
                modal_buy.find('.modal-body #price').html(price);
            };
            newPrice();
        }
    });
});

$('#buyForm').submit(function(e){
    var id = last_opened_buy;
    e.preventDefault();
    $.ajax({
        url:'/api/menu-item-buy/item/'+id,
        type:'post',
        data:$('#buyForm').serialize(),
        success:function(data){
            if (data == "true") {
                modal_buy.find('.modal-body').html("Din betaling er godkjent!");
                modal_buy.find('.modal-footer').html("<button type='button' id='closeBuyForm' class='btn btn-default' data-dismiss='modal'>Avslutt</button>");
                $('#closeBuyForm').click(function(e) {
                    $('#shop_modal_buy').modal('hide');
                    location.reload();
                });
                purchase_complete_buy = true;
            }
            else {
                modal_buy.find('#modal_buy_footer_info').html("Noe info mangler eller stemmer ikke");
            }

        }
    });
});

$('#buyFormRental').submit(function(e){
    var id = last_opened_rental;
    e.preventDefault();
    $.ajax({
        url:'/api/menu-item-rental/item/'+id,
        type:'post',
        data:$('#buyFormRental').serialize(),
        success:function(data){
            if (data == "true") {
                modal_rental.find('.modal-body').html("Din betaling er godkjent!");
                modal_rental.find('.modal-footer').html("<button type='button' id='closeBuyFormRental' class='btn btn-default' data-dismiss='modal'>Avslutt</button>");
                $('#closeBuyFormRental').click(function(e) {
                    $('#shop_modal_rental').modal('hide');
                    location.reload();
                });
                purchase_complete_rental = true;
            }
            else if (data == "none") {
                modal_rental.find('.modal-body').html("Det er dessverre ingen pakker av denne typen igjen.");
                modal_rental.find('.modal-footer').html("<button type='button' id='closeBuyFormRental' class='btn btn-default' data-dismiss='modal'>Avslutt</button>");
                $('#closeBuyFormRental').click(function(e) {
                    $('#shop_modal_rental').modal('hide');
                });
                purchase_complete_rental = true;
            }
            else {
                modal_rental.find('#modal_rental_footer_info').html("Noe info mangler eller stemmer ikke");
            }

        }
    });
});



