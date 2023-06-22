from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    basket_link = (By.CSS_SELECTOR, ".btn-group > a")

class BasketPageLocators():
    basket_empty = (By.CSS_SELECTOR, "#content_inner>p")
    basket_is_not_empty = (By.CSS_SELECTOR, "#content_inner .row h2")

class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    add_to_basket = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    add_success_alert = (By.CSS_SELECTOR, "#messages .alertinner strong")
    add_success_alert_price = (By.CSS_SELECTOR, ".alertinner>p>strong")
    iteam_name_locator = (By.CSS_SELECTOR, ".product_main>h1")
    iteam_price_locator = (By.CSS_SELECTOR, ".product_main>p.price_color")