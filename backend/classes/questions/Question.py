from abc import ABC, abstractmethod

from classes.Gender import Gender
from classes.Timeframe import Timeframe
from classes.questions.AnswerOption import AnswerOption

class Question(ABC):
	def __init__(self, text: dict[Gender, str], answer_options: list[AnswerOption], timeframe: Timeframe):
		self.__text = text
		self.__timeframe = timeframe
		self.__answer_options = answer_options
		self.questionnaire = None
		self.potentially_assign_answer_by_previous_answers = lambda: None
	@property
	def text(self) -> str: return self.timeframe.apply_to(self.__text[self.questionnaire.gender])
	@property
	def timeframe(self) -> Timeframe: return self.__timeframe
	@property
	def answer_options(self) -> list[AnswerOption]: return self.__answer_options

	@property
	@abstractmethod
	def answer(self): pass
	def not_in_candidates_error(self, a: AnswerOption):
		return ValueError(f"Answer {a.text} is not an answer candidate for {self.text} (candidates are: {[ao.text for ao in self.answer_options]}).")
	@answer.setter
	@abstractmethod
	def answer(self, answer: int | AnswerOption | list[int | AnswerOption]): pass
	@property
	@abstractmethod
	def score_contribution(self) -> int: pass

	@property
	def was_answered_negatively(self) -> bool: return self.answer == self.answer_options[0]

	@property
	def still_needs_to_be_asked(self) -> bool: return self.answer is None
