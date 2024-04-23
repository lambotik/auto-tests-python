"""Auto tests for verifying web elements on the 'Contacts' page"""
import allure
from pages.contacts_page import ContactsPage


@allure.epic("The Contacts Page")
class TestContactsPage:
    class TestContactsPageStructure:

        @allure.title("Verify presence and visibility of content on the page")
        def test_cp_01_01_verify_page_presence_and_visibility(self, driver, contacts_page_open):
            page = ContactsPage(driver)
            print(driver.current_url)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence is not None, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible on the page"
