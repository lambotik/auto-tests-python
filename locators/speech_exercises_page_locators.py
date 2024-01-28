from selenium.webdriver.common.by import By


class AuthorizedUserHomePageLocators:
    """
    link: https://brainup.site/groups
    """
    # Header
    EN_BUTTON = (By.XPATH, "//*[contains(text(),'EN')]")
    RU_BUTTON = (By.XPATH, "//*[contains(text(),'RU')]")
    PROFILE_USER = (By.XPATH, '//a[@href="/profile"]')

    SPEECH_EXERCISES_RU = (By.XPATH, '//a[@title="Речевые упражнения"]')
    SPEECH_EXERCISES_EN = (By.XPATH, '//a[@title="Speech"]')


class SpeechExercisesPageLocators:
    """
    link: https://brainup.site/groups/2/series/1
    """
    BUTTON_INTERACT = (By.XPATH, '//*[text()="Interact"]')
    BUTTON_SOLVE = (By.XPATH, '//*[text()="Solve"]')
    BUTTON_START_EN = (By.XPATH, '//button[@aria-label="Start exercise"]')
    BUTTON_START_RU = (By.XPATH, '//button[@aria-label="Начать выполнение упражнения"]')
    LIST_WORDS_IN_CARD = (By.XPATH, '//li[@class="task-player__option flex"]')
    LIST_WORDS_FOR_GROUP_WORDS = (By.XPATH, '//div[@class="flex justify-center flex-grow mt-4"]//span')
    PROGRESS_BAR = (By.XPATH, '//div[@class="progress-bar"]')

    # Speech exercises_EN Header
    WORDS_BUTTON_EN = (By.XPATH, '//button[@data-test-active-link="Words"]')
    SIMILAR_PHRASES_EN = (By.XPATH, '//button[@data-test-active-link="Similar phrases"]')

    # Speech exercises_RU Header
    WORDS_BUTTON_RU = (By.XPATH, '//button[@data-test-active-link="Слова"]')
    WORDS_BY_KOROLEVA_BUTTON = (By.XPATH, '//button[@data-test-active-link="Слова Королёвой"]')
    WORDS_SIMILAR_PHRASES_RU = (By.XPATH, '//button[@title="Распознавание похожих фраз"]')
    WORDS_GROUP_RU = (By.XPATH, '//button[@title="Распознавание последовательности слов"]')
    SENTENCES_RU = (By.XPATH, '//button[@title="Распознавание предложений"]')
    WORDS_WITH_FREQUENCY_GROUPING_RU = (By.XPATH, '//button[@title="Слова с частотной группировкой"]')
    LIST_OF_LESSONS = (By.XPATH, '//div[contains(@class, "series-container")]//a/div/div')

    WORDS_EN = (By.XPATH, '//button[@data-test-active-link="Words"]')

    # WORDS
    LIST_OF_CARD_FROM_WORDS = (
        By.XPATH,
        '//div[@class="sm:tracking-normal sm:leading-normal sm:text-base '
        'text-xs leading-none tracking-tighter text-center"]')

    # Слова
    LIST_OF_CARD_FROM_WORDS_RU = (By.XPATH,
                                  '//div[@class ="sm:grid-cols-4 gap-y-2 sm:gap-y-3 grid grid-cols-3 mx-2 mb-4"] / a')
