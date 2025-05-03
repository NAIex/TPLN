from classes.Gender import Gender

class AnswerOption:
	def __init__(self, text: dict[Gender, str]):
		self.__text = text
	def text(self, gender: Gender) -> str: return self.__text[gender]
