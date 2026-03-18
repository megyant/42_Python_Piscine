from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    radio = 'radio'
    visual = 'visual'
    physical = 'physical'
    telepathic = 'telepathic'


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None,
                                            max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_contact(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start"
                             "with 'AC' (Alien Contact)")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.telepathic
           and self.witness_count < 3):
            raise ValueError("Telepathic contact requires at "
                             "least 3 witnesses")
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals (> 7.0) "
                             "should include received messages")

        return self


def main() -> None:
    print("Space Station Data Validation\n"
          "========================================")

    print("Valid station created:")

    try:
        alien_valid = AlienContact(
                    contact_id="AC_2024_001",
                    timestamp="2024-01-20T00:00:00",
                    location="Atacama Desert, Chile",
                    contact_type="visual",
                    signal_strength=9.6,
                    duration_minutes=99,
                    witness_count=11,
                    message_received="Greetings from Zeta Reticuli",
                    is_verified=False
        )
        print(f"ID: {alien_valid.contact_id}")
        print(f"Type: {alien_valid.contact_type}")
        print(f"Location: {alien_valid.location}")
        print(f"Signal: {alien_valid.signal_strength}%")
        print(f"Duration: {alien_valid.duration_minutes}%")
        print(f"Witnesses: {alien_valid.witness_count}")
        print(f"Message: '{alien_valid.message_received}'")

    except ValidationError as e:
        error_detail = e.errors()[0].get('msg')
        print(error_detail)

    print("\n========================================")
    print("Expected validation error:")

    try:
        alien_invalid = AlienContact(
                contact_id="AC_2024_001",
                timestamp="2024-01-20T00:00:00",
                location="Atacama Desert, Chile",
                contact_type="telepathic",
                signal_strength=9.6,
                duration_minutes=99,
                witness_count=2,
                message_received="Greetings from Zeta Reticuli",
                is_verified=False
        )

        print(f"ID: {alien_invalid.contact_id}")
        print(f"Type: {alien_invalid.contact_type}")
        print(f"Location: {alien_invalid.location}")
        print(f"Signal: {alien_invalid.signal_strength}%")
        print(f"Duration: {alien_invalid.duration_minutes}%")
        print(f"Witnesses: {alien_invalid.witness_count}")
        print(f"Message: '{alien_invalid.message_received}'")

    except ValidationError as e:
        error_detail = e.errors()[0].get('msg')
        final_msg = error_detail.replace("Value error, ", "")
        print(final_msg)


if __name__ == "__main__":
    main()
