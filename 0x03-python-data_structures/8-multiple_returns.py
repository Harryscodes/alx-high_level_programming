#!/usr/bin/python3

def multiple_returns(sentence):
    """ function that returns multiple element """

    firstchar = sentence[0] if len(sentence) > 0 else None
    return len(sentence), firstchar
