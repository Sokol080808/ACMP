N = int(input())
i = 0
number = 0
while i < N:
    number += 1
    if len(str(number)) != len(set(str(number))):
        continue
    i += 1  

print(number)
