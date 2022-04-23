import unittest
import json
from yahoo_fin_api import CashFlows

class TestCashFlow(unittest.TestCase):

	def __load_cashflows(self)-> CashFlows:
		return CashFlows.from_input_file("./tests/AAPL.json")

	def test_can_load_cashflows_from_file(self):
		cf = self.__load_cashflows()

		self.assertEqual("AAPL", cf.symbol)
		self.assertEqual(1632528000, cf.cashflows[0].end_date)
		self.assertEqual("2021-09-25", cf.cashflows[0].fmt_end_date())

	def test_can_load_cashflows_from_dict(self):
		with open("./tests/AAPL.json") as file:
			d = json.loads(file.read())
			cf = CashFlows.from_dict(d)

			self.assertEqual("AAPL", cf.symbol)
			self.assertEqual(1632528000, cf.cashflows[0].end_date)
			self.assertEqual("2021-09-25", cf.cashflows[0].fmt_end_date())

	def test_correct_data(self):
		cf = self.__load_cashflows()

		cf = cf.cashflows[0]
		self.assertEqual(94680000000, cf.net_income)
		self.assertEqual(-2819000000, cf.investments)
		self.assertEqual(-14467000000, cf.dividends_paid)
		self.assertEqual(12665000000, cf.net_borrowings)


if __name__ == "__main__":
    unittest.main()