import re
import allure
from allure_commons.types import AttachmentType

@allure.severity('critical')
def test_sending_gift(app):
    app.open_main_page()
    app.action.create_new_sending()
    final_url = app.action.get_url()
    # make a screenshot for allure report
    allure.attach(app.wd.get_screenshot_as_png(), name='scr', attachment_type=AttachmentType.PNG)
    # checking the URLs equality
    assert re.sub("\d", "", final_url) == "http://qa.digift.ru/checkout/thanks/?Order_ID="
    # checking section availability
    assert app.wd.find_element_by_css_selector('div.order-payed__title > span').text == 'ЗАКАЗ ОПЛАЧЕН!'
    # checking text availability
    assert app.wd.find_element_by_css_selector('div.order-payed > h1').text == 'Ваш подарок уже в пути!'

