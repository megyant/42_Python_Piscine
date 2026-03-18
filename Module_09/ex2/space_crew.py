from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import List
from datetime import datetime
from enum import Enum


class Rank(Enum):
    cadet = 'cadet'
    officer = 'officer'
    lieutant = 'lieutant'
    captain = 'captain'
    commander = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_mission(self) -> 'SpaceMission':
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'")

        captain = 0
        commander = 0

        experienced = 0
        for member in self.crew:
            if member.rank == Rank.captain:
                captain += 1
            if member.rank == Rank.commander:
                commander += 1

            if member.years_experience >= 5:
                experienced += 1
        if captain == 0 and commander == 0:
            raise ValueError("Mission must have at least one Commander "
                             "or Captain")

        if self.duration_days > 365:
            if experienced < round(len(self.crew)/2):
                raise ValueError("Long missions (> 365 days) need"
                                 "50% experienced crew (5+ years)")

        for member in self.crew:
            if member.is_active is False:
                raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Station Data Validation\n"
          "========================================")

    print("Valid station created:")

    try:
        mission_valid = (SpaceMission(
            mission_id="M2024_TITAN",
            mission_name="Solar Observatory Research Mission",
            destination="Solar Observatory",
            launch_date="2024-03-30T00:00:00",
            duration_days=451,
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah Williams",
                    rank=Rank.captain,
                    age=43,
                    specialization="Mission Command",
                    years_experience=19,
                    is_active=True
                ),
                CrewMember(
                    member_id="CM002",
                    name="James Hernandez",
                    rank=Rank.captain,
                    age=43,
                    specialization="Pilot",
                    years_experience=30,
                    is_active=True
                ),
                CrewMember(
                    member_id="CM003",
                    name="Anna Jones",
                    rank=Rank.cadet,
                    age=35,
                    specialization="Communications",
                    years_experience=30,
                    is_active=True
                ),
                CrewMember(
                    member_id="CM004",
                    name="David Smith",
                    rank=Rank.commander,
                    age=27,
                    specialization="Security",
                    years_experience=15,
                    is_active=True
                ),
                CrewMember(
                    member_id="CM005",
                    name="Maria Jones",
                    rank=Rank.cadet,
                    age=55,
                    specialization="Research",
                    years_experience=30,
                    is_active=True
                )
            ],
            mission_status="planned",
            budget_millions=2208.1
        ))

        print(f"Mission: {mission_valid.mission_name}")
        print(f"ID: {mission_valid.mission_id}")
        print(f"Destination: {mission_valid.destination}")
        print(f"Duration: {mission_valid.duration_days} days")
        print(f"Budget: ${mission_valid.budget_millions}M")
        print(f"Crew size: {len(mission_valid.crew)}")
        print("Crew members: ")
        for member in mission_valid.crew:
            print(f"- {member.name} ({member.rank}) - {member.specialization}")

    except ValidationError as e:
        error_detail = e.errors()[0].get('msg')
        print(error_detail)

    print("\n========================================")
    print("Expected validation error:")

    try:
        mission_invalid = (SpaceMission(
            mission_id="M2024_TITAN",
            mission_name="Solar Observatory Research Mission",
            destination="Solar Observatory",
            launch_date="2024-03-30T00:00:00",
            duration_days=451,
            crew=[
                CrewMember(
                    member_id="CM001",
                    name="Sarah Williams",
                    rank=Rank.cadet,
                    age=43,
                    specialization="Mission Command",
                    years_experience=19,
                    is_active=True
                ),
                CrewMember(
                    member_id="CM002",
                    name="James Hernandez",
                    rank=Rank.cadet,
                    age=43,
                    specialization="Pilot",
                    years_experience=30,
                    is_active=True
                ),
                CrewMember(
                    member_id="CM003",
                    name="Anna Jones",
                    rank=Rank.cadet,
                    age=35,
                    specialization="Communications",
                    years_experience=30,
                    is_active=True
                ),
                CrewMember(
                    member_id="CM004",
                    name="David Smith",
                    rank=Rank.cadet,
                    age=27,
                    specialization="Security",
                    years_experience=15,
                    is_active=True
                ),
                CrewMember(
                    member_id="CM005",
                    name="Maria Jones",
                    rank=Rank.cadet,
                    age=55,
                    specialization="Research",
                    years_experience=30,
                    is_active=True
                )
            ],
            mission_status="planned",
            budget_millions=2208.1
        ))

        print(f"Mission: {mission_invalid.mission_name}")
        print(f"ID: {mission_invalid.mission_id}")
        print(f"Destination: {mission_invalid.destination}")
        print(f"Duration: {mission_invalid.duration_days} days")
        print(f"Budget: ${mission_invalid.budget_millions}M")
        print(f"Crew size: {len(mission_invalid.crew)}")
        print("Crew members: ")
        for member in mission_invalid.crew:
            print(f" - {member.name} ({member.rank}) - "
                  f"{member.specialization}")

    except ValidationError as e:
        error_detail = e.errors()[0].get('msg')
        final_msg = error_detail.replace("Value error, ", "")
        print(final_msg)


if __name__ == "__main__":
    main()
