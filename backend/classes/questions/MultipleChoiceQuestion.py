from classes.questions.Question import Question
from classes.Gender import Gender
from classes.questions.AnswerOption import AnswerOption
from classes.Timeframe import Timeframe

from typing import Callable

class MultipleChoiceQuestion(Question):
	def __init__(self, text: dict[Gender, str], answer_options: list[AnswerOption], timeframe: Timeframe=Timeframe.none, turn_answer_into_score: Callable[[list[AnswerOption]], int]=lambda l: len(l)):
		Question.__init__(self, text, answer_options, timeframe)
		self.__turn_answer_into_score = turn_answer_into_score
		self.__answer = None
	@property
	def answer(self) -> list[AnswerOption]: return self.__answer
	@answer.setter
	def answer(self, answer: int | AnswerOption | list[int | AnswerOption]):
		if isinstance(answer, int): answer = self.answer_options[answer]
		if isinstance(answer, list): answer = [self.answer_options[i] if isinstance(i, int) else i for i in answer]
		if isinstance(answer, AnswerOption): answer = [answer]
		for a in answer:
			if a not in self.answer_options: raise self.not_in_candidates_error(a)
		self.__answer = answer
	@property
	def score_contribution(self) -> int: return self.__turn_answer_into_score(self.answer)
