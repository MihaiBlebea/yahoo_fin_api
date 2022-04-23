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
	pprint(bs[0].balance_sheets[0].cash)

if __name__ == "__main__":
	main()