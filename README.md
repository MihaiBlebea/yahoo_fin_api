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