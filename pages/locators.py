from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASS = (By.ID, "id_registration-password1")
    REGISTRATION_PASS_AGAIN = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, 'btn-add-to-basket')
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_NAME_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")


class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")

