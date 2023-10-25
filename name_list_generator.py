import random

# Sample list of first names
first_names = [
    "Alice", "Bob", "Charlie", "David", "Emily", "Fiona", "George", "Helen",
    "Ivan", "Julia", "Kevin", "Laura", "Megan", "Nathan", "Olivia", "Paul",
    "Quincy", "Rita", "Steve", "Tracy", "Ursula", "Victor", "Wendy", "Xander",
    "Yvonne", "Zane", "Angela", "Brian", "Catherine", "Derek", "Eleanor",
    "Frank", "Grace", "Henry", "Isabelle", "Jack", "Kathy", "Leo", "Monica",
    "Neil", "Ophelia", "Peter", "Quinn", "Rebecca", "Samuel", "Tina",
    "Ulysses", "Vera", "William", "Xena", "Yasmine", "Zach", "Allison",
    "Bernard", "Cecilia", "Don", "Elise", "Freddie", "Gloria", "Howard",
    "Iris", "Jeremy", "Karen", "Louis", "Melissa", "Nigel", "Oscar",
    "Pamela", "Quinton", "Renee", "Sylvia", "Tom", "Uma", "Vince",
    "Winona", "Xerxes", "Yara", "Zelda", "Anthony", "Bianca", "Cliff",
    "Deborah", "Eugene", "Felicia", "Gwen", "Harold", "Ingrid", "Jake",
    "Kristen", "Lloyd", "Madeline", "Norman", "Opal", "Priscilla",
    "Quincy", "Ralph", "Sabrina", "Timothy", "Ursula", "Valerie", "Walter",
    "Xiomara", "Yusuf", "Zara"
]

# Sample list of last names
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
    "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker",
    "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy",
    "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey",
    "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson", "Watson",
    "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz",
    "Hughes", "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long",
    "Ross", "Foster", "Jimenez"
]

random_names = [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(10000)]
random_names_str = "".join(random_names)

# Convert the list to a single string
with open("names/unsorted.txt", "w") as f:
    f.write(random_names_str)

