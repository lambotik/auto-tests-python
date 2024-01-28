from selenium.webdriver.common.by import By


class FooterLocators:
    FOOTER_ELEMENTS_LOCATORS = {
        "FOOTER_SECTION": (By.TAG_NAME, "footer"),
        "FOOTER_CONTENT": (By.XPATH, "(//footer//div)[1]"),
        "ARASAAC_LINK_SECTION": (By.XPATH, "(//footer//li)[3]"),
        "CONTACT_US_LINK_SECTION": (By.XPATH, "(//footer//div)[2]"),
        "EPAM_LINK_SECTION": (By.XPATH, "(//footer//li)[5]"),
        "JETBRAINS_LINK_SECTION": (By.XPATH, "(//footer//li)[1]"),
        "REG_LINK_SECTION": (By.XPATH, "(//footer//li)[2]"),
        "SELECTEL_LINK_SECTION": (By.XPATH, "(//footer//li)[4]"),
        "WITH_THE_SUPPORT_PHRASE_SECTION": (By.XPATH, "(//footer//div)[4]")
    }

    FOOTER_TEXT_LOCATORS = {
        "CONTACT_US_LINK_TEXT": (By.XPATH, "//footer//a[@title]"),
        "WITH_THE_SUPPORT_PHRASE_TEXT": (By.XPATH, "//span[@data-test-support-message]")
    }

    FOOTER_LINKS_LOCATORS = {
        "ARASAAC_LINK": (By.XPATH, "(//footer//li)[3]/a"),
        "CONTACT_US_LINK": (By.XPATH, "//footer//a[@title]"),
        "EPAM_LINK": (By.XPATH, "(//footer//li)[5]/a"),
        "JETBRAINS_LINK": (By.XPATH, "(//footer//li)[1]/a"),
        "REG_LINK": (By.XPATH, "(//footer//li)[2]/a"),
        "SELECTEL_LINK": (By.XPATH, "(//footer//li)[4]/a")
    }

    # Footer images locators
    ARASAAC_IMAGE = (By.XPATH, "(//footer//li)[3]//img")
    EPAM_IMAGE = (By.XPATH, "(//footer//li)[5]//img")
    JETBRAINS_IMAGE = (By.XPATH, "(//footer//li)[1]//img")
    REG_IMAGE = (By.XPATH, "(//footer//li)[2]//img")
    SELECTEL_IMAGE = (By.XPATH, "(//footer//li)[4]//img")

    # Footer elements locators
    ARASAAC_LINK = (By.XPATH, "(//footer//li)[3]/a")
    CONTACT_US_LINK = (By.XPATH, "//footer//a[@title]")
    EPAM_LINK = (By.XPATH, "(//footer//li)[5]/a")
    FOOTER_SECTION = (By.TAG_NAME, "footer")
    JETBRAINS_LINK = (By.XPATH, "(//footer//li)[1]/a")
    REG_LINK = (By.XPATH, "(//footer//li)[2]/a")
    SELECTEL_LINK = (By.XPATH, "(//footer//li)[4]/a")
    WITH_THE_SUPPORT_PHRASE_TEXT = (By.XPATH, "//span[@data-test-support-message]")

    # Related pages elements locators
    # on ARASAAC page
    ARASAAC_OWNER_TITLE = (By.XPATH, "(//h2)[1]")
