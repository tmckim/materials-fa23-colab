OK_FORMAT = True

test = {   'name': 'q21',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> # Make sure you are examining the values in the column, not the column itself\n>>> import numpy\n>>> total_pay_type != numpy.ndarray\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> 'str' in str(total_pay_type)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> isinstance(total_pay_type, type)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> # Make sure to call the type function on a value in the column\n>>> total_pay_type != int\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
