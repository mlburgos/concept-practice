def fibonacci(n, known_vals=None, parent=None):
    if n == 0 or n == 1:
        return n
    
    if known_vals is None:
        known_vals = [0]*(n + 1)
    
    print 'parent:', parent
    print 'current:', n

    if known_vals[n] == 0:
        known_vals[n] = fibonacci(n-1, known_vals, parent=n) + fibonacci(n-2, known_vals, parent=n)
        print known_vals
    
    return known_vals[n]
    