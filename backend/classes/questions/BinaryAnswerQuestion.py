from classes.questions.Question import Question

from classes.Gender import Gender
from classes.Timeframe import Timeframe

class BinaryAnswerQuestion(Question):
	def __init__(self, text: dict[Gender, str], timeframe: Timeframe=Timeframe.none, is_critical: bool=False):
		Question.__init__(self, text, timeframe)
		self.__is_critical = is_critical
	@property
	def is_critical(self): return self.__is_critical
	@property
	def score_contribution(self, answer: bool) -> int: return 0 if answer == False else 1
