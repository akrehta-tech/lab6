import random
res = []
for i in range(6):
    s = str(random.randint(1, 49))
    if s not in res:
        res.append(s)
print(" ".join(res))