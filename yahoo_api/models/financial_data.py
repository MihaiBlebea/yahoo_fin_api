from __future__ import annotations
from dataclasses import dataclass
import json
import yahoo_api.utils as U
from yahoo_api.models.base_model import Model


@dataclass
class FinancialData(Model):

	symbol: str

	title: str

	current_price: float

	target_high_price: float

	target_low_price: float

	target_mean_price: float

	target_median_price: float

	free_cash_flow: float

	def from_input_file(path: str)-> FinancialData | None:
		with open(path, "r") as file:
			data = json.loads(file.read())
			return FinancialData.from_dict(data)

	def from_dict(data: dict)-> FinancialData | None:
		symbol = U.extract_key(data, "quoteType", "symbol")
		title = U.extract_key(data, "quoteType", "longName")
		d = U.extract_key(data, "financialData")
		if d is None or symbol is None:
			return None

		return FinancialData(
			symbol,
			title,
			U.extract_key(d, "currentPrice", "raw"),
			U.extract_key(d, "targetHighPrice", "raw"),
			U.extract_key(d, "targetLowPrice", "raw"),
			U.extract_key(d, "targetMeanPrice", "raw"),
			U.extract_key(d, "targetMedianPrice", "raw"),
			U.extract_key(d, "freeCashflow", "raw"),
		)