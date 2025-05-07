class Person:
    """Represents a person with a name, age, and gender."""
    name: str
    age: int
    gender: str

    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

person1 = Person("John", 36, "male")
print(person1.name)
print(person1.age)
print(person1.gender)
