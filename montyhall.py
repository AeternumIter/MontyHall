import random
results = []
while True:
    door = random.randrange(1,4)
    user = random.randrange(1,4)
    i = 0
    while i == 0:
        elim = random.randrange(1,4)
        if elim != door and elim != user:
            i+=1
    if door == user:
        results.append(0)
    else:
        results.append(1)
    probability = sum(results)
    print(probability/len(results))
