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
from yahoo_api.yahooapi import YahooApi
from pprint import pprint

def main():
	yapi = YahooApi(
		cache_response= True, # Should cache the response after fetching from API
		input_csv_file="./examples/freetrade_universe.csv", # Load the universe from this file
		download_folder_path="./data") # Cache the data from the API in this folder

	symbols = yapi.get_symbols()

	pprint(symbols[0])

if __name__ == "__main__":
	main()
```

### 2. Load the balance sheet models

```python
from yahoo_api.balance_sheet import BalanceSheets
from examples.cache_fin_data import main as cache_fin_data

from pprint import pprint

def main():
	cache_fin_data()

	balance_sheets = BalanceSheets.from_input_file("AAPL", "./data/AAPL.json")

	pprint(balance_sheets)

if __name__ == "__main__":
	main()
```

### 3. Load the cash flow models

```python
from yahoo_api.cashflow import CashFlows
from examples.cache_fin_data import main as cache_fin_data

from pprint import pprint

def main():
	cache_fin_data()

	cfs = CashFlows.from_input_file("AAPL", "./data/AAPL.json")

	pprint(cfs)

if __name__ == "__main__":
	main()
```

### 4. Load the income statement model

```python
from yahoo_api.income_statement import IncomeStatements
from examples.cache_fin_data import main as cache_fin_data

from pprint import pprint

def main():
	cache_fin_data()

	statements = IncomeStatements.from_input_file("AAPL", "./data/AAPL.json")

	pprint(statements)

if __name__ == "__main__":
	main()
```