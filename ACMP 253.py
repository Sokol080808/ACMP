counter = 0

start = list(map(int, input().split()))
end = list(map(int, input().split()))

time1 = start[0] * 60 + start[1]
time1_1 = time1 + (0 - time1 % 30) % 30
time2 = end[0] * 60 + end[1]

if time1 <= time2 and time1_1 > time2:
    print(0)
else:
    time1 = time1_1
    if time2 < time1:
        time2 += 60 * 24
    for i in range(time1, time2 + 1, 30):
        if i % 60 == 30:
            counter += 1
        else:
            if (i//60) % 12 != 0:
                counter += (i // 60) % 12
            else:
                counter += 12

    print(counter)
