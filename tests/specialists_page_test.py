"""Auto tests for verifying web elements on the 'Specialists' page"""
import time
import allure
import requests

from pages.specialists_page import SpecialistsPage
from test_data.specialists_page_data import SpecialistsPageData
from test_data.start_unauthorized_page_data import StartUnauthorizedPageData


@allure.epic("Test Specialists Page")
class TestSpecialistsPage:

    @allure.title("Verify presence, visibility and text accuracy of the title on the Specialists page")
    def test_sp_01_01_verify_specialists_page_title(self, driver, specialists_page_open):
        page = SpecialistsPage(driver)
        page_title_presence = page.check_specialists_page_title_presence()
        page_title_visibility = page.check_specialists_page_title_visibility()
        page_title_text = page.get_specialists_page_title_content()
        assert page_title_presence is not None, "The title is absent in DOM"
        assert page_title_visibility, "The title is invisible on the page"
        assert page_title_text in SpecialistsPageData.specialists_page_elements_content["page_title_content"], \
               "The title content does not match the any of the valid option"

    @allure.title("Verify presence, visibility and content accuracy of the text on the Specialists page")
    def test_sp_01_02_verify_specialists_page_text(self, driver, specialists_page_open):
        page = SpecialistsPage(driver)
        page_text_presence = page.check_specialists_page_text_presence()
        page_text_visibility = page.check_specialists_page_text_visibility()
        page_text_content = page.get_text_content_on_the_specialists_page()
        assert page_text_presence is not None, "The text is absent in DOM"
        assert page_text_visibility, "The text is invisible on the page"
        assert page_text_content in SpecialistsPageData.specialists_page_elements_content["page_text_content"], \
            "The text content does not match the any of the valid option"

    @allure.title("Verify presence, visibility and size of the grid on the Specialists page")
    def test_sp_01_03_verify_specialists_page_grid(self, driver, specialists_page_open):
        page = SpecialistsPage(driver)
        page_grid_presence = page.check_specialists_page_grid_presence()
        page_grid_visibility = page.check_specialists_page_grid_visibility()
        page_grid_size = page.get_specialists_page_grid_size()
        assert page_grid_presence is not None, "The grid is absent in DOM"
        assert page_grid_visibility, "The grid is invisible on the page"
        assert page_grid_size == SpecialistsPageData.specialists_page_grid_size, \
               "The grid size does not match the expected value"

    @allure.title("Verify visibility of cards in the grid on the Specialists page")
    def test_sp_01_04_verify_specialist_cards_visibility(self, driver, specialists_page_open):
        page = SpecialistsPage(driver)
        cards_visibility = page.check_visibility_of_specialist_cards()
        assert cards_visibility, "Specialist cards are invisible in the grid"

    class TestSpecialistCardImages:

        @allure.title("Verify presence and visibility of images in specialist cards in the grid")
        def test_sp_02_01_verify_images_in_cards_are_present_and_visible(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            time.sleep(1)
            images_visibility = page.check_image_presence_and_visibility_in_specialist_cards()
            assert images_visibility, "Images in specialist cards are invisible in the grid"

        @allure.title("Verify attribute values and sizes of images in specialist cards in the grid")
        def test_sp_02_02_verify_images_attributes_and_changed_sizes_in_cards(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            images_src = page.get_images_src_in_specialist_cards()
            images_alt = page.get_images_alt_in_specialist_cards()
            images_size_changes = page.check_size_changes_of_card_images()
            assert images_src, "The 'src' attribute value of some card images is empty"
            assert images_src == SpecialistsPageData.specialists_images_src, \
                "The 'src' attribute values of the card images are unaccurate"
            assert images_alt, "The 'alt' attribute value of some card images is empty"
            for item in images_alt:
                assert item == SpecialistsPageData.specialists_images_alt, \
                    f"The attribute 'alt' '{item}' in the list does not match expected value"
            assert images_size_changes, "Checks of changes in image sizes have not carried out"

        @allure.title("Verify presence, visibility and accuracy of the 1th card's image in the grid")
        def test_sp_02_03_verify_1th_card_image(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            # print(driver.current_url)
            image_presence = page.check_the_1th_card_image_presence()
            image_visibility = page.check_the_1th_card_image_visibility()
            image_src = page.get_the_1th_card_image_src()
            image_alt = page.get_the_1th_card_image_alt()
            image_size = page.get_visible_size_of_the_1th_card_image()
            # print(f"The visible sizes of the 1th card image are: {image_size}")
            driver.set_window_size(820, 1180)
            image_size_new = page.get_visible_size_of_the_1th_card_image()
            # print(f"The new visible sizes of the 1th card image are: {image_size_new}")
            assert image_presence is not None, "The image in the 1th card is absent"
            assert image_visibility, "The 1th card image is invisible"
            assert image_src, "The 'src' attribute value of the 1th card image is empty"
            assert image_src == SpecialistsPageData.specialists_page_images_src["1th_card_img_src"], \
                "The 'src' attribute value of the 1th card image is unaccurate"
            assert image_alt, "The 'alt' attribute value of the 1th card image is empty"
            assert image_alt == SpecialistsPageData.specialists_images_alt, "The 1th card image is unaccurate"

    class TestSpecialistCardsText:

        @allure.title("""Verify presence and visibility of text sections (including names and professions) 
         in specialist cards in the grid""")
        def test_sp_03_01_verify_text_in_cards_is_present_and_visible(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            text_sections = page.check_presence_and_visibility_of_text_sections_in_specialist_cards()
            specialist_names = page.check_presence_and_visibility_of_names_in_specialist_cards()
            specialist_professions = page.check_presence_and_visibility_of_professions_in_specialist_cards()
            assert text_sections, "Sections with text in specialist cards are invisible in the grid"
            assert specialist_names, "Names in specialist cards are invisible in the grid"
            assert specialist_professions, "Professions in specialist cards are invisible in the grid"

        @allure.title("Verify values of names in specialist cards in the grid")
        def test_sp_03_02_verify_name_values_in_cards(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            name_values = page.get_name_values_in_specialist_cards()
            assert name_values, "Name values in cards are empty"
            assert name_values in SpecialistsPageData.specialists_names, \
                "The names in specialist cards do not match the valid values"

        @allure.title("Verify values of profession in specialist cards in the grid")
        def test_sp_03_03_verify_profession_values_in_cards(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            profession_values = page.get_profession_values_in_specialist_cards()
            assert profession_values, "Profession values in cards are empty"
            assert profession_values in SpecialistsPageData.specialists_professions, \
                "The professions in specialist cards do not match the valid values"

    class TestSpecialistPageLinks:

        @allure.title("""Verify presence, visibility, clickability, href, status code, text 
                         of the 'All Specialists' link on the Specialists page""")
        def test_sp_04_01_verify_all_specialists_link(self, driver, specialists_page_open):
            page = SpecialistsPage(driver)
            link_presence = page.check_all_specialists_link_presence()
            link_visibility = page.check_all_specialists_link_visibility()
            link_clickability = page.check_all_specialists_link_clickability()
            link_href = page.get_all_specialists_link_href()
            link_status_code = requests.head(link_href).status_code
            actual_link_text = page.get_text_in_all_specialists_link()
            assert link_presence is not None, "The 'All Specialists' link is absent in DOM"
            assert link_visibility, "The 'All Specialists' link is invisible on the page"
            assert link_clickability, f"The {link_href} link is unclickable"
            assert link_href == SpecialistsPageData.all_specialists_link_href, \
                f"The attribute 'href' of the {link_href} link does not match the valid value"
            assert link_status_code == SpecialistsPageData.all_specialists_link_status_code, \
                f"The {link_href} link status code does not match the valid value"
            assert actual_link_text in SpecialistsPageData.all_specialists_link_text, \
                f"The actual text '{actual_link_text}' of the {link_href} link does not match any of the valid option"

        @allure.title("""Verify that the 'All Specialists' link leads an unauthorized user 
                         to the correct page after clicking""")
        def test_sp_04_02_verify_all_specialists_link_leads_unauthorized_user_to_the_correct_page(self,
                                                                                        driver, specialists_page_open):
            page = SpecialistsPage(driver)
            page.click_all_specialists_link()
            page.switch_to_new_window()
            time.sleep(5)
            text_on_opened_tab = page.get_element_text_on_opened_tab_with_start_unauthorized_page()
            assert text_on_opened_tab in \
                   StartUnauthorizedPageData.text_on_start_unauthorized_page["text_in_section_1"], \
                   "The 'All Specialists' link leads to an incorrect page after clicking " \
                   "or opened page does not load correctly"

        @allure.title("""Verify that the 'All Specialists' link leads an authorized user 
                         to the correct page after clicking""")
        def test_sp_04_03_verify_all_specialists_link_leads_authorized_user_to_the_correct_page(self,
                                                                                    driver, auto_test_user_authorized):
            page = SpecialistsPage(driver)
            page.open_specialists_page()
            page.click_all_specialists_link()
            page.switch_to_new_window()
            time.sleep(5)
            text_on_opened_tab = page.get_specialists_page_title_content()
            assert text_on_opened_tab in SpecialistsPageData.specialists_page_elements_content["page_title_content"], \
                   "The 'All Specialists' link leads to an incorrect page after clicking " \
                   "or opened page does not load correctly"
