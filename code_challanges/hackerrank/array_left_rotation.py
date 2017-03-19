
def array_left_rotation(a, n, k):
    i = k % n
    new_a = a[i:] + a[:i]

    for num in new_a:
        print num,

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k)
print ' '.join(map(str,answer))
