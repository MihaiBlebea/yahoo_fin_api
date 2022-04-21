from __future__ import annotations
from typing import List
from dataclasses import dataclass
import json
import yahoo_api.utils as U
from yahoo_api.base_model import Model


@dataclass
class IncomeStatement(Model):

	end_date: int

	total_revenue: int

	cost_of_revenue: int

	gross_profit: int

	research_development: int

	selling_general_administrative: int

	other_operating_expenses: int

	total_operating_expenses: int

	operating_income: int

	total_other_income_expense_net: int

	ebit: int

	interest_expense: int

	income_before_tax: int

	income_tax_expense: int

	net_income_from_continuing_ops: int

	discontinued_operations: int

	effect_of_accounting_charges: int

	net_income: int

	net_income_applicable_to_common_shares: int


@dataclass
class IncomeStatements:

	symbol: str

	income_statements: List[IncomeStatement]

	def from_input_file(symbol: str, path: str)-> IncomeStatements:
		with open(path, "r") as file:
			d = json.loads(file.read())
			d = d["incomeStatementHistory"]["incomeStatementHistory"]

			return IncomeStatements.from_dict(symbol, d)

	def from_dict(symbol: str, data: List[dict])-> IncomeStatements:
		return IncomeStatements(
			symbol,
			[
				IncomeStatement(
					U.extract_key(d, "endDate", "raw"), 
					U.extract_key(d, "totalRevenue", "raw"),
					U.extract_key(d, "costOfRevenue", "raw"),
					U.extract_key(d, "grossProfit", "raw"),
					U.extract_key(d, "researchDevelopment", "raw"),
					U.extract_key(d, "sellingGeneralAdministrative", "raw"),
					U.extract_key(d, "otherOperatingExpenses", "raw"),
					U.extract_key(d, "totalOperatingExpenses", "raw"),
					U.extract_key(d, "operatingIncome", "raw"),
					U.extract_key(d, "totalOtherIncomeExpenseNet", "raw"),
					U.extract_key(d, "ebit", "raw"),
					U.extract_key(d, "interestExpense", "raw"),
					U.extract_key(d, "incomeBeforeTax", "raw"),
					U.extract_key(d, "incomeTaxExpense", "raw"),
					U.extract_key(d, "netIncomeFromContinuingOps", "raw"),
					U.extract_key(d, "discontinuedOperations", "raw"),
					U.extract_key(d, "effectOfAccountingCharges", "raw"),
					U.extract_key(d, "netIncome", "raw"),
					U.extract_key(d, "netIncomeApplicableToCommonShares", "raw")
				) for d in data
			]
		)
