import enum

class Timeframe(enum.StrEnum):
	none = enum.auto()
	last_2_weeks = enum.auto()
	last_6_months = enum.auto()

	def apply_to(self, text: str) -> str:
		match self:
			case Timeframe.none:
				return text
			case Timeframe.last_2_weeks:
				return "În ultimele 2 săptămâni, " + text
			case Timeframe.last_6_months:
				return "În ultimele 6 luni, " + text