from __future__ import annotations
from typing import List
from dataclasses import dataclass
import json
import yahoo_api.utils as U


@dataclass
class CashFlow:

	end_date: str

	net_income: int

	investments: int

	dividends_paid: int

	net_borrowings: int


@dataclass
class CashFlows:

	symbol: str

	cashflows: List[CashFlow]

	def from_input_file(symbol: str, path: str)-> CashFlows:
		with open(path, "r") as file:
			d = json.loads(file.read())
			d = d["cashflowStatementHistory"]["cashflowStatements"]

			return CashFlows.from_dict(symbol, d)

	def from_dict(symbol: str, data: List[dict])-> CashFlows:
		return CashFlows(
			symbol,
			[
				CashFlow(
					U.extract_key(d, "endDate", "fmt"), 
					U.extract_key(d, "netIncome", "raw"),
					U.extract_key(d, "investments", "raw"),
					U.extract_key(d, "dividendsPaid", "raw"),
					U.extract_key(d, "netBorrowings", "raw"),
				) for d in data
			]
		)
