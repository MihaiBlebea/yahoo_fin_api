from yahoo_fin_api import YahooFinApi, Client, FileCache

from pprint import pprint

def main():
	yf = YahooFinApi(Client(FileCache("./data")))

	sd = yf.get_summary_detail(["AAPL", "TSLA"])
	pprint(sd)

if __name__ == "__main__":
	main()
