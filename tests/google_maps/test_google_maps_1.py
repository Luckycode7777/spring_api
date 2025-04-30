import json
from pprint import pprint

from services.service_google_map.api_google_maps import GoogleMapsAPI
import requests
from utils.cheking import Checking

"""Создание, изменение, удаление новой локации"""
class TestCreatePlace:
    def test_create_new_place(self):
        print('\nметод POST')
        result_post = GoogleMapsAPI.create_new_place()
        check_post = result_post.json()
        print(f'check_post - {check_post}')
        place_id = check_post.get('place_id', 'Такого ключа нет')
        print(f'PLACE ID *****>> {place_id}')
        Checking.checking_status_code(result_post, 200)
        Checking.check_json_keys(result_post, Checking.get_keys(result_post))
        Checking.check_json_values(result_post, 'status', 'OK')

        # print('\nметод GET')
        # result_get = GoogleMapsAPI.get_new_place(place_id)
        # Checking.checking_status_code(result_get, 200)
        # Checking.check_json_values(result_get, Checking.get_keys(result_get))
        #
        # print('\nметод DELETE')
        # result_delete = GoogleMapsAPI.delete_new_place(place_id)
        # Checking.checking_status_code(result_delete, 200)
        # Checking.check_json_values(result_delete, Checking.get_keys(result_delete))
        #
        # # print('\nметод GET DELETE')
        # # result_get = GoogleMapsAPI.get_new_place(place_id)
        # # Checking.checking_status_code(result_get, 404)
