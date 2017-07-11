import re

def solution(s):

    if len(s)%2 != 0:
        s = "{0}{1}".format(s,"_")

    return re.findall('..', s)
