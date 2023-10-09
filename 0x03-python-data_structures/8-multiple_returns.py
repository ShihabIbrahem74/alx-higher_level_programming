#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    leng = len(sentence)
    new_tu = (leng, sentence[0])
    return new_tu
