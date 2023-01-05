from pages.base import WebPage
from pages.elements import WebElement
from config import start_web


class CodePage(WebPage):

    def __init__(self, web_driver, url=''):
        url = start_web
        super().__init__(web_driver, url)

    text_authorization_code = WebElement(xpath="(//*[contains(text(), 'Авторизация по коду')])")
    text_personal_area = WebElement(xpath="(// *[contains(text(),'Личный кабинет')])")
    field_address = WebElement(xpath="// *[ @ id ='address']")
    button_get_code = WebElement(xpath="// *[ @ id ='otp_get_code']")
    code0 = WebElement(id='rt-code-0')
    code1 = WebElement(id='rt-code-1')
    code2 = WebElement(id='rt-code-2')
    code3 = WebElement(id='rt-code-3')
    code4 = WebElement(id='rt-code-4')
    code5 = WebElement(id='rt-code-5')
    incorrect_code = WebElement(xpath="(// *[contains(text(), 'Неверный код. Повторите попытку')]")
    validation_code = WebElement(xpath="(// *[contains(text(), 'Закончились попытки валидации кода. Пожалуйста, запросите код снова')])[2]")
    code_expired= WebElement(xpath="(// *[contains(text(), 'Срок действия кода истёк. Пожалуйста, запросите код снова')]")
    code_repeat = WebElement(css_selector='button.code-input-container__resend')
    prohibited_sending_code = WebElement(xpath="(// *[contains(text(), 'Отправка сообщения возможна через:')]")
