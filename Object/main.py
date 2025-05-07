class Person:
    """Represents a person with a name, age, and gender."""
    name: str
    age: int
    gender: str
    secret: str

    def __init__(self, name: str, age: int, gender: str, secret: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.__secret = secret
    def get_secret(self):
        return self.__secret

person1 = Person("John", 36, "male", "secret")
print(person1.name)
print(person1.age) 
print(person1.gender)
print(person1.get_secret())