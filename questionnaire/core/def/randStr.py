import random
import string


def randStr(chars=string.digits + string.digits, N=10):
    str = ''.join(random.choice(chars) for _ in range(N))
    return int(str)