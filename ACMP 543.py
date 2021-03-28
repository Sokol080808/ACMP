N, w, d, P = map(int, input().split())
correct_weight = N * (N - 1) * w // 2
error = correct_weight - P
if error == 0:
    answer = N
else:
    answer = error//d
print(answer)

