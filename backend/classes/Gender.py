import enum

class Gender(enum.StrEnum):
	M = enum.auto()
	F = enum.auto()
	@classmethod
	def same_for_all(cls, value: str):
		return {k: value for k in iter(cls)}