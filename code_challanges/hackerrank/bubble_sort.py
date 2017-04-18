bubble_sort.py

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))


total_swaps = 0

for i in range(n):
    swaps = 0

    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swaps += 1
            total_swaps += 1

    if swaps == 0:
        break


print 'Array is sorted in {} swaps.'.format(total_swaps)
print 'First Element: {}'.format(a[0])
print 'Last Element: {}'.format(a[-1])

