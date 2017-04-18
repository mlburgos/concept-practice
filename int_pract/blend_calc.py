# Create an interpreter for a simple lisp like language with two operators:
# 
# 4 => 4
# ( add 2 3 ) => 5
# ( mul 4 5 ) => 20
# ( mul ( add 3 2 1 ) 4 ) => 24
# ( mul ( add 3 2 1 ) ( add 3 2 1 ) ) => 24
# ( add ) => Error


def add(nums):
    """return the sum of the nums"""
    sum_ = 0
    for num in nums:
        sum_ += num
        
    return sum_


def mult(nums):
    """return the product of nums"""
    product = 1

    for num in nums:
        product *= num
    
    return product

# [ '(', 'add', '1', '2', ')']


def calculator(string):
    components = string.split()
    
    if components[0] == '(':
        components = components[1:]
    
    result, _ = _calculator(components)
    
    return result


def _calculator(components):
     
    if len(components) == 1:
        if components[0].isdigit():
            return int(components[0])
        else:
            return 'Error'
        
    nums = []
    
    index_adj = 0 
    i_adj = 0
    
    i = 0 
    while i < len(components):
    # for i, component in enumerate(components):
        # check for parens
        # check for add or mul
        
        component = components[i]
        
        if component == '(':
            inner, i_adj = _calculator(components[i + 1:])
            nums.append(inner)
            i += 1
        elif component == 'add' or component == 'mul':
            opp = component
        elif component == ')':
            break
        else:
            nums.append(int(component))
        
        
        i += i_adj + 1
        
        index_adj += 1
        
        print 'opp:', opp
        print 'i:', i
        print 'nums:', nums
    
    if nums == []:
        return 'Error'
    
    if opp == 'add':
        result = add(nums)
    else:
        result = mult(nums)
        
    print '(result, index_adj):', (result, index_adj)
    
    return (result, index_adj)
            

# print calculator('( mul 2 3 4 )')
# print calculator('( mul ( add 3 2 1 ) 4 )')
# print calculator('( sub ( add 3 2 1 ) 4 )')
        

################################################################################
# Better way to do this is with a stack


def calculator(string):
    components = string.split()

    stack = []

    for component in components:
        if component == ')':
            nums = []

            next_in_stack = stack.pop()

            while type(next_in_stack) == int:
                nums.append(next_in_stack)
                next_in_stack = stack.pop()

            print 'nums:', nums
            if next_in_stack == 'add':
                result = add(nums)
            elif next_in_stack == 'sub':
                result = sub(nums)
            else:
                result = mult(nums)

            stack.pop()

            stack.append(result)

            continue

        if component.isdigit():
            stack.append(int(component))
        else:
            stack.append(component)

    if len(stack) == 1:
        return stack[0]
    else:
        return 'Error'


def sub(nums):
    dif = 0

    for i, num in enumerate(nums):
        if i == 0:
            dif += nums[-1]
        else:
            dif -= nums[-(i + 1)]

        print dif

    return dif



