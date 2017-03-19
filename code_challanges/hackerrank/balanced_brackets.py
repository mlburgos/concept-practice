

def is_matched(expression):
    bracket_stack = []

    mates = {'[': ']',
             '{': '}',
             '(': ')',
             }

    for bracket in expression:
        if len(bracket_stack) > 0:
            if bracket == mates.get(bracket_stack[-1]):
                bracket_stack.pop()
                continue

        bracket_stack.append(bracket)

    return bracket_stack == []


# is_matched('[[{}]]')
