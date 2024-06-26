"""Locators of web elements on the 'Specialists' page"""

from selenium.webdriver.common.by import By


class SpecialistsPageLocators:
    ALL_SPECIALISTS_LINK = (By.XPATH, "//div[contains(@class, 'mt-20')]/a")
    # GRID_CARD_IMAGES = (By.XPATH, "//img[@class='rounded-full']")
    GRID_CARD_IMAGES = (By.XPATH, "//section//img")
    GRID_CARD_TEXT_SECTIONS = (By.XPATH, "//div[@class='flex-1']")
    GRID_CARD_01_IMAGE = (By.XPATH, "(//img[@class='rounded-full'])[1]")
    PAGE_GRID = (By.XPATH, "//div[contains(@class, 'grid')]")
    PAGE_GRID_CONTENT = (By.XPATH, "//div[contains(@class, 'rounded-lg')]")
    PAGE_TEXT = (By.XPATH, "//div[contains(@class, 'text-lg')]")
    PAGE_TITLE = (By.TAG_NAME, "h2")
    SPECIALIST_NAMES = (By.XPATH, "//div[contains(@class, 'mb-4')]")
    SPECIALIST_PROFESSION_SECTIONS = (By.XPATH, "//div[@class='font-openSans']")
