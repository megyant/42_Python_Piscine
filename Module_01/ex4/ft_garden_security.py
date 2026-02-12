class SecurePlant:
    """ Protects its data from corruption """
    def __init__(self, name: str, height: int, age: int) -> None:
        """ Initializing SecurePlant attributes """
        self.name = name
        self.height = height
        self.age = age
        print(f"Plant created: {self.name}")

    def get_height(self) -> int:
        """ Retrieve current height information """
        return self.height

    def set_height(self, new_height: int) -> None:
        """ Update height information """
        if (new_height < 0):
            print(f'Invalid operation attepted: height {new_height}cm '
                  '[REJECTED]')
            print('Security: Negative height rejected')
        else:
            self.height = new_height
            print(f'Height updated: {self.height}cm [OK]')

    def get_age(self) -> int:
        """ Retrieve current age information """
        return self.age

    def set_age(self, new_age: int) -> None:
        """ Update age information """
        if (new_age < 0):
            print(f'Invalid operation attepted: age {new_age} days'
                  '[REJECTED]')
            print('Security: Negative height rejected')
        else:
            self.age = new_age
            print(f'Age updated: {self.age} days [OK]')

    def get_info(self) -> None:
        """ Summary of plant's current state """
        print(f'Current plant: {self.name} ({self.height}cm, {self.age} days)')


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = SecurePlant("Rose", 0, 0)
    rose.set_height(25)
    rose.set_age(30)
    print()

    rose.set_height(-5)
    print()

    rose.get_info()
