from yahoo_fin_api import YahooFinApi, Client, FileCache

from pprint import pprint

def main():
	yf = YahooFinApi(Client(FileCache("./data")))

	bs = yf.get_balance_sheets(["AAPL", "TSLA"])
	pprint(bs)

if __name__ == "__main__":
	main()