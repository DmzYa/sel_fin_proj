from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "No add button on the page!"
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_btn.click()
        self.solve_quiz_and_get_code()


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_NAME_ADDED_MESSAGE), "OK message is presented, but should not be"


    def should_gone_after_a_while(self):
        assert self.is_disappeared(*ProductPageLocators.BOOK_NAME_ADDED_MESSAGE), "OK message is disappeared after some timeout"


    def is_msg_ok(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text == self.browser.find_element(*ProductPageLocators.BOOK_NAME_ADDED_MESSAGE).text, "Product name is not matching product name after adding to basket"
