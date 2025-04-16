from pprint import pprint

from services.service_google_map.api_google_maps import GoogleMapsAPI
import requests

"""Создание, изменение, удаление новой локации"""
class TestCreatePlace:

    def test_create_new_place(self):
        print('\nметод POST')
        result_post = GoogleMapsAPI.create_new_place()
        check_post = result_post.json()
        print(check_post)
        place_id = check_post.get('place_id')
        print(f'PLACE ID **>> {place_id}')

        print('\nметод GET')
        result_get = GoogleMapsAPI.get_new_place(place_id)
        print(result_get.status_code)
