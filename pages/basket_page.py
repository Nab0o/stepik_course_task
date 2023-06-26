from .base_page import BasePage
from .locators import BasketPageLocators



class BasketPage(BasePage):
    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.basket_empty),\
            "no text about empty basket"         
    
    def should_be_empty_basket(self):
        assert not self.is_element_present(*BasketPageLocators.basket_is_not_empty),\
            "basket is not empty" 

