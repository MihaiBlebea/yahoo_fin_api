from __future__ import annotations
from typing import List
from dataclasses import dataclass
import json
import yahoo_api.utils as U
from yahoo_api.base_model import Model


@dataclass
class BalanceSheet(Model):

	end_date: int

	cash: int

	short_term_investments: int

	net_receivables: int

	inventory: int

	other_current_assets: int

	total_current_assets: int

	long_term_investments: int

	property_plant_equipment: int

	other_assets: int

	total_assets: int

	accounts_payable: int

	short_long_term_debt: int

	other_current_liab: int

	long_term_debt: int

	other_liab: int

	total_current_liabilities: int

	total_liab: int

	common_stock: int

	retained_earnings: int

	treasury_stock: int

	other_stockholder_equity: int

	total_stockholder_equity: int

	net_tangible_assets: int


@dataclass
class BalanceSheets:

	symbol: str

	balance_sheets: List[BalanceSheet]

	def from_input_file(symbol: str, path: str)-> BalanceSheets:
		with open(path, "r") as file:
			d = json.loads(file.read())
			d = d["balanceSheetHistory"]["balanceSheetStatements"]

			return BalanceSheets.from_dict(symbol, d)

	def from_dict(symbol: str, data: List[dict])-> BalanceSheets:
		return BalanceSheets(
			symbol,
			[
				BalanceSheet(
					U.extract_key(d, "endDate", "raw"), 
					U.extract_key(d, "cash", "raw"),
					U.extract_key(d, "shortTermInvestments", "raw"),
					U.extract_key(d, "netReceivables", "raw"),
					U.extract_key(d, "inventory", "raw"),
					U.extract_key(d, "otherCurrentAssets", "raw"),
					U.extract_key(d, "totalCurrentAssets", "raw"),
					U.extract_key(d, "longTermInvestments", "raw"),
					U.extract_key(d, "propertyPlantEquipment", "raw"),
					U.extract_key(d, "otherAssets", "raw"),
					U.extract_key(d, "totalAssets", "raw"),
					U.extract_key(d, "accountsPayable", "raw"),
					U.extract_key(d, "shortLongTermDebt", "raw"),
					U.extract_key(d, "otherCurrentLiab", "raw"),
					U.extract_key(d, "longTermDebt", "raw"),
					U.extract_key(d, "otherLiab", "raw"),
					U.extract_key(d, "totalCurrentLiabilities", "raw"),
					U.extract_key(d, "totalLiab", "raw"),
					U.extract_key(d, "commonStock", "raw"),
					U.extract_key(d, "retainedEarnings", "raw"),
					U.extract_key(d, "treasuryStock", "raw"),
					U.extract_key(d, "otherStockholderEquity", "raw"),
					U.extract_key(d, "totalStockholderEquity", "raw"),
					U.extract_key(d, "netTangibleAssets", "raw"),
				) for d in data
			]
		)
