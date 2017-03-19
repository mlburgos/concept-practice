making_anagrams.py

def gen_counter(str):
    counter = {}
    for letter in str:
        counter[letter] = counter.get(letter, 0) + 1
    
    return counter

def number_needed(a, b):
    counter_a = gen_counter(a)
    counter_b = gen_counter(b)
    
    count = 0 
    
    for letter in counter_a:
            count += abs(counter_a[letter] - counter_b.get(letter, 0))
    
    for letter in counter_b:
        if letter not in counter_a:
            count += counter_b[letter]
    
    return count
    
a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
