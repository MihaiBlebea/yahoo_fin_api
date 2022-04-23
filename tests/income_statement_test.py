import unittest
import json
from yahoo_api import IncomeStatements

class TestIncomeStatement(unittest.TestCase):

	def __load_income_statements(self)-> IncomeStatements:
		return IncomeStatements.from_input_file("./tests/AAPL.json")

	def test_can_load_statements_from_file(self):
		statements = self.__load_income_statements()

		self.assertEqual("AAPL", statements.symbol)
		self.assertEqual(1632528000, statements.income_statements[0].end_date)
		self.assertEqual("2021-09-25", statements.income_statements[0].fmt_end_date())

	def test_can_load_statements_from_dict(self):
		with open("./tests/AAPL.json") as file:
			d = json.loads(file.read())
			statements = IncomeStatements.from_dict(d)

			self.assertEqual(1632528000, statements.income_statements[0].end_date)
			self.assertEqual("2021-09-25", statements.income_statements[0].fmt_end_date())

	def test_correct_data(self):
		stms = self.__load_income_statements()

		stm = stms.income_statements[0]
		self.assertEqual(365817000000, stm.total_revenue)
		self.assertEqual(212981000000, stm.cost_of_revenue)
		self.assertEqual(152836000000, stm.gross_profit)
		self.assertEqual(21914000000, stm.research_development)
		self.assertEqual(21973000000, stm.selling_general_administrative)
		self.assertEqual(256868000000, stm.total_operating_expenses)
		self.assertEqual(None, stm.other_operating_expenses)
		self.assertEqual(108949000000, stm.operating_income)



if __name__ == "__main__":
    unittest.main()