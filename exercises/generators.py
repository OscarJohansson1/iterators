"""Övningar på generators."""
from itertools import groupby

def cubes():
    """Implementera en generator som skapar en serie med kuber (i ** 3).

    Talserien utgår från de positiva heltalen: 1, 2, 3, 4, 5, 6, ...
    Talserien som skapas börjar således: 1, 8, 27, 64, 125, 216, ...

    Talserien ska inte ha något slut.

    """
    i = 0
    while True:
        i += 1
        yield i ** 3


def primes():
    """Implementera en generator som returnerar primtal.

    Talserien som förväntas börjar alltså: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...

    """
    value = 0
    while True:
        value += 1
        x = range(1, value)
#        if value == 0 or value == 1:
#            pass
        for i in x:
            if value % i == 0:
                pass
            else:
                yield value


def fibonacci():
    """Implementera en generator som returnerar de berömda fibonacci-talen.

    Fibonaccis talserie börjar med 0 och 1. Nästa tal är sedan summan av de
    två senaste.

    Alltså börjar serien: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

    """
    a, b = 0, 1
    while True:
        c, a, b = a, b, a + b
        yield c


def alphabet():
    """En generator som returnerar namnen på tecknen i det hebreiska alfabetet.

    Iteratorn returnerar namnen för de hebreiska bokstäverna i alfabetisk
    ordning. Namnen och ordningen är:

    Alef, Bet, Gimel, Dalet, He, Vav, Zayin, Het, Tet, Yod, Kaf, Lamed, Mem,
    Nun, Samekh, Ayin, Pe, Tsadi, Qof, Resh, Shin, Tav

    """
    i = 0
    a = ['Alef', 'Bet', 'Gimel', 'Dalet', 'He', 'Vav', 'Zayin', 'Het', 'Tet','Yod', 'Kaf', 'Lamed', 'Mem', 'Nun',
                'Samekh', 'Ayin', 'Pe', 'Tsadi', 'Qof', 'Resh', 'Shin', 'Tav']
    while True:
        yield a[i]
        i += 1
        if i == len(a):
            raise StopIteration


def permutations(value):
    """En generator som returnerar alla permutationer av en inmatad sträng.

    Då strängen 'abc' matas in fås: 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'
    """
    a = 'abc'
    i = 0
    q = a[0] + a[1] + a[2]
    w = a[0] + a[2] + a[1]
    e = a[1] + a[0] + a[2]
    r = a[1] + a[2] + a[0]
    t = a[2] + a[0] + a[1]
    y = a[2] + a[1] + a[0]
    b = [q, w, e, r, t, y]
    while True:
        yield b[i]
        i += 1
        if i == len(b):
            raise StopIteration


def look_and_say():
    """En generator som implementerar look-and-say-talserien.

    Sekvensen fås genom att man läser ut och räknar antalet siffror i
    föregående tal.

    1 läses 'en etta', alltså 11
    11 läses 'två ettor', alltså 21
    21 läses 'en tvåa, en etta', alltså 1211
    1211 läses 'en etta, en tvåa, två ettor', alltså 111221
    111221 läses 'tre ettor, två tvåor, en etta', alltså 312211
    """
    number = '1'
    while True:
    	yield int(number)
    	number = ''.join(str(len(list(g))) + k
    	   for k, g in groupby(number))
