from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

import time
import pytest

#отсортировал тесты по порядку из шаблона для проверки, вынес вверх те что должны быть с пометкой need_review
#не забывайте про окружение + если используете VS studio code и у вас не запускается с ошибкой WebDriverException: Message: 'chromedriver'
#то скопируйте chromedriver в папку с проектом - заработает
#+ловил 1 раз что тест упал когда не должен был, связано с работой серверов - если воспроизводится error то попробуйте пожалуйста
#запустить тесты когда на сервер будет меньшая нагрузка selenium1py.pythonanywhere.com
#pip install -r requirements.txt        - команда для установки пакетов окружения +инструкция в read Sme проекта




class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        #page.go_to_login_page
        page.should_be_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "5!"  
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        linktask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'    
        page = ProductPage(browser, linktask) 
        page.open()  
        page.should_not_be_success_message_wait()
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.should_be_add_to_basket_button()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.iteam_added_to_basket_check_name(page.iteam_name_find())
        page.iteam_added_to_basket_check_price(page.iteam_price_find())    

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_add_to_basket_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.iteam_added_to_basket_check_name(page.iteam_name_find())
    page.iteam_added_to_basket_check_price(page.iteam_price_find())

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_cart()
    page.should_be_empty_basket()
    page.should_be_empty_basket_text()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()





def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('linktask', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'])
def test_guest_cant_see_success_message(browser, linktask):
    page = ProductPage(browser, linktask) 
    page.open()  
    page.should_not_be_success_message_wait()




@pytest.mark.parametrize('linktask', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'])
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, linktask): 
    page = ProductPage(browser, linktask) 
    page.open()  
    page.add_to_basket()
    page.should_not_be_success_message_now()


@pytest.mark.parametrize('linktask', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'])
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser, linktask):
    page = ProductPage(browser, linktask) 
    page.open()  
    page.add_to_basket()
    page.should_be_disappeared_success_message()   
