import random

with open("numbers/10000.txt", "w") as f:
    for i in range(10000):
        f.write(str(random.randint(0, 10000)) + "\n")
