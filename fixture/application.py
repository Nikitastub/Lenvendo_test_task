from selenium import webdriver
from fixture.ui_action import UiActionHelper

class Application:
    def __init__(self, base_url):
        self.wd = webdriver.Chrome()
        self.action = UiActionHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
