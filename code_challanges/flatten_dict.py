def flatten(dic):

    new_dict = {}

    print _flatten(dic, new_dict, '')


def _flatten(dic, new_dict, prefix):
    for key, val in dic.items():
        if type(val) is int:
            new_dict[prefix + key] = val
        else:
            new_prefix = prefix + key + '.'
            _flatten(val, new_dict, new_prefix)
            # lower_dict = _flatten(val, new_dict, new_prefix)

            # for sub_key, sub_val in 

    print 'new_dict:', new_dict
    return new_dict


sample = {'a': 2,
          'b': 3,
          'c': {'d': 4,
                'e': {'f': 5,
                      'g': 7,
                      }
                }
          }
