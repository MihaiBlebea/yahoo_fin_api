import unittest
import json
from yahoo_fin_api import SummaryDetail

class TestSummaryDetail(unittest.TestCase):

	def __load_summary_detail(self)-> SummaryDetail:
		return SummaryDetail.from_input_file("./tests/AAPL.json")

	def test_can_load_summary_detail_from_file(self):
		sd = self.__load_summary_detail()

		self.assertEqual("AAPL", sd.symbol)

	def test_can_load_summary_detail_from_dict(self):
		with open("./tests/AAPL.json") as file:
			d = json.loads(file.read())
			sd = SummaryDetail.from_dict(d)

			self.assertEqual("AAPL", sd.symbol)

	def test_correct_data(self):
		sd = self.__load_summary_detail()

		self.assertEqual(2741673394176, sd.market_cap)


if __name__ == "__main__":
    unittest.main()