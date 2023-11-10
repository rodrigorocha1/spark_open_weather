try:
    import os
    import sys
    sys.path.insert(0, os.path.abspath(os.curdir))
except:
    pass
from modulo_a.modulo_a import modulo_a


def modulo_b():
    return 'modulo_b'


print(modulo_a())
