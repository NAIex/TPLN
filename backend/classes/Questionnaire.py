from classes.questions.Question import Question
from classes.Gender import Gender
class Questionnaire:
	def __init__(self, questions_by_subscale: dict[str, list[Question]], gender: Gender):
		self.__questions_by_subscale = questions_by_subscale
		for _, questions in self.__questions_by_subscale.items():
			for question in questions:
				question.questionnaire = self
				for answer_option in question.answer_options:
					answer_option.questionnaire = self
		self.__gender = gender
	@property
	def questions_by_subscale(self) -> dict[str, list[Question]]: return self.__questions_by_subscale
	@property
	def gender(self) -> Gender: return self.__gender
	def gen(self):
		for subscale, questions in self.__questions_by_subscale.items():
			for question in questions:
				question.potentially_assign_answer_by_previous_answers()
				if question.still_needs_to_be_asked: continue
				yield question
