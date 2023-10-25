from random import randrange

with open("numbers/1000000.txt", "w") as f:
    for i in range(10000000):
        f.write(str(randrange(0, 1000000)) + "\n")
