from yahoo_api.balance_sheet import BalanceSheets
from examples.cache_fin_data import main as cache_fin_data

from pprint import pprint

def main():
	cache_fin_data()

	balance_sheets = BalanceSheets.from_input_file("AAPL", "./data/AAPL.json")

	pprint(balance_sheets)

if __name__ == "__main__":
	main()