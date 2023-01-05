#python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_registration.py

from pages.auth_page import AuthPage
from config import first_name, last_mame, valid_password, valid_email, valid_telephone, email_gener, pass_gener
def test_new_user_registration(web_browser):
    """Проверка страницы регистраци"""
    page = AuthPage(web_browser)
    page.register_field.click()
    assert 'b2c.passport.rt.ru/auth/realms/b2c/login-actions' in page.get_current_url()
    assert page.register_first.is_presented()
    assert page.register_last.is_presented()
    assert page.register_email.is_presented()
    assert page.register_now_passw.is_presented()
    assert page.register_passw_confirm.is_presented()
    assert page.register_region.is_presented()
    assert page.register_user_agreement.is_presented()
    assert page.register_logo.is_presented()
    assert page.register_left.is_presented()
    assert page.register_right.is_presented()

def test_register_existing_user_email(web_browser):
    """Повторная регистраци на email"""
    page = AuthPage(web_browser)
    page.register_field.click()
    page.register_first.send_keys(first_name)
    page.register_last.send_keys(last_mame)
    page.register_email.send_keys(valid_email)
    page.register_now_passw.send_keys(valid_password)
    page.register_passw_confirm.send_keys(valid_password)
    page.register_button.click()
    assert page.button_re_entry.is_presented()
    page.button_re_entry.click()
    assert 'https://b2c.passport.rt.ru/' in page.get_current_url()


def test_register_existing_user_elephone(web_browser):
    """Повторная регистраци на номер телефона"""
    page = AuthPage(web_browser)
    page.register_field.click()
    page.register_first.send_keys(first_name)
    page.register_last.send_keys(last_mame)
    page.register_email.send_keys(valid_telephone)
    page.register_now_passw.send_keys(valid_password)
    page.register_passw_confirm.send_keys(valid_password)
    page.register_button.click()
    assert page.button_re_entry.is_presented()
    page.button_re_entry.click()
    assert 'https://b2c.passport.rt.ru/' in page.get_current_url()

def test_registration_user_passwords_dont_meet(web_browser):
    """Регистрация нового пользователя пароль не соответствуют требованиям"""
    page = AuthPage(web_browser)
    page.register_field.click()
    page.register_first.send_keys(first_name)
    page.register_last.send_keys(last_mame)
    page.register_email.send_keys(email_gener())
    page.register_now_passw.send_keys(pass_gener())
    page.register_passw_confirm.send_keys(pass_gener())
    page.register_button.click()
    assert page.password_short_up.is_visible()
    assert page.password_short_down.is_visible()

def test_registration_user_passwords_dont_dont_match(web_browser):
    """Регистрация нового пользователя пароли не совпадают"""
    page = AuthPage(web_browser)
    page.register_field.click()
    page.register_first.send_keys(first_name)
    page.register_last.send_keys(last_mame)
    page.register_email.send_keys(email_gener())
    page.register_now_passw.send_keys('As12dDs*')
    page.register_passw_confirm.send_keys('*sDd21sA')
    page.register_button.click()

    assert page.passwords_dont_match.is_visible()

