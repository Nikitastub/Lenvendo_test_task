from selenium.webdriver.common.by import By

class Locators():
    # поле ввода имени отправителя
    sender_name_field = (By.CSS_SELECTOR, "#name")
    # поле ввода эл. почты отправителя
    sender_email_field = (By.CSS_SELECTOR, "#email")
    # поле ввода имени получателя
    addressee_name_field = (By.CSS_SELECTOR, "#name1")
    # поле ввода эл. почты получателя
    addressee_email_field = (By.CSS_SELECTOR, "#email1")