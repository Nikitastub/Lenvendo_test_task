import string
import random

class UiActionHelper():

    def __init__(self, app):
        self.app = app

    def create_new_sending(self, name_from, email_from, name_to, email_to):
        wd = self.app.wd
        self.fill_form("name", "email", name=name_from, email=email_from)
        self.fill_form("name1", "email1", name=name_to, email=email_to)
        wd.find_element_by_css_selector('button[type="submit"]').click()

    def fill_form(self, name_id, email_id, name, email):
        wd = self.app.wd
        name_from = wd.find_element_by_css_selector('#{}'.format(name_id))
        name_from.click()
        name_from.clear()
        name_from.send_keys('{}'.format(name))
        email_from = wd.find_element_by_css_selector('#{}'.format(email_id))
        email_from.click()
        email_from.clear()
        email_from.send_keys('{}'.format(email))

    def bottom_scroll(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_url(self):
        wd = self.app.wd
        url = wd.current_url
        return url



