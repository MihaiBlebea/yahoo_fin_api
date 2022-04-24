from __future__ import annotations
from typing import List
import csv
from dataclasses import dataclass
import requests

UNIVERSE_BASE_URL = "https://raw.githubusercontent.com/MihaiBlebea/yahoo_fin_api/master/universe"
FREETRADE_FILE = "freetrade.csv"

class Universe:
	def get_freetrade_universe()-> List[str] | None:
		res = requests.get(f"{UNIVERSE_BASE_URL}/{FREETRADE_FILE}")
		
		if res.status_code != 200:
			return None

		body = res.json()

		csvreader = csv.reader(body)
		next(csvreader, None)
		return [ r[7] for r in csvreader ]

	def get_sp_500_universe()-> List[str]:
		pass

	def get_ftse_100_universe()-> List[str]:
		pass

@dataclass
class Symbol:

	title: str

	symbol: str

	industry: str

	curency: str

	isa_eligible: bool

	plus_only: bool

	def from_csv_row(
		title: str, 
		symbol: str, 
		industry: str, 
		currency: str, 
		isa_eligible: str, 
		plus_only: str)-> Symbol:

		symbol = "".join([l for l in symbol if l.upper() == l])

		return Symbol(
			title,
			symbol,
			industry.lower(),
			currency,
			isa_eligible=True if isa_eligible == "TRUE" else False,
			plus_only=True if plus_only == "TRUE" else False
		)

	def get_symbol(self)-> str:
		return self.symbol.upper()


def symbols(input_file: str)-> List[Symbol]:
	with open(input_file) as file:
		csvreader = csv.reader(file)
		next(csvreader, None)
		symbols = [
			Symbol.from_csv_row(r[1], r[7], r[2], r[3], r[4], r[10]) 
			for r in csvreader
		]

		print(f"Found {len(symbols)} symbols in the universe")

		return [symbol for symbol in symbols if symbol.isa_eligible == True]

if __name__ == "__main__":
	from pprint import pprint
	universe = Universe.get_freetrade_universe()
	pprint(universe)