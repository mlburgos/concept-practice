# given a url, store it in a trie

# {d: {o: {n: {u: { t: {}
#                  }
#              },
#          g: {o: {}
#              .: {c: {o: {m: [*, {/: *}]}}
#                  o: {r: {g: *}}
#                  }
#              }
#          }
#      }
#  }


# url_storage = {}

# def store_string(string):
#     # find the starting point
    
#     current_dict = url_storage
    
#     for i, letter in enumerate(string):
#         if letter in current_dict:
#             current_dict = current_dict[letter]


#     i = 0
#     while True:
#         letter = string[i]

#         if letter in current_dict:
#             i += 1
#             continue

#         break

#     current_dict 
#     _store_string(string, url_storage)


# def _store_string(remaining_str, current_dict):
#     if len(remaining_str) == 1:
#         return {current_dict[remaining_str[0]]: '*'}


################################################################################
# my version
class Trie_mb(object):

    def __init__(self):
        self.root_dict = {}


    def check_and_add(self, word):

        current_dict = self.root_dict

        for char in word:
            # if char not in current_dict
            #     current_dict[char] = {}

            # current_dict = current_dict[char]
            current_dict[char] = current_dict.get(char, {})
            current_dict = current_dict[char]

        current_dict['End of word'] = current_dict.get('End of word', {})


################################################################################
# Parker's version

class Trie:

    def __init__(self):
        self.root_node = {}

    def check_present_and_add(self, word):

        current_node = self.root_node
        is_new_word = False

        # Work downwards through the trie, adding nodes
        # as needed, and keeping track of whether we add
        # any nodes.
        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}
            current_node = current_node[char]

        # Explicitly mark the end of a word.
        # Otherwise, we might say a word is
        # present if it is a prefix of a different,
        # longer word that was added earlier.
        if "End Of Word" not in current_node:
            is_new_word = True
            current_node["End Of Word"] = {}

        return is_new_word

