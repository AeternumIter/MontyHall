import random
import sys
results = []
for l in range(1000000):
    door = random.randrange(1,4)
    user = random.randrange(1,4)
    i = 0
    while i == 0:
        elim = random.randrange(1,4)
        if elim != door and elim != user:
            i+=1
    i = 0
    while i == 0:
        rem = random.randrange(1,4)
        if rem != elim and rem != user:
            i+=1
    if rem == door:
        results.append(1)
    elif door == user:
        results.append(0)
    else:
        sys.exit("Error")
    probability = sum(results)
    print(probability/len(results))
