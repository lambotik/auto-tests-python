"""Data for verifying web elements on the 'Exercises "Words"' page on the 'ru' local"""
from test_data.links import MainPageLinks as Links
from test_data.links import ExercisesUrls as ExUrls


class ExercisesRuWordsPageData:
    tab_title = ["Речевые упражнения (готовы для занятий) | BrainUp", "Speech exercises | BrainUp"]
    tab_title_ru = "Речевые упражнения (готовы для занятий) | BrainUp"

    breadcrumbs = ['', 'Речевые упражнения (готовы для занятий)', 'Слова']

    group_links_text = ['СЛОВА', 'СЛОВА КОРОЛЁВОЙ', 'ПОХОЖИЕ ФРАЗЫ', 'ГРУППА СЛОВ', 'ПРЕДЛОЖЕНИЯ',
                        'ДИХОТИЧЕСКОЕ СЛУШАНИЕ', 'СЛОВА С ЧАСТОТНОЙ ГРУППИРОВКОЙ']

    group_link_titles = [
        'Распознавание слов', 'Слова по методическому пособию Инны Васильевны Королевой Учусь слушать и говорить',
        'Распознавание похожих фраз', 'Распознавание последовательности слов', 'Распознавание предложений',
        'Дихотическое слушание', 'Слова с частотной группировкой'
    ]

    group_link_active_links = ['Слова', 'Слова Королёвой', 'Похожие фразы', 'Группа слов', 'Предложения',
                               'Дихотическое слушание', 'Слова с частотной группировкой']

    subgroup_links_text = [
        'Семья', 'Любимый дом', 'Что я ем', 'Одежда', 'В школе',
        'Математика', 'Домашние питомцы', 'Мир животных',
        'Транспорт', 'Цвета и форма', 'В городе', 'В деревне',
        'На прогулке', 'Погода', 'Стану кем хочу', 'Тело человека',
        'Развлечения', 'Путешествия', 'В больнице',
        'Что я чувствую', 'Игрушки', 'Насекомые', 'Интерьер', 'На кухне', 'Музыка',
        'Музыкальные инструменты', 'Птицы', 'Украшения', 'История', 'Действия', 'Действия(слышимые)',
        'Транспорт Дополнение', 'Транспорт (спецтехника)', 'Плодовые деревья и кусты', 'Растения',
        'Деревья и кустарники', 'Спорт', 'В магазине', 'Парнокопытные', 'Породы собак', 'Канцелярские принадлежности',
        'Цветы', 'Русский язык и литература', 'Физика', 'Биология', 'Инструменты'
    ]

    subgroup_link_titles = [
        'Слова про семью', 'Слова про дом', 'Слова о еде', 'Слова об одежде', 'Слова о школе и учёбе',
        'Математика и её термины', 'Слова о домашних питомцах', 'Слова о животных',
        'Слова о транспорте', 'Слова о понятиях цета и формы', 'Слова о жизни города', 'Слова из деревенской жизни',
        'Слова о прогулке', 'Слова о погоде', 'Слова о профессии', 'Слова об организме',
        'Слова из нашей жизни развлеченийи и игр', 'Слова из мира путешествий', 'Слова медицинские',
        'Слова о чувствах и эмоциях', 'Игрушки', 'Насекомые', 'Интерьер', 'На кухне', 'Музыка',
        'Музыкальные инструменты', 'Птицы', 'Украшения', 'История', 'Действия', 'Действия(слышимые)',
        'Транспорт Дополнение', 'Транспорт (спецтехника)', 'Плодовые деревья и кусты', 'Растения',
        'Деревья и кустарники', 'Спорт', 'В магазине', 'Парнокопытные', 'Породы собак', 'Канцелярские принадлежности',
        'Цветы', 'Русский язык и литература', 'Физика', 'Биология', 'Инструменты'
    ]

    breadcrumbs_urls = [
        f"{Links.URL_GROUPS_PAGE}",
        f"{Links.URL_GROUPS_PAGE}/2",
        f"{Links.URL_GROUPS_PAGE}/2/series/1"
    ]

    subgroup_links_href = [
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/1",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/2",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/3",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/4",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/5",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/6",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/7",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/8",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/9",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/10",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/11",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/12",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/13",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/14",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/15",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/16",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/17",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/18",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/19",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/20",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/21",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/22",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/23",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/24",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/25",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/26",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/27",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/28",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/29",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/30",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/31",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/32",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/33",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/34",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/35",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/36",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/37",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/38",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/39",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/40",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/41",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/42",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/43",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/44",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/45",
        f"{ExUrls.URL_EXERCISES_RU_WORDS_PAGE}/subgroup/46"
    ]

    links_status_code = 200
