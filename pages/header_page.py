"""Methods for verifying web elements in the Header of the site"""
import allure
import requests
from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators


class HeaderPage(BasePage):
    locators = HeaderPageLocators

    # Checking the structure and display of elements in the Header
    @allure.step("Check the Header is present in the DOM tree on the page")
    def check_header_presence(self):
        return self.element_is_present(self.locators.HEADER_CONTENT)

    @allure.step("Check if the Header is visible on the page")
    def check_header_visibility(self):
        return self.element_is_visible(self.locators.HEADER_CONTENT)

    @allure.step("Get structure of the 1st level of nesting in the Header")
    def get_structure_of_1st_level(self):
        elements = self.elements_are_present(self.locators.HEADER_FIRST_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 1st level of nesting in the Header are: {tags}")
        return elements

    @allure.step("Check if elements of the 1st level of nesting are visible")
    def check_elements_visibility_on_1st_level_on_page(self):
        elements = self.elements_are_present(self.locators.HEADER_FIRST_LEVEL_ELEMENTS)
        display_of_all_elements = all(element.is_displayed() for element in elements)
        return display_of_all_elements

    @allure.step("Get structure of the 2nd level of nesting the Header")
    def get_structure_of_2nd_level(self):
        elements = self.elements_are_present(self.locators.HEADER_SECOND_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 2nd level of nesting in the Header are: {tags}")
        return elements

    @allure.step("Check if elements of the 2nd level of nesting are visible")
    def check_elements_visibility_on_2nd_level_on_page(self):
        elements = self.elements_are_present(self.locators.HEADER_SECOND_LEVEL_ELEMENTS)
        display_of_all_elements = all(element.is_displayed() for element in elements)
        return display_of_all_elements

    @allure.step("Get structure of the 3rd level of nesting the Header")
    def get_structure_of_3rd_level(self):
        elements = self.elements_are_present(self.locators.HEADER_THIRD_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 3rd level of nesting in the Header are: {tags}")
        return elements

    @allure.step("Check if elements on the 3rd level of nesting are visible")
    def check_elements_visibility_on_3rd_level_on_page(self):
        elements = self.elements_are_present(self.locators.HEADER_THIRD_LEVEL_ELEMENTS)
        display_of_all_elements = all(element.is_displayed() for element in elements)
        return display_of_all_elements

    @allure.step("Get structure of the 4th level of nesting the Header")
    def get_structure_of_4th_level(self):
        elements = self.elements_are_present(self.locators.HEADER_FOURTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 4th level of nesting in the Header are: {tags}")
        return elements

    @allure.step("Check if elements on the 4th level of nesting are visible")
    def check_elements_visibility_on_4th_level_on_page(self):
        elements = self.elements_are_present(self.locators.HEADER_FOURTH_LEVEL_ELEMENTS)
        display_of_all_elements = all(element.is_displayed() for element in elements)
        return display_of_all_elements

    @allure.step("Get structure of the 5th level of nesting the Header")
    def get_structure_of_5th_level(self):
        elements = self.elements_are_present(self.locators.HEADER_FIFTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 5th level of nesting in the Header are: {tags}")
        return elements

    @allure.step("Check if elements on the 5th level of nesting are visible")
    def check_elements_visibility_on_5th_level_on_page(self):
        elements = self.elements_are_present(self.locators.HEADER_FIFTH_LEVEL_ELEMENTS)
        display_of_elements_part = all(element.is_displayed() for element in elements[1:4])
        return display_of_elements_part

    @allure.step("Get structure of the 6th level of nesting the Header")
    def get_structure_of_6th_level(self):
        elements = self.elements_are_present(self.locators.HEADER_SIXTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 6th level of nesting in the Header are: {tags}")
        return elements

    @allure.step("Check if elements on the 6th level of nesting are invisible")
    def check_elements_invisibility_on_6th_level_on_page(self):
        elements = self.elements_are_present(self.locators.HEADER_SIXTH_LEVEL_ELEMENTS)
        # non_display_of_all_elements = all(self.element_is_not_visible(element) for element in elements)
        return all(self.element_is_not_visible(element) for element in elements)

    @allure.step("Get the list of links on different levels of nesting in the Header")
    def get_list_of_links(self):
        return self.elements_are_present(self.locators.HEADER_LINKS)

    @allure.step("Check the 'Logo' link is present in the Header")
    def check_logo_link_presence(self):
        return self.element_is_present(self.locators.LOGO_LINK)

    @allure.step("Check the 'Logo' link is visible")
    def check_logo_link_visibility(self):
        return self.element_is_visible(self.locators.LOGO_LINK)

    @allure.step("Get the list of links in the section 2 in the Header")
    def get_list_of_links_in_section2(self):
        return self.elements_are_present(self.locators.SECTION_2_LINKS)

    @allure.step("Check the 'About' and the 'Telegram' links are visible")
    def check_links_visibility_in_section2(self):
        return all(link.is_displayed() for link in self.get_list_of_links_in_section2())

    @allure.step("Get structure of the 'ru-en' section in the Header")
    def get_structure_of_ru_en_section(self):
        # tags = [element.tag_name for element in elements]
        return self.elements_are_present(self.locators.RU_EN_BUTTONS_SECTION)

    @allure.step("Check if elements in the 'ru-en' section are visible")
    def check_elements_visibility_in_ru_en_section(self):
        return all(element.is_displayed() for element in self.get_structure_of_ru_en_section())

    @allure.step("Check if the 'Logo' image is present")
    def check_logo_image_presence(self):
        return self.element_is_present(self.locators.LOGO_IMAGE)

    @allure.step("Check if the 'Logo' image is visible")
    def check_logo_image_visibility(self):
        return self.element_is_visible(self.locators.LOGO_IMAGE)

    # Checking links in the Header
    @allure.step("Check if links are clickable in the Header")
    def check_links_clickability(self):
        return all(link.is_enabled() for link in self.get_list_of_links())

    @allure.step("Get attribute 'href' of links in the Header")
    def get_links_href(self):
        return [element.get_attribute("href") for element in self.get_list_of_links()]

    @allure.step("Get status codes of links in the Header")
    def get_links_status_codes(self):
        return [requests.head(link_href).status_code for link_href in self.get_links_href()]

    @allure.step("Click on the 'Logo' link")
    def click_logo_link(self):
        self.element_is_present_and_clickable(self.locators.LOGO_LINK).click()
        return self.driver.current_url

    # Checking images in the Header
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
        links = self.get_list_of_links_in_section2()
        links_text = [link.text for link in links]
        # print(f"Text of links in the Section 2 is:", *links_text, sep='\n')
        return links_text
