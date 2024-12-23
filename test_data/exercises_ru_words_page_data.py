"""Data for verifying web elements on the 'Exercises "Words"' page on the 'ru' local"""
from test_data.links import MainPageLinks as Links


class ExercisesRuWordsPageData:
    tab_title = ["Речевые упражнения (готовы для занятий) | BrainUp", "Speech exercises | BrainUp"]
    tab_title_ru = "Речевые упражнения (готовы для занятий) | BrainUp"

    breadcrumbs = ['', 'Речевые упражнения (готовы для занятий)', 'Слова']
    group_links_text = ['СЛОВА', 'СЛОВА КОРОЛЁВОЙ', 'ПОХОЖИЕ ФРАЗЫ', 'ГРУППА СЛОВ', 'ПРЕДЛОЖЕНИЯ',
                        'ДИХОТИЧЕСКОЕ СЛУШАНИЕ', 'СЛОВА С ЧАСТОТНОЙ ГРУППИРОВКОЙ']
    cards_text = ['Семья', 'Любимый дом', 'Что я ем', 'Одежда', 'В школе', 'Математика', 'Домашние питомцы',
                  'Мир животных', 'Транспорт', 'Цвета и форма', 'В городе', 'В деревне', 'На прогулке', 'Погода',
                  'Стану кем хочу', 'Тело человека', 'Развлечения', 'Путешествия', 'В больнице', 'Что я чувствую',
                  'Игрушки', 'Насекомые', 'Интерьер', 'На кухне', 'Музыка', 'Музыкальные инструменты', 'Птицы',
                  'Украшения', 'История', 'Действия', 'Действия(слышимые)', 'Транспорт Дополнение',
                  'Транспорт (спецтехника)', 'Плодовые деревья и кусты', 'Растения', 'Деревья и кустарники',
                  'Спорт', 'В магазине', 'Парнокопытные', 'Породы собак', 'Канцелярские принадлежности', 'Цветы',
                  'Русский язык и литература', 'Физика', 'Биология', 'Инструменты']

    breadcrumbs_links_href = [
        f"{Links.URL_MAIN_PAGE}groups",
        f"{Links.URL_MAIN_PAGE}groups/2",
        f"{Links.URL_MAIN_PAGE}groups/2/series/1"
    ]

    a = ['https://www.brainup.site/groups',
         'https://www.brainup.site/groups/2',
         'https://www.brainup.site/groups/2/series/1']
