import sys
import unittest
import pandas as pd
from src.preprocessing import format_ocean_proximity

class FormattingTestCase(unittest.TestCase):

    def setUp(self):
        self.ref_df = pd.read_csv("housing.csv")

    def test_format_ocean_proximity(self):
        ref_output = format_ocean_proximity(pd.DataFrame(self.ref_df))
        print(ref_output['ocean_proximity'])
        self.assertEqual(ref_output['ocean_proximity'][0], "within_of_hour_ocean")
       
if __name__ == '__main__':
    unittest.main()

