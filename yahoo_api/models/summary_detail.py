from __future__ import annotations
from dataclasses import dataclass
import json
import yahoo_api.utils as U
from yahoo_api.models.base_model import Model


@dataclass
class SummaryDetail(Model):

	symbol: str

	title: str

	price_hint: int

	previous_close: float

	open: float

	day_low: float

	day_high: float

	regular_market_previous_close: float

	regular_market_open: float

	regular_market_day_low: float

	regular_market_day_high: float

	dividend_rate: float

	dividend_yield: float

	ex_dividend_date: int

	payout_ratio: float

	five_year_avg_dividend_yield: float

	beta: float

	trailing_pe: float

	forward_pe: float

	volume: int

	regular_market_volume: int

	average_volume: int

	average_volume_10_days: int

	average_daily_volume_10_day: int

	market_cap: int

	fifty_two_week_low: float

	fifty_two_week_high: float

	def from_input_file(path: str)-> SummaryDetail | None:
		with open(path, "r") as file:
			data = json.loads(file.read())
			return SummaryDetail.from_dict(data)

	def from_dict(data: dict)-> SummaryDetail | None:
		symbol = U.extract_key(data, "quoteType", "symbol")
		title = U.extract_key(data, "quoteType", "longName")
		d = U.extract_key(data, "summaryDetail")
		if d is None or symbol is None:
			return None

		return SummaryDetail(
			symbol,
			title,
			U.extract_key(d, "priceHint", "raw"),
			U.extract_key(d, "previousClose", "raw"),
			U.extract_key(d, "open", "raw"),
			U.extract_key(d, "dayLow", "raw"),
			U.extract_key(d, "dayHigh", "raw"),
			U.extract_key(d, "regularMarketPreviousClose", "raw"),
			U.extract_key(d, "regularMarketOpen", "raw"),
			U.extract_key(d, "regularMarketDayLow", "raw"),
			U.extract_key(d, "regularMarketDayHigh", "raw"),
			U.extract_key(d, "dividendRate", "raw"),
			U.extract_key(d, "dividendYield", "raw"),
			U.extract_key(d, "exDividendDate", "raw"),
			U.extract_key(d, "payoutRatio", "raw"),
			U.extract_key(d, "fiveYearAvgDividendYield", "raw"),
			U.extract_key(d, "beta", "raw"),
			U.extract_key(d, "trailingPE", "raw"),
			U.extract_key(d, "forwardPE", "raw"),
			U.extract_key(d, "volume", "raw"),
			U.extract_key(d, "regularMarketVolume", "raw"),
			U.extract_key(d, "averageVolume", "raw"),
			U.extract_key(d, "averageVolume10days", "raw"),
			U.extract_key(d, "averageDailyVolume10Day", "raw"),
			U.extract_key(d, "marketCap", "raw"),
			U.extract_key(d, "fiftyTwoWeekLow", "raw"),
			U.extract_key(d, "fiftyTwoWeekHigh", "raw"),
		)