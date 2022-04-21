from __future__ import annotations
from dataclasses import dataclass
import json
import yahoo_api.utils as U
from yahoo_api.base_model import Model


@dataclass
class FinancialData(Model):

	symbol: str

	current_price: float

	target_high_price: float

	target_low_price: float

	target_mean_price: float

	target_median_price: float

	def from_input_file(symbol: str, path: str)-> FinancialData:
		symbol = symbol.upper()

		with open(path, "r") as file:
			d = json.loads(file.read())
			d = d["financialData"]

			return FinancialData.from_dict(symbol, d)

	def from_dict(symbol: str, d: dict)-> FinancialData:
		return FinancialData(
			symbol,
			U.extract_key(d, "currentPrice", "raw"),
			U.extract_key(d, "targetHighPrice", "raw"),
			U.extract_key(d, "targetLowPrice", "raw"),
			U.extract_key(d, "targetMeanPrice", "raw"),
			U.extract_key(d, "targetMedianPrice", "raw"),
		)