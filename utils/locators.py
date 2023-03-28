from selenium.webdriver.common.by import By


class PageLocators(object):
    body = (By.XPATH, '//body')
    html = (By.TAG_NAME, 'html')


class HomePageLocators(PageLocators):
    loading_bar = (By.XPATH, '//div[@id="loading-screen"]/div')
    create_org_button = (By.ID, 'create-new')
    search_org_field = (
        By.XPATH, '//admin-organization-list-page/div/div[1]/form-search-component/form/nz-input-group/input')
    search_org_button = (
        By.XPATH, '//admin-organization-list-page/div/div[1]/form-search-component/form/nz-input-group/span/i')
    search_org_result = (By.XPATH,
                         '//admin-organization-list-loadmore/div/nz-list/nz-spin/div/div/div[2]/nz-list-item/admin-organization-card/div')
    dashboard_button = (By.XPATH, '//admin-organization-card/div/div/div/div[1]/button/span[1]')
    instrument_group = (By.XPATH, '//app-dashboard//app-group-list//mat-slider-content/div[2]/div/div/div[1]/div/a')
    group_consumable_state_table_loading = (By.XPATH, '//app-group-consumable-state/nz-table/nz-spin/div[1]/div/span')
    group_consumable_state_table = (
        By.XPATH, '//app-group-consumable-state/nz-table/nz-spin/div/div/nz-table-inner-default/div')
    aperture_strip_cell = (By.XPATH,
                           '//app-group-consumable-state/nz-table/nz-spin/div/div/nz-table-inner-default/div/table/tbody/tr[1]/td[1]')


class LoginPageLocators(PageLocators):
    username_field = (By.ID, 'username-field')
    next_button = (By.ID, 'next-button')
    password_field = (By.ID, 'password-field')
    sign_in_button = (By.ID, 'signin-button')
    login_error_notice = (By.XPATH, '//div[@id="login-error-text"]//span[@class="error-label"]')
