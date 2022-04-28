# Yahoo Financials API

Lightweight SDK for interacting with the Yahoo Financials API. This is more geared on towards the three main financial records: 
- balance sheet
- income statement
- cash flow

## How to install?

```bash
pip3 install yahoo-fin-api
```

## Examples

### 1. Get the data from the Yahoo Financials API

```python
from yahoo_api import Client

def main():
	client = Client(
		cache_response= True, # Should cache the response after fetching from API
		input_csv_file="./examples/freetrade_universe.csv", # Load the universe from this file
		download_folder_path="./data") # Cache the data from the API in this folder

	client.get_symbols()

if __name__ == "__main__":
	main()
```

### 2. Load the balance sheet models

```python
from yahoo_api import YahooFinApi, Client

from pprint import pprint

def main():
	yf = YahooFinApi(
		Client(
			cache_response= True, 
			input_csv_file="./examples/freetrade_universe.csv", 
			download_folder_path="./data"
		)
	)

	bs = yf.get_balance_sheets(["AAPL", "TSLA"])
	pprint(bs)

if __name__ == "__main__":
	main()
```

### 3. Load the cash flow models

```python
from yahoo_api import YahooFinApi, Client

from pprint import pprint

def main():
	yf = YahooFinApi(
		Client(
			cache_response= True, 
			input_csv_file="./examples/freetrade_universe.csv", 
			download_folder_path="./data"
		)
	)

	cf = yf.get_cashflow_statements(["AAPL", "TSLA"])
	pprint(cf)

if __name__ == "__main__":
	main()
```

### 4. Load the income statement model

```python
from yahoo_api import YahooFinApi, Client

from pprint import pprint

def main():
	yf = YahooFinApi(
		Client(
			cache_response= True, 
			input_csv_file="./examples/freetrade_universe.csv", 
			download_folder_path="./data"
		)
	)

	i_stmts = yf.get_income_statements(["AAPL", "TSLA"])
	pprint(i_stmts)

if __name__ == "__main__":
	main()
```

### 5. Load financial data model

```python
from yahoo_api import YahooFinApi, Client

from pprint import pprint

def main():
	yf = YahooFinApi(
		Client(
			cache_response= True, 
			input_csv_file="./examples/freetrade_universe.csv", 
			download_folder_path="./data"
		)
	)

	cf = yf.get_financial_data(["AAPL", "TSLA"])
	pprint(cf)

if __name__ == "__main__":
	main()
```

### 6. Load summary detail model

```python
from yahoo_api import YahooFinApi, Client

from pprint import pprint

def main():
	yf = YahooFinApi(
		Client(
			cache_response= True, 
			input_csv_file="./examples/freetrade_universe.csv", 
			download_folder_path="./data"
		)
	)

	sd = yf.get_summary_detail(["AAPL", "TSLA"])
	pprint(sd)

if __name__ == "__main__":
	main()
```

### 7. Get historic quotes

```python
from yahoo_fin_api import YahooFinApi, Client, FileCache

from pprint import pprint

def main():
	yf = YahooFinApi(Client(quote_cache=FileCache("./data/quotes", "quote")))

	quotes = yf.get_quote("AAPL", "max")

	pprint(quotes)

if __name__ == "__main__":
	main()
```

### Example of stock valuation based on 10 cap

```python
from yahoo_api import YahooFinApi, Client
from yahoo_api.universe import symbols as get_symbols

from pprint import pprint

BILLION = 1000000000

def main():
	yf = YahooFinApi(
		Client(
			cache_response= True,  
			download_folder_path="./data"
		)
	)

	symbols = [
		s.symbol for s in get_symbols("./examples/freetrade_universe.csv")
		if s.isa_eligible == True and s.plus_only == False
	]
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
				"cap_rate": cap_rate,
				"market_cap": summary.market_cap,
				"fcf": fin_data.free_cash_flow,
				"current_price": fin_data.current_price
			})

	res = sorted(res, key=lambda r: r["cap_rate"], reverse=True)
	pprint(res)


if __name__ == "__main__":
	main()
```