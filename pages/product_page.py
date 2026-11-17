from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "div.alert-info p strong")

    def add_to_basket(self):
        button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
        button.click()
        try:
            self.solve_quiz_and_get_code()
        except NoAlertPresentException:
            pass

    def get_product_name(self):
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def should_be_add_to_basket_message(self):
        assert self.is_element_present(*self.SUCCESS_MESSAGE), "Нет сообщения о добавлении в корзину"

    def should_product_name_match_in_message(self, expected_name):
        message_name = self.browser.find_element(*self.SUCCESS_MESSAGE).text
        assert message_name == expected_name, f"Название товара в сообщении ({message_name}) не совпадает с ожидаемым ({expected_name})"

    def should_basket_total_match_product_price(self, expected_price):
        basket_total = self.browser.find_element(*self.BASKET_TOTAL_MESSAGE).text
        assert basket_total == expected_price, f"Стоимость корзины ({basket_total}) не совпадает с ожидаемой ценой ({expected_price})"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except:
            return False
        return True
