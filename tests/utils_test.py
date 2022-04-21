import unittest
import yahoo_api.utils as Utils

class TestUtilsFunctions(unittest.TestCase):

	def test_extract_key(self):
		data = {
			"a": {
				"b": {
					"c": 1000
				}
			}
		}
		val = Utils.extract_key(data, "a", "b", "c")
		self.assertEqual(1000, val)

		val = Utils.extract_key(data, "a", "b")
		self.assertEqual({"c": 1000}, val)

		val = Utils.extract_key(data, "a", "d")
		self.assertEqual(None, val)

	def test_calculate_growth_rate(self):
		initial = 10.01
		final = 20.01

		res = Utils.calculate_growth_rate(initial, final)
		self.assertEqual(100, res)

	def test_format_amount(self):
		amount = 1000000

		res = Utils.format_amount(amount)
		self.assertEqual("$1,000,000", res)



if __name__ == "__main__":
    unittest.main()