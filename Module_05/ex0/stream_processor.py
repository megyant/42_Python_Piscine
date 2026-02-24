from abc import ABC, abstractmethod
from typing import Any, List


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
        if isinstance(data, List):
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

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "ERROR: Invalid text data"
        len_chars = len(data)
        len_words = len(data.split())
        return self.format_output("Processed text: "
                                  f"{len_chars} characters, "
                                  f"{len_words} words")

    def format_output(self, result: str):
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if data.find("ERROR") or data.find("INFO"):
            return True
        return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "ERROR: Invalid log format"
        elif "ERROR" in data:
            return self.format_output("[ALERT] ERROR level dected: "
                                      "Connection timeout")
        elif "INFO" in data:
            return self.format_output("[ALERT] INFO level dected: "
                                      "System ready")

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def data_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")

    try:
        process_n = NumericProcessor()
        data_n = [1, 2, 3, 4, 5]

        print(f"Processing data: {data_n}")

        if process_n.validate(data_n):
            print("Validation: Numeric data verified")
            print(process_n.format_output(data_n))
        else:
            raise ValueError("ERROR: Invalid intput")
    except ValueError as e:
        print(e)

    print("\nInitializing Text Processor...")

    try:
        process_t = TextProcessor()
        data_t = "Hello Nexus World"

        print(f"Processing data: {data_t}")
        if process_t.validate(data_t):
            print("Validation: Text data verified")
            print(process_t.process(data_t))
        else:
            raise ValueError("ERROR: Invalid intput")
    except ValueError as e:
        print(e)

    print("\nInitializing Log Processor...")

    try:
        process_log = LogProcessor()
        data_log = "ERROR: Connection timeout"

        print(f"Processing data: {data_log}")

        if process_log.validate(data_log):
            print("Validation: Log entry verified")
            print(process_log.process(data_log))
        else:
            raise ValueError("ERROR: Invalid input")
    except ValueError as e:
        print(e)

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    try:
        processors = [process_n, process_t, process_log]
        datasets = [[1, 2, 3], "Hello World", "INFO: System ready"]

        for i in range(len(processors)):
            proc = processors[i]
            data = datasets[i]

            result_num = i + 1

            output = proc.process(data).replace('Output: ', '')

            print(f"Result {result_num}: {output}")
    except ValueError:
        print("ERROR: Invalid input")


if __name__ == "__main__":
    data_processor()
