import string
import random

class UiActionHelper():

    def __init__(self, app):
        self.app = app

    def create_new_sending(self):
        wd = self.app.wd
        self.fill_form_from()
        self.fill_form_to()
        wd.find_element_by_css_selector('button[type="submit"]').click()

    def get_url(self):
        wd = self.app.wd
        url = wd.current_url
        return url

    def fill_form_from(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#name').click()
        wd.find_element_by_css_selector('#name').clear()
        wd.find_element_by_css_selector('#name').send_keys(self.random_string(7))
        wd.find_element_by_css_selector('#email').click()
        wd.find_element_by_css_selector('#email').clear()
        wd.find_element_by_css_selector('#email').send_keys(self.random_email(7))

    def fill_form_to(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#name1').click()
        wd.find_element_by_css_selector('#name1').clear()
        wd.find_element_by_css_selector('#name1').send_keys(self.random_string(7))
        wd.find_element_by_css_selector('#email1').click()
        wd.find_element_by_css_selector('#email1').clear()
        wd.find_element_by_css_selector('#email1').send_keys(self.random_email(7))

    def get_final_url(self):
        wd = self.app.wd
        final_url = wd.current_url
        return final_url

    def random_string(self, maxlen):
        symbols = string.ascii_letters + string.digits
        return "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))])

    def random_email(self, maxlen):
        symbols = string.ascii_letters + string.digits
        return "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))]) + '@' + 'mail.ru'
