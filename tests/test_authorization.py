#python -m pytest -v --driver Chrome --driver-path /chromedriver.exe tests/test_authorization.py


from pages.auth_page import AuthPage
from pages.auth_code import CodePage
from config import valid_email, valid_password, valid_telephone, no_valid_telephone, \
    login_no_valid, ls_no_valid, pass_gener, email_gener, code

def test_main_page_all_items(web_browser):
    """Проверка главной страницы"""
    page = AuthPage(web_browser)

    assert page.email_input_form.is_visible()
    assert page.password_input_form.is_visible()
    assert page.tab_phone.is_visible()
    assert page.tab_email.is_visible()
    assert page.tab_login.is_visible()
    assert page.tab_ls.is_visible()
    assert 'https://b2c.passport.rt.ru/' in page.get_current_url()
    assert page.text_authorization.is_visible()
    assert page.text_personal_area.is_visible()

def test_positive_authorisation_phone(web_browser):
    """Авторизация по номеру телефона и паролю"""
    page = AuthPage(web_browser)
    page.tab_phone.click()
    page.email_input_form.send_keys(valid_telephone)
    page.password_input_form.send_keys(valid_password)
    page.check_mark.click() #Снимаем галочку с поля запомнить меня
    page.btn.click()
    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()

def test_negative_authorisation_phone(web_browser):
    """Не удачная авторизация по номеру телефона и паролю"""
    page = AuthPage(web_browser)
    page.tab_phone.click()
    page.email_input_form.send_keys(no_valid_telephone)
    page.password_input_form.send_keys(valid_password)
    page.check_mark.click()
    page.btn.click()
    assert page.forgot_password.is_visible()
    assert page.invalid_login_password.is_visible()

def test_negative_authorization_login(web_browser):
    """Не удачная авторизация по логину и паролю"""
    page = AuthPage(web_browser)
    page.tab_login.click()
    page.email_input_form.send_keys(login_no_valid)
    page.password_input_form.send_keys(valid_password)
    page.check_mark.click()
    page.btn.click()
    assert page.forgot_password.is_visible()
    assert page.invalid_login_password.is_visible()


def test_positive_authorisation_email(web_browser):
    """Авторизация по email и паролю"""
    page = AuthPage(web_browser)
    page.tab_email.click()
    page.email_input_form.send_keys(valid_email)
    page.password_input_form.send_keys(valid_password)
    page.check_mark.click()
    page.btn.click()
    assert 'https://b2c.passport.rt.ru/account_b2c/page' in page.get_current_url()


def test_negative_authorization_ls(web_browser):
    """Не удачная авторизация по лицевому счету и паролю"""
    page = AuthPage(web_browser)
    page.tab_ls.click()
    page.email_input_form.send_keys(ls_no_valid)
    page.password_input_form.send_keys(valid_password)
    page.check_mark.click()
    page.btn.click()
    assert page.forgot_password.is_visible()
    assert page.invalid_login_password.is_visible()

def test_negative_authorisation_email(web_browser):
    """Не удачная авторизация по рандомным email и паролям"""
    page = AuthPage(web_browser)
    page.tab_email.click()
    if page.captcha_text.is_visible() == False:
        for i in range(5):
            page.email_input_form.send_keys(email_gener())
            page.password_input_form.send_keys(pass_gener())
            page.check_mark.click()
            page.btn.click()
            if page.captcha_text.is_visible():
                break
        page.email_input_form.send_keys(email_gener())
        page.password_input_form.send_keys(pass_gener())
        page.captcha.send_keys(pass_gener())
        page.btn.click()
        assert page.text_authorization.is_visible()
        assert page.captcha_text.is_visible()
        assert page.text_invalid.is_visible()

    if page.captcha_text.is_visible():
        page.email_input_form.send_keys(email_gener())
        page.password_input_form.send_keys(pass_gener())
        page.captcha.send_keys(pass_gener())
        page.btn.click()
        assert page.text_authorization.is_visible()
        assert page.captcha_text.is_visible()
        assert page.text_invalid.is_visible()


def test_negative_authorisation_code(web_browser):
    """Не удачная авторизация по коду на email"""
    page = CodePage(web_browser)

    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/' in page.get_current_url()
    assert page.text_authorization_code.is_visible()
    assert page.text_personal_area.is_visible()
    page.field_address.send_keys(valid_email)
    page.button_get_code.click()
    assert page.code0.is_visible()
    assert page.code1.is_visible()
    assert page.code2.is_visible()
    assert page.code3.is_visible()
    assert page.code4.is_visible()
    assert page.code5.is_visible()


