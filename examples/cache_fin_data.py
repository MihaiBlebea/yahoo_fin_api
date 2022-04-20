from yahoo_api.yahooapi import YahooApi
from pprint import pprint

def main():
	yapi = YahooApi(
		cache_response= True, 
		input_csv_file="./examples/freetrade_universe.csv", 
		download_folder_path="./data")

	symbols = yapi.get_symbols()

	pprint(symbols[0])

if __name__ == "__main__":
	main()