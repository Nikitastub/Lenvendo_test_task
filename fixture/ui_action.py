import string
import random

class UiActionHelper():

    def __init__(self, app):
        self.app = app

    def create_new_sending(self):
        wd = self.app.wd
        self.fill_form("name", "email")
        self.fill_form("name1", "email1")
        wd.find_element_by_css_selector('button[type="submit"]').click()

    def fill_form(self, name_id, email_id):
        wd = self.app.wd
        rand_data = self.random_data(7)
        name_from = wd.find_element_by_css_selector('#{}'.format(name_id))
        name_from.click()
        name_from.clear()
        name_from.send_keys('{}'.format(rand_data[0]))
        email_from = wd.find_element_by_css_selector('#{}'.format(email_id))
        email_from.click()
        email_from.clear()
        email_from.send_keys('{}'.format(rand_data[1]))

    def get_url(self):
        wd = self.app.wd
        url = wd.current_url
        return url

    def random_data(self, maxlen):
        symbols = string.ascii_letters + string.digits
        random_name = "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))])
        random_email = "".join([random.choice(symbols) for i in range(random.randrange(1, maxlen))]) + '@' + 'mail.ru'
        return [random_name, random_email]

