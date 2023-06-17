from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    add_to_basket = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    add_success_alert = (By.CSS_SELECTOR, "#messages .alertinner strong")
    add_success_alert_price = (By.CSS_SELECTOR, ".alertinner>p>strong")