class AggressiveStrategy:
    def __init__(self, name):
        self.name = name

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"
    
    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets