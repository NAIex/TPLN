from abc import ABC, abstractmethod

from classes.Gender import Gender
from classes.Timeframe import Timeframe

class Question(ABC):
	__global_id = 1
	def __init__(self, text: dict[Gender, str], timeframe: Timeframe):
		self.__id = Question.__global_id
		Question.__global_id += 1
		self.__text = text
		self.__timeframe = timeframe
	def text(self, gender: Gender) -> str: return self.timeframe.apply_to(self.__text[gender])
	@property
	def id(self) -> int: return self.__id
	@property
	def timeframe(self) -> Timeframe: return self.__timeframe
	@property
	@abstractmethod
	def is_critical(self) -> bool: pass

	@property
	def json(self) -> dict:
		return {
			'id': self.id,
			'text': self.text(Gender.M),
			'timeframe': self.timeframe.json,	
			'is_critical': self.is_critical,
		}
	
