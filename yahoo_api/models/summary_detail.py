from __future__ import annotations
from dataclasses import dataclass
import json
import yahoo_api.utils as U
from yahoo_api.models.base_model import Model


@dataclass
class SummaryDetail(Model):

	symbol: str

	market_cap: int

	def from_input_file(path: str)-> SummaryDetail | None:
		with open(path, "r") as file:
			data = json.loads(file.read())
			return SummaryDetail.from_dict(data)

	def from_dict(data: dict)-> SummaryDetail | None:
		symbol = U.extract_key(data, "quoteType", "symbol")
		d = U.extract_key(data, "summaryDetail")
		if d is None or symbol is None:
			return None

		return SummaryDetail(
			symbol,
			U.extract_key(d, "marketCap", "raw"),
		)