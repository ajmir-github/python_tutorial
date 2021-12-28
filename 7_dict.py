person = {
 "name":"Ahmad",
 "age":33,
 "postion":"manager"
}

print(person)
print(person["postion"])
print(person.get("title"))

person["age"] = 34
print(person)

person.pop("age")
person.clear()
print(person)