import json
import random

import allure
import requests

from locators.speech_exercises_page_locators import SpeechExercisesPageLocators
from pages.base_page import BasePage

authorization_url = ('https://www.googleapis.com/identitytoolkit/v3/'
                     'relyingparty/verifyPassword?key=AIzaSyCxu7mVxd_waBDUn9VKblBl4zl8MX5WxWY')
data_specialist_user = {"email": "autoTestSpecialist@brainup.spb.ru", "password": "password",
                        "returnSecureToken": "true"}
result_post_specialist = requests.post(authorization_url, data_specialist_user)
id_token = json.loads(result_post_specialist.text)['idToken']

data_default_user = {"email": "default@default.ru", "password": "password",
                     "returnSecureToken": "true"}
result_post_default = requests.post(authorization_url, data_default_user).json()
id_token_default = result_post_default['idToken']


class SpeechExercisesAPI(BasePage):
    locators = SpeechExercisesPageLocators()

    @staticmethod
    def get_random_id_from_list_sub_group(card_id, seria_id):
        print('Card_id is:', card_id)
        print('Seria_id is:', seria_id)
        list_cards_id = requests.get(f'https://brainup.site/api/subgroups?seriesId={seria_id}',
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(id_token)})
        with allure.step(
                f'Send GET request with params: '
                f'https://brainup.site/api/subgroups?seriesId={seria_id} '
                f'headers="Content-Type": "application/json","Authorization": "Bearer": "{{id_token}}"'):
            pass
        with allure.step(f'Getting list of cards id: {list_cards_id.json()}'):
            pass
        result_get = json.loads(list_cards_id.text)
        id_number = random.choice(result_get['data'][card_id]['exercises'])
        with allure.step(f'Select random id from list: {id_number}'):
            pass
        print('Nuber exercise on backend is: ', id_number)
        return id_number

    # General methods
    @staticmethod
    def get_list_of_words_from_card(card_id):
        result_get = requests.get(f'https://brainup.site/api/tasks/{str(card_id)}',
                                  headers={'Content-Type': 'application/json',
                                           'Authorization': 'Bearer {}'.format(id_token)})
        # word = json.loads(result_get.text)['data']["answerOptions"][0]['word']
        amount_words = len(json.loads(result_get.text)['data']["answerOptions"])
        words = [json.loads(result_get.text)['data']["answerOptions"][i]['word'] for i in range(amount_words)]
        with allure.step(f'Getting a list of exercise words from the backend: {words}.'):
            print('\nBACKEND LIST: ', words)
            ref_list = [i.lower() for i in words]
            print('\nBACKEND LIST in lowercase: ', ref_list)
        return ref_list

    @staticmethod
    def get_list_of_words_from_card_group_words(card_id):
        result_get = requests.get(f'https://brainup.site/api/tasks/{str(card_id)}',
                                  headers={'Content-Type': 'application/json',
                                           'Authorization': 'Bearer {}'.format(id_token)})
        dict_list = json.loads(result_get.text)['data']["answerOptions"]
        words = []
        for k, v in dict_list.items():
            for i in range(len(dict_list[k])):
                words.append(dict_list[k][i]['word'])
        with allure.step(f'Getting a list of exercise words from the backend: {words}.'):
            print('\nBACKEND LIST: ', words)
            ref_list = [i.lower() for i in words]
            print('\nBACKEND LIST in lowercase: ', ref_list)
        return ref_list

    def click_start_and_get_list_words_en(self):
        with allure.step('Click button "Start".'):
            self.element_is_present_and_clickable(self.locators.BUTTON_START_EN).click()
        list_words = self.elements_are_visible(self.locators.LIST_WORDS_IN_CARD)
        words = [i.text.lower() for i in list_words]
        with allure.step(f'Getting a list of exercise words from the front: {words}'):
            print('\nUI LIST: ', words)
        return words

    def click_start_and_get_list_words_ru(self):
        with allure.step('Click button "Start".'):
            self.element_is_present_and_clickable(self.locators.BUTTON_START_RU).click()
        list_words = self.elements_are_visible(self.locators.LIST_WORDS_IN_CARD)
        words = [i.text.lower() for i in list_words]
        with allure.step(f'Getting a list of exercise words from the front: {words}'):
            print('\nUI LIST: ', words)
        with allure.step('Click button "Повторить".'):
            self.element_is_present_and_clickable(self.locators.BUTTON_REPEAT_RU).click()
        with allure.step('Click button "Решать".'):
            self.element_is_present_and_clickable(self.locators.BUTTON_SOLVE_RU).click()
        return words

    def click_start_and_get_list_words_for_group_words_ru(self):
        with allure.step('Click button "Start".'):
            self.element_is_present_and_clickable(self.locators.BUTTON_START_RU).click()
        list_words = self.elements_are_visible(self.locators.LIST_WORDS_FOR_GROUP_WORDS)
        words = [i.text.lower() for i in list_words]
        with allure.step(f'Getting a list of exercise words from the front: {words}'):
            print('\nUI LIST: ', words)
        return words

    @staticmethod
    def get_random_id_from_list_sub_group_default(card_id, seria_id):
        print('Card_id is:', card_id)
        print('Seria_id is:', seria_id)
        list_cards_id = requests.get(f'https://brainup.site/api/subgroups?seriesId={seria_id}',
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(id_token_default)})
        with allure.step(
                f'Send GET request with params: '
                f'https://brainup.site/api/subgroups?seriesId={seria_id}'
                f'headers="Content-Type": "application/json","Authorization": "Bearer": "{{id_token_default}}"'):
            pass
        with allure.step(f'Getting list of cards id: {list_cards_id.json()}'):
            pass
        result_get = json.loads(list_cards_id.text)
        # print('IDS', result_get['data'][card_id]['exercises'])
        payloads = {}
        payloads.setdefault('ids', result_get['data'][card_id]['exercises'])
        print('payloads', payloads)
        id_number = random.choice(result_get['data'][card_id]['exercises'])
        with allure.step(f'Select random id from list: {id_number}'):
            pass
        print('Nuber exercise on backend is: ', id_number)
        return payloads

    # General methods
    @staticmethod
    def get_list_of_words_from_card_default(card_id):
        result_get = requests.post(f'https://brainup.site/api/tasks/{str(card_id)}',
                                   headers={'Content-Type': 'application/json',
                                            'Authorization': 'Bearer {}'.format(id_token_default)})
        amount_words = len(json.loads(result_get.text)['data']["answerOptions"])
        words = [json.loads(result_get.text)['data']["answerOptions"][i]['word'] for i in range(amount_words)]
        with allure.step(f'Getting a list of exercise words from the backend: {words}.'):
            print('\nBACKEND LIST: ', words)
            ref_list = [i.lower() for i in words]
            print('\nBACKEND LIST in lowercase: ', ref_list)
        return ref_list

    @staticmethod
    def get_random_id_from_payloads(payloads):
        exercises = requests.post(f'https://brainup.site/api/exercises/byIds',
                                  headers={'Content-Type': 'application/json',
                                           'Authorization': 'Bearer {}'.format(id_token_default)}, json=payloads)
        random_id = random.choice(exercises.json()['data'])
        print('random_id', random_id)
        return random_id
