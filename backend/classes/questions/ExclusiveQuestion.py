from classes.questions.Question import Question
from classes.questions.AnswerOption import AnswerOption

from classes.Gender import Gender
from classes.Timeframe import Timeframe

class ExclusiveQuestion(Question):
	def __init__(self, text: dict[Gender, str], answer_options: list[AnswerOption], timeframe: Timeframe=Timeframe.none):
		Question.__init__(self, text, answer_options, timeframe)
		self.__answer = None
	@property
	def answer(self) -> AnswerOption: return self.__answer
	@answer.setter
	def answer(self, answer: int | AnswerOption | list[int | AnswerOption]):
		if isinstance(answer, int):
			answer = self.answer_options[answer]
		if isinstance(answer, list):
			answer = [self.answer_options[i] if isinstance(i, int) else i for i in answer]
			if len(answer) != 1:
				raise ValueError(f"Received {len(answer)} answers, but expected 1.")
			answer = answer[0]
		if answer not in self.answer_options: raise self.not_in_candidates_error(answer)
		self.__answer = answer
	@property
	def score_contribution(self) -> int: return self.answer.score_contribution
