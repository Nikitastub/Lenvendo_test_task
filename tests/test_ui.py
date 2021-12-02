import re
import allure
from allure_commons.types import AttachmentType

@allure.feature('digift.ru')
@allure.story('отправка подарочной электронной карты')
@allure.severity('critical')
def test_sending_gift(app, data):
    with allure.step('Переход на главную страницу'):
        app.open_main_page()
    with allure.step('Пролистывание страницы до футера'):
        app.action.bottom_scroll()
    with allure.step('Заполнение форм отправителя и получателя, переход к оплате'):
        app.action.create_new_sending(data["name_from"], data["email_from"], data["name_to"], data["email_to"])
    with allure.step('Получение URL после перехода на страницу оплаты'):
        final_url = app.action.get_url()
    with allure.step('Проверка соотвествия URL страницы оплаты'):
        assert re.sub("\d", "", final_url) == "http://qa.digift.ru/checkout/thanks/?Order_ID="
    with allure.step('Проверка отображения секции "Заказ оплачен"'):
        assert app.wd.find_element_by_css_selector('div.order-payed__title > span').text == 'ЗАКАЗ ОПЛАЧЕН!'
    with allure.step('Проверка отображения текста "Ваш подарок уже в пути"'):
        assert app.wd.find_element_by_css_selector('div.order-payed > h1').text == 'Ваш подарок уже в пути!'
    allure.attach(app.wd.get_screenshot_as_png(), name='checkout_page', attachment_type=AttachmentType.PNG)
