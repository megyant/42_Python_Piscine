from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def __init__(self, data: any):
        self.data = data

    def process(self, data: any) -> str

    def validate(self, data: any) -> bool

    def format_output(self, result: str) -> str


class NumericProcessor:

class TextProcessor:

class LogProcessor: