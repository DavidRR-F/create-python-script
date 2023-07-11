import unittest


class TestExample(unittest.TestCase):
    def setUp(self):
        print("Setting up")

    def tearDown(self):
        print("Tearing down")

    def test_project(self):
        print("Running test")


if __name__ == "__main__":
    unittest.main()
