"""Auto tests for verifying web elements in the Footer on pages"""
import allure
from pages.footer_page import FooterPage
from test_data.links import SpecificExercisesUrls
from test_data.footer_data import FooterData


@allure.epic("Test Footer")
class TestFooter:
    class TestFooterStructure:
        @allure.title("Verify presence and visibility of the Footer")
        def test_fp_01_01_verify_footer_presence_and_visibility(self, driver, main_page_open):
            page = FooterPage(driver)
            footer_presence = page.check_footer_presence()
            footer_visibility = page.check_footer_visibility()
            assert footer_presence is not None, "The Footer is absent in DOM"
            assert footer_visibility, "The Footer is invisible"

        @allure.title("Verify composition and visibility of elements on the 1st-7th levels of nesting in the Footer")
        def test_fp_01_02_verify_footer_structure_and_visibility(self, driver, main_page_open):
            page = FooterPage(driver)
            structure_of_1st_level = page.get_structure_of_1st_level()
            visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level_on_page()
            structure_of_2nd_level = page.get_structure_of_2nd_level()
            visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level_on_page()
            structure_of_3rd_level = page.get_structure_of_3rd_level()
            visibility_of_elements_on_3rd_level = page.check_elements_visibility_on_3rd_level_on_page()
            structure_of_4th_level = page.get_structure_of_4th_level()
            visibility_of_elements_on_4th_level = page.check_elements_visibility_on_4th_level_on_page()
            structure_of_5th_level = page.get_structure_of_5th_level()
            visibility_of_elements_on_5th_level = page.check_elements_visibility_on_5th_level_on_page()
            structure_of_6th_level = page.get_structure_of_6th_level()
            visibility_of_elements_on_6th_level = page.check_elements_visibility_on_6th_level_on_page()
            structure_of_7th_level = page.get_structure_of_7th_level()
            visibility_of_elements_on_7th_level = page.check_elements_visibility_on_7th_level_on_page()
            assert structure_of_1st_level, "The Footer is empty"
            assert visibility_of_elements_on_1st_level, "1st-level elements are invisible"
            assert structure_of_2nd_level, "Elements on the 2nd level are absent on the page"
            assert visibility_of_elements_on_2nd_level, "2nd-level elements are invisible"
            assert structure_of_3rd_level, "Elements on the 3rd level are absent on the page"
            assert visibility_of_elements_on_3rd_level, "3rd-level elements are invisible"
            assert structure_of_4th_level, "Elements on the 4th level are absent on the page"
            assert visibility_of_elements_on_4th_level, "4th-level elements are invisible"
            assert structure_of_5th_level, "Elements on the 5th level are absent on the page"
            assert visibility_of_elements_on_5th_level, "5th-level elements are invisible"
            assert structure_of_6th_level, "Elements on the 6th level are absent on the page"
            assert visibility_of_elements_on_6th_level, "6th-level elements are invisible"
            assert structure_of_7th_level, "Elements on the 7th level are absent on the page"
            assert visibility_of_elements_on_7th_level, "7th-level elements are invisible"

        @allure.title("Verify presence, visibility of text, links, images in the Footer")
        def test_fp_01_03_verify_footer_structural_elements(self, driver, main_page_open):
            page = FooterPage(driver)
            text_on_4th_level = page.check_text_presence()
            text_visibility = page.check_text_visibility()
            links_on_3rd_and_6th_levels = page.get_list_of_links()
            links_visibility = page.check_links_visibility()
            images_on_7th_level = page.get_list_of_images()
            images_visibility = page.check_images_visibility()
            assert text_on_4th_level, "The text on the 4th level is absent in the Footer"
            assert text_visibility, "The text on the 4th level is invisible"
            assert links_on_3rd_and_6th_levels, "Links on the 3rd and 6th levels are absent in the Footer"
            assert links_visibility, "Links on the 3rd and 6th levels are invisible"
            assert images_on_7th_level, "Images on the 7th level are absent in the Footer"
            assert images_visibility, "Images on the 7th level are invisible"

    class TestFooterText:
        @allure.title("Verify content of text in the Footer")
        def test_fp_02_01_verify_footer_text(self, driver, main_page_open):
            page = FooterPage(driver)
            text_content = page.get_footer_text()
            assert text_content, "The text content in the Footer is empty"
            assert text_content in FooterData.with_the_support_text, "Text in the Footer mismatches the valid value"

        @allure.title("Verify text in the 'Contact us' link in the Footer")
        def test_fp_02_02_verify_text_in_links(self, driver, main_page_open):
            page = FooterPage(driver)
            link_text = page.get_text_in_contact_us_link()
            assert link_text, "Text in the link is empty"
            assert link_text in FooterData.contact_us_link_text, "Text in the link mismatches the valid value"

    class TestFooterLinks:
        @allure.title("Verify clickability, href, prefix and subject, status code of links in the Footer")
        def test_fp_03_01_verify_footer_links(self, driver, main_page_open):
            page = FooterPage(driver)
            links_clickability = page.check_links_clickability()
            links_href = page.get_links_href()
            link_prefix_and_subject = page.check_contact_us_link_href()
            link_status_codes = page.get_supporter_links_status_codes()
            assert links_clickability, "Links are unclickable"
            assert links_href, "Links href are empty"
            assert all(link_href in FooterData.links_href for link_href in links_href), \
                "Attributes 'href' of links mismatch valid values"
            assert link_prefix_and_subject, \
                "The attribute 'href' of the 'Contact us' link does not contain the proper prefix and/or subject"
            assert all(status_code in FooterData.link_status_codes for status_code in link_status_codes), \
                "Status codes of links mismatch valid values"

        @allure.title("Verify that links in the Footer lead to correct pages after clicking")
        def test_fp_03_02_verify_links_lead_to_the_correct_pages(self, driver, main_page_open):
            page = FooterPage(driver)
            new_tabs_urls = page.click_on_links()
            assert all(tab_url in FooterData.pages_urls for tab_url in new_tabs_urls), \
                "Links in the Footer lead to incorrect pages after clicking or did not loaded during the allotted time"

        @allure.title("Verify that the 'Contact us' link in the Footer calls an email client")
        def test_fp_03_03_verify_contact_us_link_calls_an_email_client(self, driver, main_page_open):
            page = FooterPage(driver)
            page.click_contact_us_link()
            assert True, "the 'Contact us' link in the Footer does not call an email client"

    class TestFooterForAuthorizedUserOnly:

        @allure.title("Verify Footer invisibility through the modal window with the exercise")
        def test_fp_02_01_01_verify_footer_invisibility_through_the_modal_window(self, driver, auto_test_user_authorized):
            modal_window_page = FooterPage(driver, SpecificExercisesUrls.URL_OF_EXERCISE_1_MODAL_WINDOW_PAGE)
            modal_window_page.open()
            assert (modal_window_page.check_footer_presence() and modal_window_page.check_jetbrains_image_presence()), \
                "Footer (including the Jetbrains image) is absent in the DOM tree"
            assert (modal_window_page.check_footer_invisibility()
                    and modal_window_page.check_jetbrains_image_invisibility()), \
                "Footer (including the Jetbrains image) is visible through the modal window"

    class TestFooterImages:
        @allure.title("Verify accuracy of the ARASAAC link's image in Footer")
        def test_fp_04_01_verify_arasaac_link_image(self, driver, main_page_open):
            page = FooterPage(driver)
            link_image_src = page.get_arasaac_image_src()
            link_image_alt = page.get_arasaac_image_alt()
            assert link_image_src, "The 'src' attribute value of the ARASAAC link's image is empty"
            assert link_image_src == FooterData.footer_images_src["arasaac_img_src"], \
                "The 'src' attribute value of the ARASAAC link image is unaccurate"
            assert link_image_alt, "The 'alt' attribute value of the ARASAAC link image is empty"
            assert link_image_alt == FooterData.footer_images_alt["arasaac_img_alt"], \
                "The ARASAAC link image is unaccurate"

        @allure.title("Verify visible sizes of the ARASAAC link's image in Footer")
        def test_fp_04_02_verify_visible_sizes_of_arasaac_link_image(self, driver, main_page_open):
            page = FooterPage(driver)
            link_href = page.get_arasaac_link_href()
            image_width = page.get_visible_width_of_arasaac_image()
            image_height = page.get_visible_height_of_arasaac_image()
            # print(f"The current visible sizes of the picture in the {link_href} link are: "
            #       f"{image_width}x{image_height} px")
            assert image_width != 0, \
                f"The image in the {link_href} link in Footer is invisible, a reason: image width = 0"
            assert image_height != 0, \
                f"The image in the {link_href} link in Footer is invisible, a reason: image height = 0"

        @allure.title("Verify changes of visible sizes of the ARASAAC link's image in Footer")
        def test_fp_04_03_verify_changes_of_visible_sizes_of_arasaac_link_image(self, driver, main_page_open):
            page = FooterPage(driver)
            link_href = page.get_arasaac_link_href()
            image_width = page.get_visible_width_of_arasaac_image()
            image_height = page.get_visible_height_of_arasaac_image()
            # print(f"The current visible sizes of the picture in the {link_href} link are: "
            #       f"{image_width}x{image_height} px")
            driver.set_window_size(504, 638)
            image_width_new = page.get_visible_width_of_arasaac_image()
            image_height_new = page.get_visible_height_of_arasaac_image()
            # print(f"The new visible sizes of the picture in the {link_href} link are: "
            #       f"{image_width_new}x{image_height_new} px")
            assert image_width != image_width_new, \
                f"The image width in the {link_href} link in Footer has not changed due to resizing"
            assert image_height == image_height_new, \
                f"The image height in the {link_href} link in Footer has changed due to resizing"

        @allure.title("Verify accuracy of the EPAM link's image in Footer")
        def test_fp_04_04_verify_epam_link_image(self, driver, main_page_open):
            page = FooterPage(driver)
            link_image_src = page.get_epam_image_src()
            link_image_alt = page.get_epam_image_alt()
            assert link_image_src, "The 'src' attribute value of the EPAM link's image is empty"
            assert link_image_src == FooterData.footer_images_src["epam_img_src"], \
                "The 'src' attribute value of the EPAM link image is unaccurate"
            assert link_image_alt, "The 'alt' attribute value of the EPAM link image is empty"
            assert link_image_alt == FooterData.footer_images_alt["epam_img_alt"], \
                "The EPAM link image is unaccurate"

        @allure.title("Verify visible sizes of the EPAM link's image in Footer")
        def test_fp_04_05_verify_visible_sizes_of_epam_link_image(self, driver, main_page_open):
            page = FooterPage(driver)
            link_href = page.get_epam_link_href()
            image_width = page.get_visible_width_of_epam_image()
            image_height = page.get_visible_height_of_epam_image()
            # print(f"The current visible sizes of the picture in the {link_href} link are: "
            #       f"{image_width}x{image_height} px")
            assert image_width != 0, \
                f"The image in the {link_href} link in Footer is invisible, a reason: image width = 0"
            assert image_height != 0, \
                f"The image in the {link_href} link in Footer is invisible, a reason: image height = 0"

        @allure.title("Verify changes of visible sizes of the EPAM link's image in Footer")
        def test_fp_04_06_verify_changes_of_visible_sizes_of_epam_link_image(self, driver, main_page_open):
            page = FooterPage(driver)
            link_href = page.get_epam_link_href()
            image_width = page.get_visible_width_of_epam_image()
            image_height = page.get_visible_height_of_epam_image()
            # print(f"The current visible sizes of the picture in the {link_href} link are: "
            #       f"{image_width}x{image_height} px")
            driver.set_window_size(504, 638)
            image_width_new = page.get_visible_width_of_epam_image()
            image_height_new = page.get_visible_height_of_epam_image()
            # print(f"The new visible sizes of the picture in the {link_href} link are: "
            #       f"{image_width_new}x{image_height_new} px")
            assert image_width != image_width_new, \
                f"The image width in the {link_href} link in Footer has not changed due to resizing"
            assert image_height == image_height_new, \
                f"The image height in the {link_href} link in Footer has changed due to resizing"

        @allure.title("Verify accuracy of the JETBRAINS link's image in Footer")
        def test_fp_04_07_verify_jetbrains_link_image(self, driver, main_page_open):
            page = FooterPage(driver)
            link_image_src = page.get_jetbrains_image_src()
            link_image_alt = page.get_jetbrains_image_alt()
            assert link_image_src == FooterData.footer_images_src["jetbrains_img_src"], \
                "The 'src' attribute value of the JETBRAINS link image is unaccurate"
            assert link_image_alt, "The 'alt' attribute value of the JETBRAINS link image is empty"
            assert link_image_alt == FooterData.footer_images_alt["jetbrains_img_alt"], \
                "The JETBRAINS link image is unaccurate"

        @allure.title("Verify visible sizes of the JETBRAINS link's image in Footer")
        def test_fp_04_08_verify_visible_sizes_of_jetbrains_link_image(self, driver, main_page_open):
            page = FooterPage(driver)
            link_href = page.get_jetbrains_link_href()
            image_width = page.get_visible_width_of_jetbrains_image()
            image_height = page.get_visible_height_of_jetbrains_image()
            # print(f"The current visible sizes of the picture in the {link_href} link are: "
            #       f"{image_width}x{image_height} px")
            assert image_width != 0, \
                f"The image in the {link_href} link in Footer is invisible, a reason: image width = 0"
            assert image_height != 0, \
                f"The image in the {link_href} link in Footer is invisible, a reason: image height = 0"

        @allure.title("Verify changes of visible sizes of the JETBRAINS link's image in Footer")
        def test_fp_04_09_verify_changes_of_visible_sizes_of_jetbrains_link_image(self, driver, main_page_open):
            page = FooterPage(driver)
            link_href = page.get_jetbrains_link_href()
            image_width = page.get_visible_width_of_jetbrains_image()
            image_height = page.get_visible_height_of_jetbrains_image()
            # print(f"The current visible sizes of the picture in the {link_href} link are: "
            #       f"{image_width}x{image_height} px")
            driver.set_window_size(504, 638)
            image_width_new = page.get_visible_width_of_jetbrains_image()
            image_height_new = page.get_visible_height_of_jetbrains_image()
            # print(f"The new visible sizes of the picture in the {link_href} link are: "
            #       f"{image_width_new}x{image_height_new} px")
            assert image_width != image_width_new, \
                f"The image width in the {link_href} link in Footer has not changed due to resizing"
            assert image_height == image_height_new, \
                f"The image height in the {link_href} link in Footer has changed due to resizing"

        @allure.title("Verify accuracy of the REG.RU link's image in Footer")
        def test_fp_04_10_verify_reg_link_image(self, driver, main_page_open):
            page = FooterPage(driver)
            link_image_src = page.get_reg_image_src()
            link_image_alt = page.get_reg_image_alt()
            assert link_image_src == FooterData.footer_images_src["reg_img_src"], \
                "The 'src' attribute value of the REG.RU link image is unaccurate"
            assert link_image_alt, "The 'alt' attribute value of the REG.RU link image is empty"
            assert link_image_alt == FooterData.footer_images_alt["reg_img_alt"], "The REG.RU link image is unaccurate"

        @allure.title("Verify visible sizes of the REG.RU link's image in Footer")
        def test_fp_04_11_verify_visible_sizes_of_reg_link_image(self, driver, main_page_open):
            page = FooterPage(driver)
            link_href = page.get_reg_link_href()
            image_width = page.get_visible_width_of_reg_image()
            image_height = page.get_visible_height_of_reg_image()
            # print(f"The current visible sizes of the picture in the {link_href} link are: "
            #       f"{image_width}x{image_height} px")
            assert image_width != 0, \
                f"The image in the {link_href} link in Footer is invisible, a reason: image width = 0"
            assert image_height != 0, \
                f"The image in the {link_href} link in Footer is invisible, a reason: image height = 0"

        @allure.title("Verify changes of visible sizes of the REG.RU link's image in Footer")
        def test_fp_04_12_verify_changes_of_visible_sizes_of_reg_link_image(self, driver, main_page_open):
            page = FooterPage(driver)
            link_href = page.get_reg_link_href()
            image_width = page.get_visible_width_of_reg_image()
            image_height = page.get_visible_height_of_reg_image()
            # print(f"The current visible sizes of the picture in the {link_href} link are: "
            #       f"{image_width}x{image_height} px")
            driver.set_window_size(504, 638)
            image_width_new = page.get_visible_width_of_reg_image()
            image_height_new = page.get_visible_height_of_reg_image()
            # print(f"The new visible sizes of the picture in the {link_href} link are: "
            #       f"{image_width_new}x{image_height_new} px")
            assert image_width != image_width_new, \
                f"The image width in the {link_href} link in Footer has not changed due to resizing"
            assert image_height == image_height_new, \
                f"The image height in the {link_href} link in Footer has changed due to resizing"

        @allure.title("Verify accuracy of the Selectel link's image in Footer")
        def test_fp_04_13_verify_selectel_link_image(self, driver, main_page_open):
            page = FooterPage(driver)
            link_image_src = page.get_selectel_image_src()
            link_image_alt = page.get_selectel_image_alt()
            assert link_image_src == FooterData.footer_images_src["selectel_img_src"], \
                "The 'src' attribute value of the Selectel link image is unaccurate"
            assert link_image_alt, "The 'alt' attribute value of the Selectel link image is empty"
            assert link_image_alt == FooterData.footer_images_alt["selectel_img_alt"], \
                "The Selectel link image is unaccurate"

        @allure.title("Verify visible sizes of the Selectel link's image in Footer")
        def test_fp_04_14_verify_visible_sizes_of_selectel_link_image(self, driver, main_page_open):
            page = FooterPage(driver)
            link_href = page.get_selectel_link_href()
            image_width = page.get_visible_width_of_selectel_image()
            image_height = page.get_visible_height_of_selectel_image()
            # print(f"The current visible sizes of the picture in the {link_href} link are: "
            #       f"{image_width}x{image_height} px")
            assert image_width != 0, \
                f"The image in the {link_href} link in Footer is invisible, a reason: image width = 0"
            assert image_height != 0, \
                f"The image in the {link_href} link in Footer is invisible, a reason: image height = 0"

        @allure.title("Verify changes of visible sizes of the Selectel link's image in Footer")
        def test_fp_04_15_verify_changes_of_visible_sizes_of_selectel_link_image(self, driver, main_page_open):
            page = FooterPage(driver)
            link_href = page.get_selectel_link_href()
            image_width = page.get_visible_width_of_selectel_image()
            image_height = page.get_visible_height_of_selectel_image()
            # print(f"The current visible sizes of the picture in the {link_href} link are: "
            #       f"{image_width}x{image_height} px")
            driver.set_window_size(504, 638)
            image_width_new = page.get_visible_width_of_selectel_image()
            image_height_new = page.get_visible_height_of_selectel_image()
            # print(f"The new visible sizes of the picture in the {link_href} link are: "
            #       f"{image_width_new}x{image_height_new} px")
            assert image_width != image_width_new, \
                f"The image width in the {link_href} link in Footer has not changed due to resizing"
            assert image_height == image_height_new, \
                f"The image height in the {link_href} link in Footer has changed due to resizing"
