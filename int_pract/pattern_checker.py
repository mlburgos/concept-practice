

def pattern_checker(string, pattern):
    return _pattern_checker(string=string, pattern=pattern, s_i=0, p_i=0, last_letter=None)


def _pattern_checker(string, pattern, s_i, p_i, last_letter):

    print 'string[s_i:]:', string[s_i:]
    print 'pattern[p_i:]:', pattern[p_i:]

    # Base Cases
    # Case 1: Exhausted the entire string AND exhausted the pattern
    if s_i == len(string) and p_i == len(pattern):
        return True
    # Case 2: Exausted the entire string, and the current pattern char is '*';
    # proceed to the next pattern char
    elif s_i == len(string) and pattern[p_i] == '*':
        _pattern_checker(string=string,
                         pattern=pattern,
                         s_i=s_i,
                         p_i=p_i + 1,
                         last_letter=string[s_i],
                         )
    # Case 3: One is exhausted but the other is not, and the remaining chars in
    # the pattern are not '*'s
    elif s_i == len(string) or p_i == len(pattern):
        return False

    if string[s_i] == pattern[p_i] or pattern[p_i] == '?':
        return _pattern_checker(string=string,
                                pattern=pattern,
                                s_i=s_i + 1,
                                p_i=p_i + 1,
                                last_letter=None,
                                )

    elif pattern[p_i] == '*':
        # Case 1: zero
        zero = _pattern_checker(string=string,
                                pattern=pattern,
                                s_i=s_i,
                                p_i=p_i + 1,
                                last_letter=string[s_i],
                                )

        # Case 2: more than zero
        if last_letter is None:
            more_than_zero = _pattern_checker(string=string,
                                              pattern=pattern,
                                              s_i=s_i + 1,
                                              p_i=p_i,
                                              last_letter=string[s_i],
                                              )
        elif string[s_i] == last_letter:
            more_than_zero = _pattern_checker(string=string,
                                              pattern=pattern,
                                              s_i=s_i + 1,
                                              p_i=p_i,
                                              last_letter=last_letter,
                                              )
        # end the '*' cycle
        else:
            more_than_zero = _pattern_checker(string=string,
                                              pattern=pattern,
                                              s_i=s_i,
                                              p_i=p_i + 1,
                                              last_letter=last_letter,
                                              )

        return any([zero, more_than_zero])




s = 'annnnts'
s2 = 'annnznts'
s3 = 'azzzznts'
s4 = s3 + 'z'

p = 'a*nts'
p2 = 'a*nt*'
p3 = 'a*nt**'
p4 = 'a*nt***'




