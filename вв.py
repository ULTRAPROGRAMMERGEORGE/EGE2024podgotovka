max_sum = -1
for n in range(4,10_000):
    s = '1' + '2' * n
    while '12' in s or '322' in s or '222' in s:
        if '12' in s:
            s = s.replace('12', '2', 1)
        if '322' in s:
            s = s.replace('322', '21', 1)
        if '222' in s:
            s = s.replace('222', '3', 1)
    summ = s.count('1') + 2 * s.count('2') + s.count('3') * 3
    max_sum = max(max_sum, summ)
print(max_sum)
