from selenium.webdriver.common.by import By


class PageLocators(object):
    body = (By.XPATH, '//body')
    html = (By.TAG_NAME, 'html')


class HomePageLocators(PageLocators):
    loading_bar = (By.XPATH, '//div[@id="loading-screen"]/div')
    create_org_button = (By.ID, 'create-new')


class LoginPageLocators(PageLocators):
    username_field = (By.ID, 'username-field')
    next_button = (By.ID, 'next-button')
    password_field = (By.ID, 'password-field')
    sign_in_button = (By.ID, 'signin-button')
    login_error_notice = (By.XPATH, '//div[@id="login-error-text"]//span[@class="error-label"]')
