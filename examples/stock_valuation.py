from __future__ import annotations
from yahoo_fin_api import YahooFinApi, Client, FileCache, Universe

from pprint import pprint

BILLION = 1000000000

def main():
	yf = YahooFinApi(Client(FileCache("./data")))
	symbols = Universe.get_ftse_100_universe()
	tickers = yf.get_all(symbols)
	
	res = []
	for t in tickers:
		fin_data = t.financial_data
		summary = t.summary_detail

		if fin_data is None or summary is None:
			continue

		if fin_data.free_cash_flow is None or summary.market_cap is None:
			continue

		if fin_data.free_cash_flow < 0:
			continue

		if summary.market_cap < 5 * BILLION:
			continue

		cap_rate = fin_data.free_cash_flow / summary.market_cap * 100

		if cap_rate > 10:
			res.append({
				"symbol": t.symbol,
				"title": t.title,
				"cap_rate": cap_rate,
				"market_cap": summary.market_cap,
				"fcf": fin_data.free_cash_flow,
				"current_price": fin_data.current_price,
				"profit_margin": fin_data.profit_margins
			})

	res = sorted(res, key=lambda r: r["cap_rate"], reverse=True)
	pprint(res)


if __name__ == "__main__":
	main()