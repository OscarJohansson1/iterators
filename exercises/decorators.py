"""Övningar på decorators."""

from functools import wraps  # NoQA


def memoize(F):
    """Implementera memoization (cache).

    Detta är den enklaste typen av cache som helt enkelt lagrar alla
    returvärden för de anropsvärden som används.
    """
    memo = {}

    @wraps(F)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = F(*args)
            memo[args] = rv
            return rv
    return wrapper


def rovarsprak(F):
    """Översätt utdata till rövarspråket.

    Funktionen som dekoreras kan antas returnera textsträngar. Dessa översätts
    av decoratorn till rövarspråket.
    """
    data = F()
    result = ''
    vocal = 'aeiouyåäö'

    for letter in data:
        if letter.lower() in vocal:
            result = result + letter
        else:
            result = result + letter + 'o' + letter
    return lambda: result


'''
def html(F):
    data = F()
    result = ""

    for word in data.split(' '):
        if word[0] == '_' and word[-1] == '_':
            result.append('<em>' + word[1:-1] + '</em>')
        else:
            result.append(word)

    return lambda: ' '.join(result)

# om inte lambda kan man göra såhär:

#    def R():
#        return result
#
#    return R

@html
def my_fun():
    return 'Fy vilket _dåligt_ spel!!'

if __name__ == "__main__":
    print(my_fun())
'''
