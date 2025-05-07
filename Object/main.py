# This line defines a new "blueprint" for creating objects. We're calling this blueprint "Person".
class Person:
    """Represents a person with a name, age, and gender."""
    # """This is a docstring (documentation string). It explains what the class does.
    # Represents a person with a name, age, gender, and a secret."""
    # These lines are type hints. They suggest what type of data each attribute should hold.
    # 'name' is expected to be a string (text).
    name: str
    # 'age' is expected to be an integer (whole number).
    age: int
    # 'gender' is expected to be a string.
    gender: str
    # 'secret' is also expected to be a string.
    secret: str # Note: This public type hint is for documentation; the actual storage is `__secret`

    # This is a special method called the "constructor".
    # It's automatically called when you create a new 'Person' object.
    # 'self' refers to the instance of the object being created.
    # 'name', 'age', 'gender', 'secret' are parameters that you pass in when creating a Person.
    def __init__(self, name: str, age: int, gender: str, secret: str):
        # These lines assign the values passed into the constructor to the object's attributes.
        # So, each Person object will have its own name, age, and gender.
        self.name = name
        self.age = age
        self.gender = gender
        # This attribute starts with double underscores. This is a convention in Python
        # for "name mangling", making it harder to access directly from outside the class.
        # It's often used for attributes that are considered "private" or internal to the class.
        self.__secret = secret

    # This is a method (a function that belongs to an object).
    # It allows controlled access to the '__secret' attribute.
    def get_secret(self):
        # It returns the value of the object's '__secret' attribute.
        return self.__secret

# Now, let's create an actual 'Person' object (an instance of the Person class).
# We're calling the Person class and passing in the required arguments for the __init__ method.
person1 = Person("John", 36, "male", "secret")
print(person1.name)
print(person1.age) 
print(person1.gender)
print(person1.get_secret())

# We can access the public attributes of our 'person1' object using dot notation.
print(person1.name)  # Output: John
print(person1.age)   # Output: 36
print(person1.gender) # Output: male

# To get the secret, we call the 'get_secret' method.
# We can't easily do person1.__secret because of name mangling (it would be person1._Person__secret).
print(person1.get_secret()) # Output: secret
