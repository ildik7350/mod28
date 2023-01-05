#python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_password_recovery.py

from pages.auth_page import AuthPage
from config import valid_telephone, pass_gener, email_gener


def test_selection_window(web_browser):
    """Проверка страницы восстановления пароля"""
    page = AuthPage(web_browser)
    page.forgot_password.click()
    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/' in page.get_current_url()
    assert page.text_recovery.is_visible()
    assert page.tab_phone.is_visible()
    assert page.tab_email.is_visible()
    assert page.tab_login.is_visible()
    assert page.tab_ls.is_visible()
    assert page.email_input_form.is_visible()
    assert page.captcha_text.is_visible()
    assert page.button_continue.is_visible()
    assert page.button_back.is_visible()


def test_password_recovery_phone(web_browser):
    """Восстановление пароля по номеру телефона"""
    page = AuthPage(web_browser)
    page.forgot_password.click()
    page.email_input_form.send_keys(valid_telephone)
    page.captcha.send_keys(pass_gener())
    page.button_continue.click()

    assert page.captcha_text.is_visible()
    assert page.button_continue.is_visible()
    assert page.button_back.is_visible()
    assert page.tab_phone_trait.is_visible()
    assert page.text_invalid.is_visible()


def test_password_recovery_email(web_browser):
    """Восстановление пароля по email"""
    page = AuthPage(web_browser)
    page.forgot_password.click()
    page.email_input_form.send_keys(email_gener())
    page.captcha.send_keys(pass_gener())
    page.button_continue.click()

    assert page.captcha_text.is_visible()
    assert page.button_continue.is_visible()
    assert page.button_back.is_visible()
    assert page.tab_email_trait.is_visible()
    assert page.text_invalid.is_visible()
