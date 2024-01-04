import os
from dotenv import load_dotenv
import allure
from pages.profile_page import ProfilePage
from pages.registration_page import RegistrationPage
from test_data.links import MainPageLinks
from test_data.data import Messages, Data
load_dotenv()


@allure.epic("Test Registration Page")
class TestRegistrationPage:
    urls = MainPageLinks
    msg = Messages

    @allure.title('Checking impossibility of registration with an existing email')
    def test_registration_with_existing_email(self, driver):
        page = RegistrationPage(driver)
        driver.get(self.urls.URL_MAIN_PAGE)
        page.open_registration_page()
        page.fill_first_name(Data.FIRST_NAME)
        page.fill_birthday(Data.BIRTHDAY)
        page.choose_gender()
        page.fill_email(os.environ["CHANGE_PASSWORD_EMAIL"])
        page.fill_password(os.environ["CHANGE_PASSWORD"])
        page.fill_repeat_password(os.environ["CHANGE_PASSWORD"])
        page.choose_agreement()
        page.click_registration_button()
        text = page.check_error_message_existing_email()
        assert text == self.msg.EXISTING_EMAIL, 'The user has registered with an existing email'

    @allure.title('Checking possibility of registration with a new email')
    def test_registration_with_new_email(self, driver):
        page = RegistrationPage(driver)
        driver.get(self.urls.URL_MAIN_PAGE)
        page.open_registration_page()
        page.fill_first_name(Data.FIRST_NAME)
        page.fill_birthday(Data.BIRTHDAY)
        page.choose_gender()
        page.fill_email(Data.EMAIL)
        page.fill_password(os.environ["CHANGE_PASSWORD"])
        page.fill_repeat_password(os.environ["CHANGE_PASSWORD"])
        page.choose_agreement()
        page.click_registration_button()
        page.check_change_url()
        page = ProfilePage(driver)
        assert page.check_user_profile(), 'The user has not registered with a new email'
