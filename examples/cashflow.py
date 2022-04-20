from yahoo_api.cashflow import CashFlows
from examples.cache_fin_data import main as cache_fin_data

from pprint import pprint

def main():
	cache_fin_data()

	cfs = CashFlows.from_input_file("AAPL", "./data/AAPL.json")

	pprint(cfs)

if __name__ == "__main__":
	main()