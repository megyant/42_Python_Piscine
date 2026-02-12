from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for number in data:
                if not isinstance(number, int):
                    return False
            return True
        return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "ERROR: Invalid numeric data"

        len_list = len(data)
        sum_list = sum(data)
        avg_list = sum_list / len_list

        if isinstance(data, int):
            return f"Processed 1 numeric value, sum={data}, avg={data:.1f}"

        else:
            return self.format_output(f"Processed {len_list} numeric values, "
                                      f"sum={sum_list}, "
                                      f"avg={avg_list:.1f}")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for string in data:
                if not isinstance(string, str):
                    return False
            return True
        return False

#class LogProcessor(DataProcessor):
    #a


def data_processor():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")

if __name__ == "__main__":
    data_processor()
