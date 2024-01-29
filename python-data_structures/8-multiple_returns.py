#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        a = sentence[0]
    else:
        a = None
    res = (len(sentence), a)
    return res
