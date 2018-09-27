from unittest.case import TestCase
from csv import DictReader
from tsuan import tiau


class tshi(TestCase):
    def test_naphing(self):
        with open('LTS_utf8,.csv') as tong:
            for tsua in DictReader(tong):
                self.assertEqual(
                    tiau(tsua['原檔'].rstrip()),
                    tsua['修正'].rstrip()
                )
