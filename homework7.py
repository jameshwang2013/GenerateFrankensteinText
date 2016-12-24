############################################################
# CIS 521: Homework 7
############################################################

student_name = "James Wang"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import string
from collections import defaultdict
import random


############################################################
# Section 1: Markov Models
############################################################

def tokenize(text):
    strip = text.strip()
    split = strip.split()
    lst = []
    for i in split:
        for j in i:
            if j in string.punctuation:
                lst.append(" {} ".format(j))

            else:
                lst.append(j)
        lst.append(" ")
    return "".join(lst).split()


def ngrams(n, tokens):
    tokens = tokens + ["<END>"]
    ngrams = ["<START>"] * (n - 1) + tokens
    lst = []
    start = 0
    end = n - 1
    for i in tokens:
        lst.append((tuple(ngrams[start:end]), i))
        start += 1
        end += 1
    return lst


class NgramModel(object):

    def __init__(self, n):
        self.n = n
        self.tokens_by_context = defaultdict(int)
        self.contexts = defaultdict(int)
        self.cdfs = defaultdict(dict)

    def update(self, sentence):
        tokens = tokenize(sentence)
        n_grams = ngrams(self.n, tokens)
        for i in n_grams:
            self.tokens_by_context[i] += 1
            self.contexts[i[0]] += 1

    def prob(self, context, token):
        numer = float(self.tokens_by_context[(context, token)])
        denom = float(self.contexts[context])
        return numer / denom

    def random_token(self, context):
        r = random.random()
        if context not in self.cdfs:
            prev = 0
            build_cdf = defaultdict(float)
            for i in sorted(self.tokens_by_context.keys()):
                if i[0] == context:
                    numer = float(self.tokens_by_context[i])
                    denom = float(self.contexts[i[0]])
                    build_cdf[i[1]] = prev + (numer / denom)
                    prev = build_cdf[i[1]]
            self.cdfs[context] = build_cdf
        cdf = self.cdfs[context]
        lst = sorted(cdf.items())
        before = sum(lst[:0])
        for i in range(len(lst)):
            if lst[i][1] > r and r >= before:
                return lst[i][0]
            before = lst[i][1]

    def random_text(self, token_count):
        context = ("<START>",) * (self.n - 1)
        if self.n == 1:
            print([self.random_token(()) for i in range(token_count)])
            return " ".join([self.random_token(())
                             for i in range(token_count)])
        else:
            lst = []
            for i in range(token_count):
                w = self.random_token(context)
                if w == "<END>":
                    context = ("<START>",) * (self.n - 1)
                    next
                lst.append(w)
                context = tuple(list(context)[1:] + [w])
            print(lst)
            return " ".join(lst)

    def perplexity(self, sentence):
        pass


def create_ngram_model(n, path):
    f = open(path)
    txt = f.read()
    lst = txt.splitlines()
    m = NgramModel(n)
    [m.update(i) for i in lst]
    return m

############################################################
# Section 2: Feedback
############################################################

feedback_question_1 = """
12 hours
"""

feedback_question_2 = """
The programming was hard to conceptualize
"""

feedback_question_3 = """
I liked the real world application of generating text
"""
