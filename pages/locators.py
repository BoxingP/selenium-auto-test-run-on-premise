from selenium.webdriver.common.by import By


class PageLocators(object):
    body = (By.XPATH, '//body')
    html = (By.TAG_NAME, 'html')


class HomePageLocators(PageLocators):
    logo_img = (By.XPATH, '(//a[@id="hfLifetechLogoLink"]/*[@id="Layer_1"])[2]')
    sign_in_menu = (By.ID, 'sign-in-toggle')
    sign_in_button = (By.XPATH, '//li[@id="sign-in"]//div[@id="accounts-dd"]/div/div[1]/div/a')
    logged_in_menu = (By.ID, 'logged-in-toggle')
    sign_out_link = (By.XPATH, '//li[@id="logged-in"]//div[@id="accounts-dd"]/div/div/div[4]/a')


class LoginPageLocators(PageLocators):
    username_field = (By.ID, 'username-field')
    next_button = (By.ID, 'next-button')
    password_field = (By.ID, 'password-field')
    sign_in_button = (By.ID, 'signin-button')
    login_error_notice = (By.XPATH, '//div[@id="login-error-text"]//span[@class="error-label"]')


class RequestQuotePageLocators(PageLocators):
    inquiry_title = (By.XPATH, '//div[@class="page-header"]/h1')
    loading_circle = (By.ID, 'formIncludeLoading')
    request_quote_iframe = (By.ID, 'forminclude')
    comments_input_box = (By.ID, 'contact-us-data-esb_message')
    submit_button = (By.XPATH, '//div[@class="submit section"]/div[4]/div[2]/input')
    informed_msg = (By.ID, 'tfCustomerInformationDTO.emailOptIn_rightcol')
