import os
import unittest

class Detail:
    def __init__(self):
        self.detail_file_name = "detail.csv"
        default_contents = "Rest, CCCV_DChg"
        with open(self.detail_file_name, "w") as f:
            f.write(default_contents)

    def empty_dataset(self):
        os.remove(self.detail_file_name)


class TestDetail(unittest.TestCase):
    def setUp(self):
        self.detail = Detail()

    def tearDown(self):
        self.detail.empty_dataset()

    def test_detail_writes_file(self):
        with open(self.detail.detail_file_name) as f:
            contents = f.read()
        self.assertEqual(contents, "Rest, CCCV_DChg")