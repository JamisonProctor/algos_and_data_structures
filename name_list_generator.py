import random

# Sample list of first names
first_names = [
    "Alice", "Bob", "Charlie", "David", "Emily", "Fiona",
    "George", "Helen", "Ivan", "Jill", "Kevin", "Laura"
]

# Sample list of last names
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller",
    "Davis", "Garcia", "Rodriguez", "Martinez", "Hernandez", "Kim"
]

random_names = [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(100)]
random_names_str = "\n".join(random_names)

# Convert the list to a single string
with open("names/unsorted.txt", "w") as f:
    
    f.write(random_names_str)

