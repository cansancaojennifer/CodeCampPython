lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Igor", "Caye", "Guzguz", "Gabiel", "Isa", "Isa", "Kurby", "Jhuly", "Raissa", "Pedro"]
# friends.extend(lucky_numbers)
# friends.append("Emilly")
friends.insert(1, "Alice")
friends.remove("Gabiel")
# friends.clear()
# friends.pop()
# firends.sort() <-- alphabetical order

print(friends)
print(friends.index("Caye"))
print(friends.count("Isa"))