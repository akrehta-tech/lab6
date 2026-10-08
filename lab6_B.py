s = input().split()
rez = []
for i in range(len(s) + 1):
    if s[i] > s[i+1]:
        rez.append(s[i])
print(rez)