import unittest

class ExploratoryTests(unittest.TestCase):
    def test_find_works_like_i_think(self):
        blob = "dfadfadfdafafdfayomamaahofdafafa"
        self.assertTrue(blob.find("yomamaaho"))


if __name__ == '__main__':
    unittest.main()
