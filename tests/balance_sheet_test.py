import unittest
import json
from yahoo_api.balance_sheet import BalanceSheets

class TestBalanceSheet(unittest.TestCase):

	def __load_balance_sheets(self)-> BalanceSheets:
		return BalanceSheets.from_input_file("AAPL", "./tests/AAPL.json")

	def test_can_load_cashflows_from_file(self):
		bs = self.__load_balance_sheets()

		self.assertEqual("AAPL", bs.symbol)
		self.assertEqual(1632528000, bs.balance_sheets[0].end_date)
		self.assertEqual("2021-09-25", bs.balance_sheets[0].fmt_end_date())

	def test_can_load_balance_sheets_from_dict(self):
		with open("./tests/AAPL.json") as file:
			d = json.loads(file.read())
			d = d["balanceSheetHistory"]["balanceSheetStatements"]
			bs = BalanceSheets.from_dict("AAPL", d)

			self.assertEqual("AAPL", bs.symbol)
			self.assertEqual(1632528000, bs.balance_sheets[0].end_date)
			self.assertEqual("2021-09-25", bs.balance_sheets[0].fmt_end_date())

	def test_correct_data(self):
		bs = self.__load_balance_sheets()

		bs = bs.balance_sheets[0]
		self.assertEqual(34940000000, bs.cash)
		self.assertEqual(27699000000, bs.short_term_investments)
		self.assertEqual(51506000000, bs.net_receivables)
		self.assertEqual(6580000000, bs.inventory)


if __name__ == "__main__":
    unittest.main()