import re

class UiActionHelper():

    def __init__(self, app):
        self.app = app

    def fill_form(self, name_id, name, email_id, email):

        wd = self.app.wd
        name_from = wd.find_element_by_css_selector('#{}'.format(name_id))
        name_from.click()
        name_from.clear()
        name_from.send_keys('{}'.format(name))
        email_from = wd.find_element_by_css_selector('#{}'.format(email_id))
        email_from.click()
        email_from.clear()
        email_from.send_keys('{}'.format(email))

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



