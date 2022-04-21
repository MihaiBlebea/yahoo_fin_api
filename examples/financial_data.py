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
