import re
import allure
from allure_commons.types import AttachmentType

@allure.severity('critical')
def test_sending_gift(app, data):
    test_data = data
    app.open_main_page()
    app.action.create_new_sending(name_from=test_data["random_name_from"], email_from=test_data["random_email_from"],
                                  name_to=test_data["random_name_to"], email_to=test_data["random_email_to"])
    final_url = app.action.get_url()
    # make a screenshot for allure report
    allure.attach(app.wd.get_screenshot_as_png(), name='scr', attachment_type=AttachmentType.PNG)
    # checking the URLs equality
    assert re.sub("\d", "", final_url) == "http://qa.digift.ru/checkout/thanks/?Order_ID="
    # checking section accuracy
    assert app.wd.find_element_by_css_selector('div.order-payed__title > span').text == 'ЗАКАЗ ОПЛАЧЕН!'
    # checking text accuracy
    assert app.wd.find_element_by_css_selector('div.order-payed > h1').text == 'Ваш подарок уже в пути!'

