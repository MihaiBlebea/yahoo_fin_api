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


if __name__ == "__main__":
    unittest.main()