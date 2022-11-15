from selenium.webdriver.common.by import By


class PageLocators(object):
    body = (By.XPATH, '//body')
    html = (By.TAG_NAME, 'html')


class HomePageLocators(PageLocators):
    search_field = (By.XPATH, '//div[@id="__next"]/div[2]/div[2]/div/div[1]/div[1]/div[1]/input')
    cart_link = (By.ID, 'Cart-navitem')


class SearchPageLocators(PageLocators):
    search_field = (By.ID, 'form-input')
    result = (By.XPATH, '//div[@id="__next"]/div[2]/div[2]/div/div[3]/div')
    first_result = (By.XPATH, '//div[@id="__next"]/div[2]/div[2]/div/div[3]/div/div[3]/div[1]')


class ProductPageLocators(PageLocators):
    add_to_cart_button = (By.XPATH, '//div[@id="__next"]/div[2]/div[3]/div[2]')
    added_to_cart_msg = (By.XPATH, '//div[@id="__next"]/div[2]/div[2]/div[3]/div/div')
    cart_link = (By.ID, 'Cart-navitem')


class CartPageLocators(PageLocators):
    edit_ship_to = (By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/img')
    ship_to_field = (By.XPATH, '(//*[@id="DeliveryAddress_uncheckedButton__2mqM9"])[3]')
    settle_order_button = (By.ID, 'myCartChina_placeOrder__3z3Mz')
    ship_to_phone_field = (By.ID, 'shiptono')
    bill_to_phone_field = (By.ID, 'billtono')
    disclaimer = (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[1]/div[5]/span')
    submit_order_button = (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[2]/div[2]')
    notification_msg = (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]')
    order_number = (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/span')
    my_order = (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[1]/div[3]/button[1]/div')


class OrderPageLocators(PageLocators):
    my_order = (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[1]/div/div[2]/div[3]')
    order_number = (
        By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/div/div[1]/div/div[1]/div[1]/div/label')
