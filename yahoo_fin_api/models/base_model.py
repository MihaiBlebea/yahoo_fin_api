from __future__ import annotations
from datetime import datetime

class Model:

	end_date = 0

	def fmt_end_date(self)-> str | None:
		if self.end_date == 0:
			return None
		ts = datetime.fromtimestamp(self.end_date)
		return ts.strftime("%Y-%m-%d")