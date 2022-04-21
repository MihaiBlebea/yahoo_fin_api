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

	cfs = yf.get_cashflow_statements(["SHOP"])[0]

	for cf in cfs.cashflows:
		print(cf.fmt_end_date())
		pprint(cf.free_cash_flow(True))

if __name__ == "__main__":
	main()