import unittest
from API_ya_test import folder_creation
from yandex_auth_info import yandex_token

class TestApi(unittest.TestCase):
    def setUp(self):
        print('setup')

    def tearDown(self):
        print('teardown')

    def test_folder_creation(self):
        result = folder_creation(yandex_token)
        if result == 201:
            print('folder created')


if __name__=='__main__':
    unittest.main()