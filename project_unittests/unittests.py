import requests
import unittest

"""
Документацию по API вы можете найти здесь:
http://193.178.169.224:5000/api/v1/docs/
"""

server = "http://193.178.169.224:5000/"
link = "api/v1/parse/statistic?domain="
headers = {"ADMIN": "not_real_secret_key"}


class TestParsing(unittest.TestCase):
    def test_server_available(self):
        try:
            requests.get(server)
        except ConnectionError:
            self.assertFalse(True, "Server not available")

    def test_amazon_true(self):
        _request = requests.get(server + link + "amazon.com", headers=headers)
        self.assertTrue(_request.json()["status"])

    def test_yandex_true(self):
        _request = requests.get(server + link + "yandex.ru", headers=headers)
        self.assertTrue(_request.json()["status"])

    def test_google_true(self):
        _request = requests.get(server + link + "google.com", headers=headers)
        self.assertTrue(_request.json()["status"])

    def test_roblox_true(self):
        _request = requests.get(server + link + "roblox.com", headers=headers)
        self.assertTrue(_request.json()["status"])
