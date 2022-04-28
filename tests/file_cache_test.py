import unittest
import json
import time
from pathlib import Path
from yahoo_fin_api import FileCache

DIR = Path(__file__).resolve().parent


class TestFileCache(unittest.TestCase):

	symbol = "TEST"

	prefix = "test"

	def __save_to_cache(self, ttl: int = 10)-> FileCache:
		fc = FileCache(DIR, self.prefix, ttl)
		fc.to_cache(self.symbol, {"value": "testing the cache"})

		return fc

	def __clear_cache(self, fc):
		fc.clear_cache(self.symbol)

	def test_can_save_to_cache(self):
		fc = self.__save_to_cache()

		with open(f"{DIR}/{self.prefix}_{self.symbol}.json") as file:
			data = json.load(file)
			self.assertEqual(data["value"], "testing the cache")

			self.__clear_cache(fc)

	def test_can_clear_cache(self):
		fc = self.__save_to_cache()
		fc.clear_cache(self.symbol)

		found_file = Path(f"{DIR}/{self.prefix}_{self.symbol}.json").is_file()
		self.assertFalse(found_file)

	def test_cache_is_expired(self):
		fc = self.__save_to_cache(0)
		time.sleep(1)
		is_cached = fc.is_cached(self.symbol)
		self.assertFalse(is_cached)

		self.__clear_cache(fc)

	def test_cache_is_not_expired(self):
		fc = self.__save_to_cache(10)
		is_cached = fc.is_cached(self.symbol)
		self.assertTrue(is_cached)

		self.__clear_cache(fc)


if __name__ == "__main__":
    unittest.main()