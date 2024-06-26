"""Methods for verifying web elements in the Header on the site"""
import time

import allure
import requests

from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators


class HeaderPage(BasePage):
    locators = HeaderPageLocators

    @allure.step("Check if some content is present in the Header")
    def check_presence_of_header_content(self):
        return self.element_is_present(self.locators.HEADER_CONTENT)

    @allure.step("Check if page content is visible in the Header")
    def check_visibility_of_header_content(self):
        return self.element_is_visible(self.locators.HEADER_CONTENT)

    @allure.step("Get structure of the 1st level of nesting in the Header")
    def get_structure_of_1st_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_FIRST_LEVEL_ELEMENTS)
        # print(f"Amount of elements on the 1st level of nesting in the Header is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 1st level of nesting in the Header are: {tags}")
        return tags

    @allure.step("Check if elements of the 1st level of nesting are visible in the Header")
    def check_elements_visibility_on_1st_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_FIRST_LEVEL_ELEMENTS)
        display_of_all_elements = all(element.is_displayed() for element in elements)
        return display_of_all_elements

    @allure.step("Get structure of the 2nd level of nesting the Header")
    def get_structure_of_2nd_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_SECOND_LEVEL_ELEMENTS)
        # print(f"Amount of elements on the 2nd level of nesting in the Header is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 2nd level of nesting in the Header are: {tags}")
        return tags

    @allure.step("Check if elements of the 2nd level of nesting are visible in the Header")
    def check_elements_visibility_on_2nd_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_SECOND_LEVEL_ELEMENTS)
        display_of_all_elements = all(element.is_displayed() for element in elements)
        return display_of_all_elements

    @allure.step("Get structure of the 3rd level of nesting the Header")
    def get_structure_of_3rd_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_THIRD_LEVEL_ELEMENTS)
        # print(f"Amount of elements on the 3rd level of nesting in the Header is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 3rd level of nesting in the Header are: {tags}")
        return tags

    @allure.step("Check if elements on the 3rd level of nesting are visible in the Header")
    def check_elements_visibility_on_3rd_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_THIRD_LEVEL_ELEMENTS)
        display_of_all_elements = all(element.is_displayed() for element in elements)
        return display_of_all_elements

    @allure.step("Get structure of the 4th level of nesting the Header")
    def get_structure_of_4th_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_FOURTH_LEVEL_ELEMENTS)
        # print(f"Amount of elements on the 4th level of nesting in the Header is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 4th level of nesting in the Header are: {tags}")
        return tags

    @allure.step("Check if elements on the 4th level of nesting are visible in the Header")
    def check_elements_visibility_on_4th_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_FOURTH_LEVEL_ELEMENTS)
        display_of_all_elements = all(element.is_displayed() for element in elements)
        return display_of_all_elements

    @allure.step("Get structure of the 5th level of nesting the Header")
    def get_structure_of_5th_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_FIFTH_LEVEL_ELEMENTS)
        # print(f"Amount of elements on the 5th level of nesting in the Header is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 5th level of nesting in the Header are: {tags}")
        return tags

    @allure.step("Check if elements on the 5th level of nesting are visible in the Header")
    def check_elements_visibility_on_5th_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_FIFTH_LEVEL_ELEMENTS)
        display_of_elements_part = all(element.is_displayed() for element in elements[1:4])
        return display_of_elements_part

    @allure.step("Get structure of the 6th level of nesting the Header")
    def get_structure_of_6th_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_SIXTH_LEVEL_ELEMENTS)
        # print(f"Amount of elements on the 6th level of nesting in the Header is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 6th level of nesting in the Header are: {tags}")
        return tags

    @allure.step("Check if elements on the 6th level of nesting are invisible in the Header")
    def check_elements_invisibility_on_6th_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_SIXTH_LEVEL_ELEMENTS)
        non_display_of_all_elements = all(self.element_is_not_visible(element) for element in elements)
        return non_display_of_all_elements

    @allure.step("Get structure of the 'ru-en' section in the Header")
    def get_structure_of_ru_en_section(self):
        elements = self.elements_are_present(self.locators.SECTION_WITH_BUTTONS_RU_EN)
        # print(f"Amount of elements in the 'ru-en' section in the Header is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        # print(f"Tags of elements in the 'ru-en' section in the Header are: {tags}")
        return tags

    @allure.step("Check if elements in the 'ru-en' section are visible in the Header")
    def check_elements_visibility_in_ru_en_section(self):
        elements = self.elements_are_present(self.locators.SECTION_WITH_BUTTONS_RU_EN)
        display_of_all_elements = all(element.is_displayed() for element in elements)
        return display_of_all_elements

