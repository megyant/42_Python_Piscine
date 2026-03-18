from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation\n"
          "========================================")

    print("Valid station created:")

    try:
        iss_valid = SpaceStation(
                    station_id="LGW125",
                    name="Titan Mining Outpost",
                    crew_size=6,
                    power_level=6.4,
                    oxygen_level=95.5,
                    last_maintenance="2023-07-11T00:00:00",
                    is_operational=True,
                    notes=None
        )
        print(f"ID: {iss_valid.station_id}")
        print(f"Name: {iss_valid.name}")
        print(f"Crew: {iss_valid.crew_size} people")
        print(f"Power: {iss_valid.power_level}%")
        print(f"Power: {iss_valid.oxygen_level}%")
        print("Status: "
              f"{'Operational' if iss_valid.is_operational else 'Inactive'}")
    except ValidationError as e:
        error_detail = e.errors()[0].get('msg')
        print(error_detail)

    print("\n========================================")
    print("Expected validation error:")

    try:
        iss_invalid = SpaceStation(
                station_id="LGW125",
                name="Titan Mining Outpost",
                crew_size=21,
                power_level=6.4,
                oxygen_level=95.5,
                last_maintenance="2023-07-11T00:00:00",
                is_operational=True,
                notes=None
        )

        print(f"ID: {iss_invalid.station_id}")
        print(f"Name: {iss_invalid.name}")
        print(f"Crew: {iss_invalid.crew_size} people")
        print(f"Power: {iss_invalid.power_level}%")
        print(f"Power: {iss_invalid.oxygen_level}%")
        print("Status: "
              f"{'Operational' if iss_invalid.is_operational else 'Inactive'}")

    except ValidationError as e:
        error_detail = e.errors()[0].get('msg')
        print(error_detail)


if __name__ == "__main__":
    main()
