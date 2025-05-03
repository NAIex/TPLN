from abc import ABC, abstractmethod

from classes.Gender import Gender
from classes.Timeframe import Timeframe

class Question(ABC):
	def __init__(self, text: dict[Gender, str], timeframe: Timeframe):
		self.__text = text
		self.__timeframe = timeframe
	def text(self, gender: Gender) -> str: return self.timeframe.apply_to(self.__text[gender])
	@property
	def timeframe(self) -> Timeframe: return self.__timeframe
	@property
	@abstractmethod
	def is_critical(self) -> bool: pass
