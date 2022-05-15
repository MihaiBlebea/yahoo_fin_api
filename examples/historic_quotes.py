from yahoo_fin_api import YahooFinApi, Client, FileCache

from pprint import pprint

def main():
	yf = YahooFinApi(Client())

	quotes = yf.get_quote("AAPL", "1y", "3mo")

	pprint(quotes)

if __name__ == "__main__":
	main()