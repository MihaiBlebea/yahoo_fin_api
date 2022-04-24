from yahoo_fin_api import YahooFinApi, Client, FileCache

from pprint import pprint

def main():
	yf = YahooFinApi(Client(FileCache("./data")))

	cf = yf.get_financial_data(["AAPL"])
	pprint(cf)

if __name__ == "__main__":
	main()
