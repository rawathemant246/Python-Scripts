import unittest
from arangeit import Arange

class TestArange(unittest.TestCase):
    def test_get_folder(self):
        config = {"Pictures": [".jpg", ".png"], "Videos": [".mp4"]}
        self.assertEqual(Arange.get_folder(".jpg", config), "Pictures")
        self.assertEqual(Arange.get_folder(".txt", config), "other")


if __name__ == "__main__":
    unittest.main()