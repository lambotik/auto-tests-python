"""Auto tests for verifying web elements on the 'Exercises "Similar phrases"' page on the 'ru' local"""
import allure
from pages.exercises_ru_similar_phrases_page import ExercisesRuSimilarPhrasesPage


@allure.epic("The Exercises 'Similar phrases' Page on the 'ru' local")
class TestExercisesRuSimilarPhrasesPage:
    class TestExRuSimPhrPageStructure:
        @allure.title("Verify presence and visibility of content on the page")
        def test_ersp_01_01_verify_page_presence_and_visibility(self, driver, exercises_ru_similar_phrases_page_open):
            page = ExercisesRuSimilarPhrasesPage(driver)
            page_content_presence = page.check_presence_of_page_content()
            page_content_visibility = page.check_visibility_of_page_content()
            assert page_content_presence, "The page content is absent in DOM"
            assert page_content_visibility, "The page content is invisible"

        @allure.title("Verify composition, visibility of elements on the 1st-7th levels of nesting on the page")
        def test_ersp_01_02_verify_page_structure_and_visibility(self, driver, exercises_ru_similar_phrases_page_open):
            page = ExercisesRuSimilarPhrasesPage(driver)
            structure_of_1st_level = page.get_structure_of_1st_level()
            visibility_of_elements_on_1st_level = page.check_elements_visibility_on_1st_level()
            structure_of_2nd_level = page.get_structure_of_2nd_level()
            visibility_of_elements_on_2nd_level = page.check_elements_visibility_on_2nd_level()
            structure_of_3rd_level = page.get_structure_of_3rd_level()
            visibility_of_elements_on_3rd_level = page.check_elements_visibility_on_3rd_level()
            structure_of_4th_level = page.get_structure_of_4th_level()
            visibility_of_elements_on_4th_level = page.check_elements_visibility_on_4th_level()
            structure_of_5th_level = page.get_structure_of_5th_level()
            visibility_of_elements_on_5th_level = page.check_elements_visibility_on_5th_level()
            structure_of_6th_level = page.get_structure_of_6th_level()
            visibility_of_elements_on_6th_level = page.check_elements_visibility_on_6th_level()
            structure_of_7th_level = page.get_structure_of_7th_level()
            visibility_of_elements_on_7th_level = page.check_elements_visibility_on_7th_level()
            assert structure_of_1st_level, "The page is empty"
            assert visibility_of_elements_on_1st_level, "1th-level elements are invisible"
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

        @allure.title("Verify presence, visibility of lists on the page")
        def test_erw_01_03_verify_page_structural_elements(self, driver, exercises_ru_similar_phrases_page_open):
            page = ExercisesRuSimilarPhrasesPage(driver)
            list1_on_5th_level = page.get_list1_of_breadcrumbs_links()
            list1_visibility = page.check_list1_visibility()
            assert list1_on_5th_level, "The list1 on the 5th level is absent on the page"
            assert list1_visibility, "The list1 on the 5th level is invisible"
