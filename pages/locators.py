from selenium.webdriver.common.by import By


class PageLocators(object):
    body = (By.XPATH, '//body')
    html = (By.TAG_NAME, 'html')


class HomePageLocators(PageLocators):
    logo_img = (By.XPATH, '//a[@id="hfLifetechLogoLink"]/*[@id="Layer_1"]')
    sign_in_menu = (By.ID, 'sign-in-toggle')
    sign_in_button = (By.XPATH, '//*[@id="sign-in"]/div/div/div[1]/div/a')
    logged_in_menu = (By.ID, 'logged-in-toggle')
    sign_out_link = (By.XPATH, '//*[@id="logged-in"]/div/div/div/div[4]/a')


class LoginPageLocators(PageLocators):
    username_field = (By.ID, 'username-field')
    next_button = (By.ID, 'next-button')
    password_field = (By.ID, 'password-field')
    sign_in_button = (By.ID, 'signin-button')
    login_error_notice = (By.XPATH, '//div[@id="login-error-text"]//span[@class="error-label"]')


class RequestQuotePageLocators(PageLocators):
    elms_skus_inquiry_title = (By.XPATH, '//div[@class="page-header"]/h1')
    elms_skus_loading_circle = (By.ID, 'formIncludeLoading')
    elms_skus_request_quote_iframe = (By.ID, 'forminclude')
    elms_skus_comments_input_box = (By.ID, 'contact-us-data-esb_message')
    elms_skus_submit_button = (By.XPATH, '//div[@class="submit section"]/div[4]/div[2]/input')
    elms_skus_informed_msg = (By.ID, 'tfCustomerInformationDTO.emailOptIn_rightcol')
    catalog_skus_inquiry_title = (By.XPATH, '//*[@id="pageheadinghero-183085645"]/div/div/h1')
    catalog_skus_request_quote_form = (By.ID, 'form-container-1814652328')
    catalog_skus_first_name_title = (By.XPATH, '//*[@id="form-container-1814652328"]/div[6]/div/label')
    bulk_inquiry_title = (By.XPATH, '/html/body/div[1]/div[2]/div[4]/div/div/div/div/div/h1')
    bulk_request_quote_form = (
        By.ID, '_content_lifetech_global_en_home_forms_cm-test-using-open-column_jcr_content_MainParsys_start_503f')
    bulk_first_name_title = (By.XPATH,
                             '//*[@id="_content_lifetech_global_en_home_forms_cm-test-using-open-column_jcr_content_MainParsys_start_503f"]/div[4]/div[1]/div[1]/div/div/div[1]/div[1]/label')
    analysis_inquiry_title = (By.XPATH, '/html/body/div[1]/div[2]/div[4]/div/div/div/div/div/h1/p')
    analysis_request_quote_form = (By.ID,
                                   '_content_lifetech_greater-china_zh-cn_home_industrial_spectroscopy-elemental-isotope-analysis_quotation-form_jcr_content_MainParsys_start')
    analysis_name_title = (By.XPATH,
                           '//*[@id="_content_lifetech_greater-china_zh-cn_home_industrial_spectroscopy-elemental-isotope-analysis_quotation-form_jcr_content_MainParsys_start"]/div[3]/div[1]/div[1]/div/div/div[1]/div[1]/label')
