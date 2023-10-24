import random

with open("numbers/1000000.txt", "w") as f:
    for i in range(1000000):
        f.write(str(random.randint(0, 1000)) + "\n")
