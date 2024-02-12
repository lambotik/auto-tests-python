from selenium.webdriver.common.by import By


class UsedResourcesPageLocators:
    PAGE_TITLE = (By.TAG_NAME, "h1")
    PAGE_TEXT = (By.XPATH, "//section/p")
    LINKS_SECTION = (By.XPATH, "//section/ul")