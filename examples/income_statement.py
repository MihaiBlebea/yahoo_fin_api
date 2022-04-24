from yahoo_fin_api import YahooFinApi, Client, FileCache

from pprint import pprint

def main():
	yf = YahooFinApi(Client(FileCache("./data")))

	i_stmts = yf.get_income_statements(["AAPL", "TSLA"])
	pprint(i_stmts)

if __name__ == "__main__":
	main()