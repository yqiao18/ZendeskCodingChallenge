import unittest
from API import Zendesk


class MyTestCase(unittest.TestCase):
    def test_something(self):
        x = Zendesk()
        x.requestData()
        self.assertEqual(len(x.data['tickets']), 100)  # add assertion here


if __name__ == '__main__':
    unittest.main()
