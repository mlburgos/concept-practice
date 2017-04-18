binary_search_ice_cream_parlor.py

# number of trips
t = int(raw_input().strip())
for a0 in xrange(t):
    # money pooled
    m = int(raw_input().strip())
    # number of flavors
    n = int(raw_input().strip())
    # list of prices
    a = map(int, raw_input().strip().split(' '))

    for i in range(n):
        if i < m:
            for j in range(i,n):
                if j != i and a[i] + a[j] == m:
                    print i, j

