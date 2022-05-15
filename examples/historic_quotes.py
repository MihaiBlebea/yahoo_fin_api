from yahoo_fin_api import YahooFinApi, Client, FileCache

from pprint import pprint

def main():
	yf = YahooFinApi(Client(quote_cache=FileCache("./data/quotes", "quote")))

	quotes = yf.get_quote("AAPL", "1y")

	pprint(quotes)

if __name__ == "__main__":
	main()