from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> list[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "type": "General Data"}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: list[Any]) -> str:
        if not isinstance(data_batch, list):
            return "ERROR: Invalid input data"
        total_processed = 0
        temp_sum: Union[int, float] = 0.0
        temp_count = 0
        average: Union[int, float] = 0
        try:
            for item in data_batch:
                total_processed += 1
                parts = str(item).split(':')
                if len(parts) == 2 and parts[0] == "temp":
                    temp_sum += float(parts[1])
                    temp_count += 1
            if temp_count > 0 or temp_count > 0.0:
                average = temp_sum / temp_count

            return (f"Sensor analysis: {total_processed} readings processed, "
                    f"avg temp: {average}°C")

        except (ValueError, IndexError):
            return "Error when processing Sensor data"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch

        data = []

        for item in data_batch:
            try:
                type, value_str = str(item).split(':')
                value = float(value_str)

                if type == "temp":
                    if criteria == "critical" and value > 37:
                        data.append(item)
                    elif criteria == "non-critical" and value <= 37:
                        data.append(item)
            except (ValueError, IndexError):
                continue

        return data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "type": "Environmental Data"}


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch) -> str:
        if not isinstance(data_batch, list):
            return "ERROR: Invalid input data"

        count = 0
        net_flow = 0

        try:
            for item in data_batch:
                count += 1
                flow = str(item).split(':')

                if len(flow) != 2:
                    return "Error when processing Transaction data"

                type, value = flow[0], int(flow[1])

                if type == "buy":
                    net_flow += value
                elif type == "sell":
                    net_flow -= value
                else:
                    return "Error when processing Transaction data"

            return (f"Transaction analysis: {count} operations, "
                    f"net flow: {net_flow:+} units")

        except (ValueError, IndexError):
            return "Error when processing Transaction data"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        if not isinstance(data_batch, list):
            return "ERROR: Invalid input data"

        data = []

        for item in data_batch:
            try:
                type, val_str = str(item).split(':')
                value = int(val_str)

                if type in ("buy", "sell"):
                    if criteria == "large" and value > 150:
                        data.append(item)
                    elif criteria == "small" and value <= 150:
                        data.append(item)

            except (ValueError, IndexError):
                continue

        return data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "type": "Financial Data"}


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch) -> str:
        if not isinstance(data_batch, list):
            return "ERROR: Invalid input data"

        count = 0
        count_error = 0

        for item in data_batch:
            count += 1
            if item in ("login", "error", "logout"):
                if item == "error":
                    count_error += 1
            else:
                return "Error when processing Event data"

        return (f"Event analysis: {count} events, "
                f"{count_error} error detected")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:

        if criteria is None:
            return data_batch

        if not isinstance(data_batch, list):
            return []

        return [item for item in data_batch if str(item) == criteria]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "type": "System Events"}


class StreamProcessor():
    def __init__(self) -> None:
        self.streams = []

    def add_stream(self, stream: DataStream) -> None:
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def process_all(self, stream_data: Dict[str, List[Any]]) -> None:
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        print("Batch 1 Results:")

        for stream in self.streams:
            data = stream_data.get(stream.stream_id, [])

            stream.process_batch(data)

            stats = stream.get_stats()
            type = stats['type'].split(' ')[0]

            if type == "Environmental":
                category = "Sensor"
                print(f"- {category} data: {len(data)} readings processed")
            elif type == "Financial":
                category = "Transaction"
                print(f"- {category} data: {len(data)} operations processed")
            elif type == "System":
                category = "Event"
                print(f"- {category} data: {len(data)} events processed")
            else:
                print('ERROR: Invalid input data')


def data_stream() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    s_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    t_data = ["buy:100", "sell:150", "buy:75"]
    e_data = ["login", "error", "logout"]

    print("Initializing Sensor Stream...")
    s_stream = SensorStream("SENSOR_001")
    s_stream_stats = s_stream.get_stats()
    print(f"Stream ID: {s_stream_stats['stream_id']}, "
          f"Type: {s_stream_stats['type']}")
    print(f"Processing sensor batch: {s_data}")
    print(f"{s_stream.process_batch(s_data)}")

    print("\nInitializing Transaction Stream...")
    t_stream = TransactionStream("TRANS_001")
    t_stream_stats = t_stream.get_stats()
    print(f"Stream ID: {t_stream_stats['stream_id']}, "
          f"Type: {t_stream_stats['type']}")
    print(f"Processing transaction batch: {t_data}")
    print(f"{t_stream.process_batch(t_data)}")

    print("\nInitializing Event Stream...")
    e_stream = EventStream("EVENT_001")
    e_stream_stats = e_stream.get_stats()
    print(f"Stream ID: {e_stream_stats['stream_id']}, "
          f"Type: {e_stream_stats['type']}")
    print(f"Processing event batch: {e_data}")
    print(f"{e_stream.process_batch(e_data)}")

    p_stream = StreamProcessor()
    p_stream.add_stream(s_stream)
    p_stream.add_stream(t_stream)
    p_stream.add_stream(e_stream)

    mixed_data_map = {
        "SENSOR_001": ["temp:38.0", "temp:42.0"],
        "TRANS_001": ["buy:30", "sell:200", "buy:100", "sell:50"],
        "EVENT_001": ["login", "error", "logout"]
    }

    p_stream.process_all(mixed_data_map)

    print("\nStream filtering active: High-priority data only")

    s_filtered = s_stream.filter_data(mixed_data_map["SENSOR_001"],
                                      criteria="critical")
    t_filtered = t_stream.filter_data(mixed_data_map["TRANS_001"],
                                      criteria="large")

    print(f"Filtered results: {len(s_filtered)} critical sensor alerts, "
          f"{len(t_filtered)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
