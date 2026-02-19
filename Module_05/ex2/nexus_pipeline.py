from abc import ABC, abstractmethod
from typing import Any, List, Union, Dict, Protocol


class ProcessingStage:
    def process(self, data: Any) -> Any:
        return data


class InputStage:
    def process(self, data: Any) -> Dict:

        if isinstance(data, dict):
            processed = {}
            if "sensor" in data:
                if data.get("sensor") in ("temp", "humidity", "pressure"):
                    processed.update({"sensor": data.get("sensor")})
                else:
                    return {}
                if "value" in data:
                    try:
                        processed.update({"value": float(data.get("value"))})
                    except ValueError:
                        print("ERROR: Invalid input")
                else:
                    return {}
                if "unit" in data:
                    try:
                        processed.update({"unit": data.get("unit")})
                    except ValueError:
                        print("ERROR: Invalid input")
                else:
                    return {}
            return processed

        if isinstance(data, str) and "," in data:
            processed = {}
            data_split = data.split(",")
            index = 1
            total_actions = 0
            if len(data_split) % 3 != 0:
                return {}
            while index < len(data_split):
                total_actions += 1
                index += 3
            processed.update({"actions": total_actions})
            return processed

        if isinstance(data, list):
            if len(data) == 0:
                return {}
            processed = {}
            total = 0
            index = 0
            while index < len(data):
                try:
                    total += float(data[index])
                    index += 1
                except ValueError:
                    print("ERROR: Invalid input")
            return processed
        else:
            return {}


class TransformStage:
    def process(self, data: Any) -> Dict:
        if not data:
            return None
        transformed = {}
        if "sensor" in data:
            transformed.update({"type": "sensor"})
            if data.get("sensor") == "temp":
                transformed.update({"sensor": "temperature"})
                transformed.update({"value": data["value"]})
                if data["value"] <= 5 or data["value"] >= 30:
                    transformed.update({"range": "Critical"})
                else:
                    transformed.update({"range": "Normal"})
                transformed.update({"unit": data["unit"]})
            else:
                transformed.update({"sensor": "pressure"})
                transformed.update({"value": data["value"]})
                if data["value"] <= 950 or data["value"] >= 1050:
                    transformed.update({"range": "Critical"})
                else:
                    transformed.update({"range": "Normal"})
                transformed.update({"unit": data["unit"]})
            return transformed
        if "actions" in data:
            transformed.update({"type": "user"})
            transformed.update({"actions": data["actions"]})
            return transformed
        if "readings" in data:
            transformed.update({"type": "stream"})
            transformed.update({"readings": data["readings"]})
            transformed.update({"average": data["average"]})
            return transformed
        return None

class OutputStage:
    def process(self, data: Any) -> str:
        if not data:
            return None
        if data["type"] == "sensor":
            value = data["value"]
            sensor_range = data["range"]


class ProcessingPipe(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage]

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    def add_stage(self, stage: ProcessingStage) -> None:
        if stage is not None:
            self.stages.append(stage)
