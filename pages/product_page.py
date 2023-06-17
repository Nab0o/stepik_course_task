from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.add_to_basket), "add_to_basket is not present"

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.add_to_basket).click()
        #self.is_element_present(*ProductPageLocators.add_to_basket).click()
        #self.browser.find_element(*ProductPageLocators.add_to_basket).click()
    

    def iteam_added_to_basket_check_name_price(self):  
        assert self.is_element_present(*ProductPageLocators.add_success_alert), 'no success alert for adding to cart'

        success_alert =  self.browser.find_element(*ProductPageLocators.add_success_alert).text
        #WebDriverWait(self.browser, 60).until(
            #EC.presence_of_element_located(*ProductPageLocators.add_success_alert)).text
        assert success_alert == "The shellcoder's handbook", 'alert says you added wrong book'
        # Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.

        success_alert_price = self.browser.find_element(*ProductPageLocators.add_success_alert_price).text
        #WebDriverWait(self.browser, 60).until(
         #   EC.presence_of_element_located(*ProductPageLocators.add_success_alert_price)).text
        assert success_alert_price == '9,99 £', 'full basket price not equal to the iteam price that you have just added'
        # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 