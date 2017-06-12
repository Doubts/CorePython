from random import randrange, choice
from time import ctime
from string import ascii_lowercase as lc

tlds = ('com', 'edu', 'gov', 'net', 'org')

for i in range(randrange(5, 11)):
    maxsize = 2 ** 32 - 1
    dtint = randrange(maxsize)
    dtstr = ctime(dtint)
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in range(dlen))

    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen))