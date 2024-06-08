"""Auto tests for verifying web elements on the 'Used Resources' page"""
import allure
from pages.used_resources_page import UsedResourcesPage
from test_data.used_resources_page_data import UsedResourcesPageData


@allure.epic("Test Used Resources Page")
class TestUsedResourcesPage:
    data = UsedResourcesPageData

    class TestUsedResourcesPageForAuthorizedUser:

        @allure.title("Verify presence, visibility and text accuracy of the title on the page")
        def test_ur_01_01_verify_used_resources_page_title(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            page_title_presence = page.check_used_resources_page_title_presence()
            page_title_visibility = page.check_used_resources_page_title_visibility()
            page_title_text = page.get_used_resources_page_title_content()
            assert page_title_presence is not None, "The title is absent in DOM"
            assert page_title_visibility, "The title is invisible on the page"
            assert (page_title_text
                    in UsedResourcesPageData.used_resources_page_elements_content["page_title_content"]), \
                "The title content does not match the any of the valid option"

        @allure.title("Verify presence, visibility and content accuracy of the text on the page")
        def test_ur_01_02_verify_used_resources_page_text(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            page_text_presence = page.check_used_resources_page_text_presence()
            page_text_visibility = page.check_used_resources_page_text_visibility()
            page_text_content = page.get_text_content_on_the_used_resources_page()
            assert page_text_presence is not None, "The text is absent in DOM"
            assert page_text_visibility, "The text is invisible on the page"
            assert (page_text_content
                    in UsedResourcesPageData.used_resources_page_elements_content["page_text_content"]), \
                "The text content does not match the any of the valid option"

        @allure.title("Verify presence and visibility of the section with links on the page")
        def test_ur_01_03_verify_links_section_on_used_resources_page(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            links_section_presence = page.check_presence_of_links_section_on_used_resources_page()
            links_section_visibility = page.check_visibility_of_links_section_on_used_resources_page()
            assert links_section_presence is not None, "The section with links is absent in DOM"
            assert links_section_visibility, "The section with links is invisible on the page"

        @allure.title("Verify presence and visibility of the section with the freepik.com link on the page")
        def test_ur_01_04_verify_section_of_freepik_com_link(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            section_presence = page.check_presence_of_freepik_com_link_section()
            section_visibility = page.check_visibility_of_freepik_com_link_section()
            assert section_presence is not None, "The section with the freepik.com link is absent"
            assert section_visibility, "The section with the freepik.com link is invisible"

        @allure.title("Verify text of the freepik.com link")
        def test_ur_01_05_verify_freepik_com_link(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            actual_link_text = page.get_text_in_freepik_com_link()
            assert actual_link_text == \
                   UsedResourcesPageData.used_resources_page_elements_content["freepik_com_link_content"], \
                   f"The actual text of the link does not match the valid option"

        @allure.title("Verify presence and visibility of the section with the 'Plants' link on the page")
        def test_ur_01_09_verify_section_of_plants_link(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            section_presence = page.check_presence_of_plants_link_section()
            section_visibility = page.check_visibility_of_plants_link_section()
            assert section_presence is not None, "The section with the 'Plants' link is absent"
            assert section_visibility, "The section with the 'Plants' link is invisible"

        @allure.title("Verify text of the 'Plants' link")
        def test_ur_01_10_verify_plants_link(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            actual_link_text = page.get_text_in_plants_link()
            assert actual_link_text == \
                   UsedResourcesPageData.used_resources_page_elements_content["plants_link_content"], \
                   f"The actual text of the link does not match the valid option"

        @allure.title("Verify presence and visibility of the section with the 'Flora' link on the page")
        def test_ur_01_14_verify_section_of_flora_link(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            section_presence = page.check_presence_of_flora_link_section()
            section_visibility = page.check_visibility_of_flora_link_section()
            assert section_presence is not None, "The section with the 'Flora' link is absent"
            assert section_visibility, "The section with the 'Flora' link is invisible"

        @allure.title("Verify text of the 'Flora' link")
        def test_ur_01_15_verify_flora_link(self, driver, auto_test_user_authorized):
            page = UsedResourcesPage(driver)
            page.open_used_resources_page()
            actual_link_text = page.get_text_in_flora_link()
            assert actual_link_text == \
                   UsedResourcesPageData.used_resources_page_elements_content["flora_link_content"], \
                   f"The actual text of the link does not match the valid option"

        class TestUsedResourcesPageForAuthorizedText:
            @allure.title("Verify value of the title of the page")
            def test_ur_02_01_verify_page_title(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                title_value = page.get_value_of_page_title()
                assert title_value, "The title value of the page is empty"
                assert title_value == UsedResourcesPageData.page_title_current, \
                    "The title value of the page doesn't match the valid value"

        class TestUsedResourcesPageForAuthorizedUserLinks:
            @allure.title("""Verify presence, visibility, clickability, href, status code of links in the sections""")
            def test_ur_03_01_verify_links_in_sections(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                links_presence = page.get_list_of_links()
                links_visibility = page.check_links_visibility()
                links_clickability = page.check_links_clickability()
                links_href = page.get_links_href()
                links_status_codes = page.get_links_status_codes()
                assert links_presence is not None, "The 'Contacts' links are absent in DOM"
                assert links_visibility, "Links are invisible on the page"
                assert links_clickability, "Links are unclickable"
                assert links_href, "Links href are empty"
                assert all(link_href in UsedResourcesPageData.links_href for link_href in links_href), \
                    "Attributes 'href' of links do not match the valid values"
                assert all(link_status_code in UsedResourcesPageData.links_status_codes
                           for link_status_code in links_status_codes), \
                    "Status codes of links do not match the expected values"

            @allure.title("Verify that links in the sections lead to the correct pages after clicking")
            def test_ur_03_02_verify_links_lead_to_the_correct_pages(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                new_tabs_titles = page.click_on_links()
                assert all(new_tab_title in UsedResourcesPageData.pages_titles for new_tab_title in new_tabs_titles), \
                    "Links in the sections lead to incorrect pages after clicking"

        class TestUsedResourcesPageForAuthorizedUserIcons:
            @allure.title("Verify presence, visibility and attributes of icons in the sections")
            def test_ur_04_01_verify_icons_in_sections(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                icons_presence = page.get_list_of_icons()
                icons_visibility = page.check_icons_visibility()
                icons_xmlns = page.get_icons_xmlns_in_sections()
                assert icons_presence, "The icons in the sections are absent"
                assert icons_visibility, "The icons in the sections are invisible"
                assert icons_xmlns, "The 'xmlns' attribute value of the icons in the sections is empty"
                assert all(icon_xmlns == UsedResourcesPageData.icons_xmlns for icon_xmlns in icons_xmlns), \
                    "The 'xmlns' attribute value of some icons is empty or non-accurate"

            @allure.title("Verify sizes of icons in the sections")
            def test_ur_04_02_verify_icons_sizes(self, driver, auto_test_user_authorized):
                page = UsedResourcesPage(driver)
                page.open_used_resources_page()
                icons_size = page.get_icons_sizes()
                icons_size_changes = page.check_size_changes_of_icons()
                assert icons_size != 0, "The icons in the sections hasn't sizes"
                assert icons_size_changes, "Checks of changes in icon sizes have not carried out"
