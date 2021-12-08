import allure

@allure.feature('digift.ru')
@allure.story('отправка подарочной электронной карты')
@allure.severity('critical')
def test_sending_gift(app, data):
    with allure.step('Переход на главную страницу'):
        app.open_main_page()
    with allure.step('Пролистывание страницы до футера'):
        app.action.bottom_scroll()
    with allure.step('Заполнение поля формы отправителя'):
        app.action.fill_sender_form(*data[:2])
    with allure.step('Заполнение поля формы получателя'):
        app.action.fill_addressee_form(*data[2:])
    with allure.step('Нажатие кнопки перехода к оплате'):
        app.action.go_to_paying_page()
    with allure.step('Проверка URL после перехода на страницу оплаты'):
        app.action.check_paying_page_url(paying_url=app.action.get_url())
    with allure.step('Проверка отображения секции "Заказ оплачен"'):
        app.action.check_payed_section()
    with allure.step('Проверка отображения текста "Ваш подарок уже в пути"'):
        app.action.check_payed_section_text()

