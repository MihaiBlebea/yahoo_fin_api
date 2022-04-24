from __future__ import annotations
import unittest
import json
from yahoo_fin_api import FinancialData

class TestFinancialData(unittest.TestCase):

	def __load_financial_data(self)-> FinancialData | None:
		return FinancialData.from_input_file("./tests/AAPL.json")

	def test_can_load_financial_data_from_file(self):
		fd = self.__load_financial_data()
		if fd is None:
			self.fail("could not load financial data")

		self.assertEqual("AAPL", fd.symbol)

	def test_can_load_financial_data_from_dict(self):
		with open("./tests/AAPL.json") as file:
			d = json.loads(file.read())
			fd = FinancialData.from_dict(d)
			if fd is None:
				self.fail("could not load financial data")

			self.assertEqual("AAPL", fd.symbol)

	def test_correct_data(self):
		fd = self.__load_financial_data()
		if fd is None:
			self.fail("could not load financial data")
			
		self.assertEqual(167.11, fd.current_price)
		self.assertEqual(210, fd.target_high_price)
		self.assertEqual(128.01, fd.target_low_price)
		self.assertEqual(174.93, fd.target_mean_price)
		self.assertEqual(174.5, fd.target_median_price)


if __name__ == "__main__":
    unittest.main()