# Checks of Logo in the Section 1 in the Header
    @allure.step("Check the 'Logo' link is present in DOM")
    def check_logo_link_presence(self):
        return self.element_is_present(self.locators.LOGO_LINK)

    @allure.step("Check the 'Logo' link is visible on the page")
    def check_logo_link_visibility(self):
        return self.element_is_visible(self.locators.LOGO_LINK)

    @allure.step("Check the 'Logo' link is clickable")
    def check_logo_link_clickability(self):
        return self.element_is_clickable(self.locators.LOGO_LINK)

    @allure.step("Get attribute 'href' of the 'Logo' link")
    def get_logo_link_href(self):
        return self.get_link_href(self.locators.LOGO_LINK)

    @allure.step("Get status code of the 'Logo' link")
    def get_logo_link_status_code(self):
        link_href = self.get_logo_link_href()
        link_status_code = requests.head(link_href).status_code
        # print(f"Logo link status code is: ", link_status_code)
        return link_status_code

    @allure.step("Click on the 'Logo' link")
    def click_logo_link(self):
        self.element_is_present_and_clickable(self.locators.LOGO_LINK).click()
        return self.driver.current_url

    @allure.step("Check if the 'Logo' image is present")
    def check_logo_image_presence(self):
        return self.element_is_present(self.locators.LOGO_IMAGE)

    @allure.step("Check if the 'Logo' image is visible")
    def check_logo_image_visibility(self):
        return self.element_is_visible(self.locators.LOGO_IMAGE)

    @allure.step("Get attribute 'xmlns' of the 'Logo' image")
    def get_xmlns_of_logo_image(self):
        return self.element_is_present(self.locators.LOGO_IMAGE).get_attribute("xmlns")

    @allure.step("Get size values of the 'Logo' image")
    def get_sizes_of_logo_image(self):
        logo_image_sizes = self.get_image_size(self.locators.LOGO_IMAGE)
        # print(f"The sizes of the 'Logo' image are: {logo_image_sizes}")
        return logo_image_sizes

    @allure.step("""Get size of the 'Logo' image and check its changes after resizing""")
    def check_size_changes_of_logo_section(self):
        section_size_before = self.get_image_size(self.locators.LOGO_SECTION)
        # print(f"The sizes of the 'Logo' section are: {section_size_before}")
        self.driver.set_window_size(220, 1100)
        section_size_after = self.get_image_size(self.locators.LOGO_LINK)
        # print(f"The sizes of the 'Logo' section are: {section_size_after}")
        if section_size_before != section_size_after:
            changes = 1
            # print(f"\nThe 'Logo' section has sizes that changed: \nfrom {section_size_before} before "
            #       f"resizing \nto {section_size_after} after resizing")
        else:
            changes = 0
            # print("\nThe 'Logo' section has sizes that didn't change after resizing")
        return changes

    # Checks of the 'About' and the 'Telegram' links in the Section 2 in the Header
    @allure.step("Get the list of links in the Section 2 in the Header")
    def get_list_of_links_in_section_2(self):
        links = self.elements_are_present(self.locators.SECTION_2_LINKS)
        # print(f"\nAmount of links in the Section 2 is: {len(links)}")
        return links

    @allure.step("Check the 'About' and the 'Telegram' links are present and visible in the Section 2 in the Header")
    def check_links_visibility_in_section_2(self):
        links = self.get_list_of_links_in_section_2()
        all_links_are_displayed = all(link.is_displayed() for link in links)
        return all_links_are_displayed

    @allure.step("Check the 'About' and the 'Telegram' links are clickable in the Section 2 in the Header")
    def check_links_clickability_in_section_2(self):
        links = self.get_list_of_links_in_section_2()
        all_links_are_enabled = all(link.is_enabled() for link in links)
        return all_links_are_enabled

    @allure.step("Get attribute 'href' of the 'About' and the 'Telegram' links in the Section 2 in the Header")
    def get_links_href_in_section_2(self):
        links = self.get_list_of_links_in_section_2()
        links_href = [element.get_attribute("href") for element in links]
        return links_href

    @allure.step("Get status codes of the 'About' and the 'Telegram' links in the Section 2 in the Header")
    def get_links_status_code_in_section_2(self):
        links_href = self.get_links_href_in_section_2()
        links_status_code = [requests.head(link_href).status_code for link_href in links_href]
        return links_status_code

    @allure.step("""Click on the 'About' and the 'Telegram' links in the Section 2 in the Header 
    and thereby open corresponding web pages in the same or new tab""")
    def click_on_links_and_return_back(self):
        opened_pages = []
        self.element_is_present_and_clickable(self.locators.SECTION_2_LINK_ABOUT).click()
        opened_pages.append(self.driver.current_url)
        self.driver.back()
        opened_pages.append(self.driver.current_url)
        self.element_is_present_and_clickable(self.locators.SECTION_2_LINK_TELEGRAM).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        opened_pages.append(self.driver.current_url)
        self.driver.switch_to.window(self.driver.window_handles[0])
        opened_pages.append(self.driver.current_url)
        # print('\n', *opened_pages, sep='\n')
        return opened_pages

    @allure.step("Get the list of text in the 'About' and the 'Telegram' links in the Sections 2 in the Header")
    def get_text_in_links_in_section_2(self):
        links = self.get_list_of_links_in_section_2()
        links_text = [link.text for link in links]
        # print(f"Text of links in the Section 2 is:", *links_text, sep='\n')
        return links_text
