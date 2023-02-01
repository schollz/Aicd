from collections import *


def train_char_lm(fname, order=4):
    data = open(fname, "r").read()
    lm = defaultdict(Counter)
    pad = "~" * order
    data = pad + data
    for i in range(len(data) - order):
        history, char = data[i : i + order], data[i + order]
        lm[history][char] += 1

    def normalize(counter):
        s = float(sum(counter.values()))
        return [(c, cnt / s) for c, cnt in counter.items()]

    outlm = {hist: normalize(chars) for hist, chars in lm.items()}
    return outlm


from random import random


def generate_letter(lm, history, order):
    history = history[-order:]
    dist = lm[history]
    x = random()
    for c, v in dist:
        x = x - v
        if x <= 0:
            return c


def generate_text(lm, order, nletters=1000):
    history = "~" * order
    out = []
    for i in range(nletters):
        c = generate_letter(lm, history, order)
        history = history[-order:] + c
        out.append(c)
    return "".join(out)


lm = train_char_lm("shakespeare_input.txt", order=7)
print((generate_text(lm, 7)))
