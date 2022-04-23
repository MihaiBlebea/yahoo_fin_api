from __future__ import annotations
from typing import List
from dataclasses import dataclass
import json
import yahoo_api.utils as U
from yahoo_api.models.base_model import Model


@dataclass
class CashFlow(Model):

	end_date: int

	net_income: int

	depreciation: int

	change_to_net_income: int

	change_to_account_receivables: int

	change_to_liabilities: int

	change_to_inventory: int

	change_to_operating_activities: int

	total_cash_from_operating_activities: int

	capital_expenditures: int

	investments: int

	other_cashflows_from_investing_activities: int

	total_cashflows_from_investing_activities: int

	dividends_paid: int

	net_borrowings: int

	other_cashflows_from_financing_activities: int

	total_cash_from_financing_activities: int

	change_in_cash: int

	repurchase_of_stock: int

	issuance_of_stock: int

	def free_cash_flow(self, formatted: bool = False)-> int:
		val = self.total_cash_from_operating_activities - self.capital_expenditures
		return U.format_amount(val) if formatted else val

@dataclass
class CashFlows:

	symbol: str

	cashflows: List[CashFlow]

	def from_input_file(path: str)-> CashFlows | None:
		with open(path, "r") as file:
			data = json.loads(file.read())
			return CashFlows.from_dict(data)

	def from_dict(data: dict)-> CashFlows | None:
		symbol = U.extract_key(data, "quoteType", "symbol")
		data = U.extract_key(data, "cashflowStatementHistory", "cashflowStatements")
		if data is None or symbol is None:
			return None

		return CashFlows(
			symbol,
			[
				CashFlow(
					U.extract_key(d, "endDate", "raw"), 
					U.extract_key(d, "netIncome", "raw"),
					U.extract_key(d, "depreciation", "raw"),
					U.extract_key(d, "changeToNetincome", "raw"),
					U.extract_key(d, "changeToAccountReceivables", "raw"),
					U.extract_key(d, "changeToLiabilities", "raw"),
					U.extract_key(d, "changeToInventory", "raw"),
					U.extract_key(d, "changeToOperatingActivities", "raw"),
					U.extract_key(d, "totalCashFromOperatingActivities", "raw"),
					U.extract_key(d, "capitalExpenditures", "raw"),
					U.extract_key(d, "investments", "raw"),
					U.extract_key(d, "otherCashflowsFromInvestingActivities", "raw"),
					U.extract_key(d, "totalCashflowsFromInvestingActivities", "raw"),
					U.extract_key(d, "dividendsPaid", "raw"),
					U.extract_key(d, "netBorrowings", "raw"),
					U.extract_key(d, "otherCashflowsFromFinancingActivities", "raw"),
					U.extract_key(d, "totalCashFromFinancingActivities", "raw"),
					U.extract_key(d, "changeInCash", "raw"),
					U.extract_key(d, "repurchaseOfStock", "raw"),
					U.extract_key(d, "issuanceOfStock", "raw"),
				) for d in data
			]
		)
