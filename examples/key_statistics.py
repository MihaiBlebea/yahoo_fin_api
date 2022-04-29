from yahoo_fin_api import YahooFinApi, Client

from pprint import pprint

def main():
	yf = YahooFinApi(Client())

	cf = yf.get_key_statistics(["AAPL"])
	pprint(cf)

if __name__ == "__main__":
	main()
