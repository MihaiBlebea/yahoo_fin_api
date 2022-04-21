from typing import List
from yahoo_api.client import Client
from yahoo_api.cashflow import CashFlows
from yahoo_api.income_statement import IncomeStatements
from yahoo_api.balance_sheet import BalanceSheets

class YahooFinApi:

	def __init__(self, client: Client) -> None:
		self.client = client

	def get_balance_sheets(self, symbols: list[str])-> List[BalanceSheets]:
		res = self.client.get_symbols(symbols)

		return [
			BalanceSheets.from_dict(
				symbols[i], 
				r["balanceSheetHistory"]["balanceSheetStatements"]
			) for i, r in enumerate(res)
		]

	def get_cashflow_statements(self, symbols: list[str])-> List[CashFlows]:
		res = self.client.get_symbols(symbols)

		return [
			CashFlows.from_dict(
				symbols[i], 
				r["cashflowStatementHistory"]["cashflowStatements"]
			) for i, r in enumerate(res)
		]

	def get_income_statements(self, symbols: List[str])-> List[IncomeStatements]:
		res = self.client.get_symbols(symbols)

		return [
			IncomeStatements.from_dict(
				symbols[i], 
				r["incomeStatementHistory"]["incomeStatementHistory"]
			) for i, r in enumerate(res)
		]
