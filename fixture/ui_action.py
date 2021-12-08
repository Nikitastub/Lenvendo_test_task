import re
from fixture.locators import Locators

class UiActionHelper():

    def __init__(self, app):
        self.app = app

    def fill_sender_form(self, name, email):
        wd = self.app.wd
        sender_name = wd.find_element(*Locators.sender_name_field)
        sender_name.click()
        sender_name.clear()
        sender_name.send_keys('{}'.format(name))
        sender_email = wd.find_element(*Locators.sender_email_field)
        sender_email.click()
        sender_email.clear()
        sender_email.send_keys('{}'.format(email))

    def fill_addressee_form(self, name, email):
        wd = self.app.wd
        addressee_name = wd.find_element(*Locators.addressee_name_field)
        addressee_name.click()
        addressee_name.clear()
        addressee_name.send_keys('{}'.format(name))
        addressee_email = wd.find_element(*Locators.addressee_email_field)
        addressee_email.click()
        addressee_email.clear()
        addressee_email.send_keys('{}'.format(email))

    def go_to_paying_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('button[type="submit"]').click()

    def bottom_scroll(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_url(self):
        wd = self.app.wd
        url = wd.current_url
        return url

    def check_paying_page_url(self, paying_url):
        assert re.sub("\d", "", paying_url) == "http://qa.digift.ru/checkout/thanks/?Order_ID=",\
            "Paying page's URL doesn't match the expected result"

    def check_payed_section(self):
        wd = self.app.wd
        assert wd.find_element_by_css_selector('div.order-payed__title > span').text == 'ЗАКАЗ ОПЛАЧЕН!',\
            "Section's text doesn't match the expected result"

    def check_payed_section_text(self):
        wd = self.app.wd
        assert wd.find_element_by_css_selector('div.order-payed > h1').text == 'Ваш подарок уже в пути!',\
            "text doesn't match the expected result"



