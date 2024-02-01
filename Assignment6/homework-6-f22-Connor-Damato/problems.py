import re

from pyparsing import Regex


def problem1(searchstring):
    """
    Match emails.

    :param searchstring: string
    :return: True or False
    """
    pattern1 = re.compile('^([A-Za-z]{1,7}(?=\d{0,4}\@))')
    pattern2 = re.compile('(@jediacademy\.edu)$')
    pattern3 = re.compile('\D\d+\D\@')
    if (pattern1.search(searchstring) and pattern2.search(searchstring) and not pattern3.search(searchstring)):
        return True
    return False


def problem2(searchstring):
    """
    Extract student and ship.

    :param searchstring: string
    :return: tuple
    """
    fullSearch = re.compile('([A-Z][a-z]*\s){1,2}(?=flies the(?= ([A-Z].*-\S+)))')

    if (fullSearch.search(searchstring)):
        both = fullSearch.search(searchstring)
        return (both.group(0).strip(), both.group(2).strip())
    else:
        return ("noname", "noship")

def problem3(searchstring):
    """
    Replace apprentice with title.

    :param searchstring: string
    :return: string
    """
    jedi = re.compile('(?<=[Jj]edi )([Aa]pprentice)')
    sith = re.compile('(?<=[Ss]ith )([Aa]pprentice)')

    if (jedi.search(searchstring)):
        output = jedi.sub('Master', searchstring)
    elif (sith.search(searchstring)):
        output = sith.sub('Darth', searchstring)
    else:
        return ("nomatch")

    return output

if __name__ == "__main__":
    print("To test your code, run the `test_problems.py` file provided.")
