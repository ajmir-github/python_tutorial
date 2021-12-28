class Person:
 def __init__(self, name, age):
  self.name = name
  self.age = age
 def introduce(self):
  print(f"This is {self.name}, and s/he is {self.age}.")


class User(Person):
 def __init__(self, name, age, email, position):
  super().__init__(name, age)
  self.email = email
  self.position = position
 def changePostion(self, newPostion):
  self.position = newPostion
 def checkPostion(self):
  print(f"{self.name} is a {self.position.lower()}.")


def register(name):
  print(f"{name} is registered!")

database_url = "https://domain_name.com"
