from classes.questions.Question import Question
from classes.Gender import Gender
from classes.questions.AnswerOption import AnswerOption
from classes.Timeframe import Timeframe

from typing import Callable

class MultipleChoiceQuestion(Question):
	def __init__(self, text: dict[Gender, str], answer_options: list[AnswerOption], timeframe: Timeframe=Timeframe.none, turn_answer_into_score: Callable[[list[bool]], int]=lambda l: sum(map(int, l))):
		Question.__init__(self, text, timeframe)
		self.__answer_options = answer_options
		self.__turn_answer_into_score = turn_answer_into_score
	@property
	def answer_options(self) -> list[AnswerOption]: return self.__answer_options
	@property
	def score_contribution(self, answer: list[bool]) -> int: return self.__turn_answer_into_score(answer)
	@property
	def is_critical(self) -> bool: return False

	@property
	def json(self):
		s = super().json
		s["answer_options"] = list(map(lambda ao: ao.text(Gender.M), self.answer_options))
		return s
