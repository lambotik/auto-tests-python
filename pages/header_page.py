"""Methods for verifying web elements in the Header on the site"""
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
        print(f"Amount of elements on the 1st level of nesting in the Header is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 1st level of nesting in the Header are: {tags}")
        return tags

    @allure.step("Check if elements of the 1st level of nesting are visible in the Header")
    def check_elements_visibility_on_1st_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_FIRST_LEVEL_ELEMENTS)
        display_of_all_elements = all(element.is_displayed() for element in elements)
        return display_of_all_elements

    @allure.step("Get structure of the 2nd level of nesting the Header")
    def get_structure_of_2nd_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_SECOND_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 2nd level of nesting in the Header is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 2nd level of nesting in the Header are: {tags}")
        return tags

    @allure.step("Check if elements of the 2nd level of nesting are visible in the Header")
    def check_elements_visibility_on_2nd_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_SECOND_LEVEL_ELEMENTS)
        display_of_all_elements = all(element.is_displayed() for element in elements)
        return display_of_all_elements

    @allure.step("Get structure of the 3rd level of nesting the Header")
    def get_structure_of_3rd_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_THIRD_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 3rd level of nesting in the Header is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 3rd level of nesting in the Header are: {tags}")
        return tags

    @allure.step("Check if elements on the 3rd level of nesting are visible in the Header")
    def check_elements_visibility_on_3rd_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_THIRD_LEVEL_ELEMENTS)
        display_of_all_elements = all(element.is_displayed() for element in elements)
        return display_of_all_elements

    @allure.step("Get structure of the 4th level of nesting the Header")
    def get_structure_of_4th_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_FOURTH_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 4th level of nesting in the Header is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 4th level of nesting in the Header are: {tags}")
        return tags

    @allure.step("Check if elements on the 4th level of nesting are visible in the Header")
    def check_elements_visibility_on_4th_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_FOURTH_LEVEL_ELEMENTS)
        display_of_all_elements = all(element.is_displayed() for element in elements)
        return display_of_all_elements

    @allure.step("Get structure of the 5th level of nesting the Header")
    def get_structure_of_5th_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_FIFTH_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 5th level of nesting in the Header is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 5th level of nesting in the Header are: {tags}")
        return tags

    @allure.step("Check if elements on the 5th level of nesting are visible in the Header")
    def check_elements_visibility_on_5th_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_FIFTH_LEVEL_ELEMENTS)
        display_of_elements_part = all(element.is_displayed() for element in elements[1:4])
        return display_of_elements_part

    @allure.step("Get structure of the 6th level of nesting the Header")
    def get_structure_of_6th_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_SIXTH_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 6th level of nesting in the Header is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 6th level of nesting in the Header are: {tags}")
        return tags

    @allure.step("Check if elements on the 6th level of nesting are invisible in the Header")
    def check_elements_invisibility_on_6th_level_in_header(self):
        elements = self.elements_are_present(self.locators.HEADER_SIXTH_LEVEL_ELEMENTS)
        non_display_of_all_elements = all(self.element_is_not_visible(element) for element in elements)
        return non_display_of_all_elements

# Checks of Logo in the Header
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
