from yahoo_api.income_statement import IncomeStatements
from examples.cache_fin_data import main as cache_fin_data

from pprint import pprint

def main():
	cache_fin_data()

	statements = IncomeStatements.from_input_file("AAPL", "./data/AAPL.json")

	pprint(statements)

if __name__ == "__main__":
	main()