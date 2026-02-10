from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    @abstractmethod

    def process(self, data: Any) -> str:
        pass

    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        pass


class NumericProcessor(DataProcessor):

class TextProcessor(DataProcessor):

class LogProcessor(DataProcessor):
    a
