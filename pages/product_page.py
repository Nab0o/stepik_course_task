from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.add_to_basket), "add_to_basket is not present"
    
       
    def iteam_name_find(self):    #запоминаем имя добавляемого товара в переменную
        iteam_name = self.browser.find_element(*ProductPageLocators.iteam_name_locator)
        return iteam_name.text 
    
    def iteam_price_find(self):
        iteam_price = self.browser.find_element(*ProductPageLocators.iteam_price_locator)
        return iteam_price.text



    def add_to_basket(self): 
        self.browser.find_element(*ProductPageLocators.add_to_basket).click()
        #self.is_element_present(*ProductPageLocators.add_to_basket).click()
        #self.browser.find_element(*ProductPageLocators.add_to_basket).click()
    

    def iteam_added_to_basket_check_name(self, iteam_name):  
        #iteam_name это переменная с названием товара iteam_price с ценой товара
        
        assert self.is_element_present(*ProductPageLocators.add_success_alert), 'no success alert for adding to cart'

        success_alert =  self.browser.find_element(*ProductPageLocators.add_success_alert)
        #WebDriverWait(self.browser, 60).until(
            #EC.presence_of_element_located(*ProductPageLocators.add_success_alert)).text
        
        assert iteam_name == success_alert.text, 'alert says you added wrong book'
        # Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.



    def iteam_added_to_basket_check_price(self, iteam_price): 
        success_alert_price = self.browser.find_element(*ProductPageLocators.add_success_alert_price)
        #WebDriverWait(self.browser, 60).until(
        #   EC.presence_of_element_located(*ProductPageLocators.add_success_alert_price)).text
        assert success_alert_price.text == iteam_price, 'full basket price not equal to the iteam price that you have just added'
        # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 


    def should_not_be_success_message_wait(self):
        assert self.is_not_element_present(*ProductPageLocators.add_success_alert), \
            "Success message is presented, but should not be"
        #В первом случае мы будет ждать 4 секунды и если в течении этого времени элемент не появится - тест пройдет успешно.
        
    def should_not_be_success_message_now(self):
        assert not self.is_element_present(*ProductPageLocators.add_success_alert),\
            "Success message is presented"
        #Во втором случае (assert not) - ожидание не выполняется и тест пройдет успешно сразу же, как увидит, что искомого элемента на странице нет. 
        #настройка в base page
     
    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.add_success_alert), \
            "Success message is presented, but should not be"
