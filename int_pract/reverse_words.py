# given a phrase, return the same phrase with words in opposite order
#
# 'The fox is quick' --> 'quick is fox The'


def reverse_chars(letters):

    for i in range(len(letters)/2):
        letters[i], letters[-(i + 1)] = letters[-(i + 1)], letters[i]

    print letters
    return letters


def reverse_words(phrase):

    charlist = list(phrase)

    charlist = reverse_chars(charlist)

    begging_of_word = 0

    for i in range(len(charlist)):
        if charlist[i] == ' ':
            word = reverse_chars(charlist[begging_of_word: i])
            charlist[begging_of_word: i] = word
            begging_of_word = i + 1

        if i == len(charlist) - 1:
            word = reverse_chars(charlist[begging_of_word:])
            charlist[begging_of_word:] = word

    return ''.join(charlist)



# 'The fox is quick' -->
    # 'kciuq si xof ehT' -->
        # 'quick is fox The'


###############################################################################
# less absurd way to do this problem


def reverse_words(phrase):
    words = phrase.split(' ')

    for i in range(len(words)/2):
        words[i], words[-(i + 1)] = words[-(i + 1)], words[i]

    return ' '.join(words)









