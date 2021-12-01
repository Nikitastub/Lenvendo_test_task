import re

def test_sending_gift(app):
    app.open_home_page()
    app.action.create_new_sending()
    final_url = app.action.get_url()
    assert re.sub("\d", "", final_url) == "http://qa.digift.ru/checkout/thanks/?Order_ID="
    assert app.wd.find_element_by_css_selector('div.order-payed__title > span').text == 'ЗАКАЗ ОПЛАЧЕН!'
    assert app.wd.find_element_by_css_selector('div.order-payed > h1').text == 'Ваш подарок уже в пути!'

