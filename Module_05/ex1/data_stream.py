from abc import ABC, abstractmethod
from typing import Any, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: list[Any]) -> str:
        pass

    def filter_data(self, data_batch: list[Any],
                    criteria: Optional[str] = None) -> list[Any]:
        return data_batch

    def get_stats(self) -> dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id}

class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
    
    def process_batch(self, data_batch):
        return super().process_batch(data_batch)

class TransactionStream(DataStream):

class EventStream(DataStream):