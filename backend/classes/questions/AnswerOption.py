from classes.Gender import Gender

class AnswerOption:
	@classmethod
	def no(cls, score_contribution: int=0, is_critical: bool=False) -> 'AnswerOption':
		return cls(Gender.same_for_all("nu"), score_contribution, is_critical)
	@classmethod
	def yes(cls, score_contribution: int=1, is_critical: bool=False) -> 'AnswerOption':
		return cls(Gender.same_for_all("da"), score_contribution, is_critical)
	def __init__(self, text: dict[Gender, str], score_contribution: int, is_critical: bool=False):
		self.__text = text
		self.__score_contribution = score_contribution
		self.__is_critical = is_critical
		self.__questionnaire = None
	@property
	def text(self) -> str: return self.__text[self.questionnaire.gender]
	@property
	def score_contribution(self) -> int: return self.__score_contribution
	@property
	def is_critical(self) -> bool: return self.__is_critical

	@property
	def questionnaire(self) -> 'Questionnaire': return self.__questionnaire
	@questionnaire.setter
	def questionnaire(self, questionnaire: 'Questionnaire'): self.__questionnaire = questionnaire

