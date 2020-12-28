from unittest import TestCase
from unittest.mock import patch
import pytest
from doge import Doge

some_breeds={
    'message': {'gamer': [], 'Karl': [], "Bart": ["english", "shetland"], "spaniel": [
        "lenny", "gamer", "Karl", "Bart", "japanese", "sussex", "welsh"]}, 'status': 'success'
}


def img(num):
    return {
        'message': ['https://images.dog.ceo/breeds/hound-afghan/n02088094_.jpg'] * num,
        'status': 'success'
    }

class TestImages(TestCase):
    @patch('doge.Doge.random_images', side_effect=img)
    def test_images(self, random_images):
        self.assertEqual(len(random_images(42)["message"]), 42)

    @patch('doge.Doge')
    def test_breeds(self, lazy_doge):
        doge = lazy_doge()
        doge.all_breeds.return_value = some_breeds
        assert doge.all_breeds() == some_breeds


    def test_request_respons_with_patcher(self):
        get_patcher = patch('doge.Doge.get_random')
        get = get_patcher.start()
        get.return_value.status_code = 200
        response = Doge.get_random()
        get_patcher.stop()
        self.assertEqual(response.status_code, 200)
