'''
HOMEWORK 7 TESTING
'''

# TEST: tokenize()

print(tokenize("  This is an example.  ") == ['This', 'is', 'an', 'example', '.'])
print(tokenize("'Medium-rare,' she said.") == ["'", 'Medium', '-', 'rare', ',', "'", 'she', 'said', '.'])

# TEST: ngrams()

print(ngrams(1, ["a", "b", "c"]) == [((), 'a'), ((), 'b'), ((), 'c'), ((), '<END>')])
print(ngrams(2, ["a", "b", "c"]) == [(('<START>',), 'a'), (('a',), 'b'), (('b',), 'c'), (('c',), '<END>')])
print(ngrams(3, ["a", "b", "c"]) == [(('<START>', '<START>'), 'a'), (('<START>', 'a'), 'b'), (('a', 'b'), 'c'), (('b', 'c'), '<END>')])

### TEST: __init__(), update(), prob()
# test 1
m = NgramModel(1)
m.update("a b c d")
m.update("a b a b")
print(m.prob((), "a") == 0.3)
print(m.prob((), "c") == 0.1)
print(m.prob((), "<END>") == 0.2)

# test 2
m = NgramModel(2)
m.update("a b c d")
m.update("a b a b")
print(m.prob(("<START>",), "a") == 1.0)
print(m.prob(("b",), "c") == 0.3333333333333333)
print(m.prob(("a",), "x") == 0.0)

### TEST: random_token()
# test 1
m = NgramModel(1)
m.update("a b c d")
m.update("a b a b")
random.seed(1)
[m.random_token(()) for i in range(25)] == ['<END>', 'c', 'b', 'a', 'a', 'a', 'b',
                                            'b', '<END>', '<END>', 'c', 'a', 'b',
                                            '<END>', 'a', 'b', 'a', 'd', 'd',
                                            '<END>', '<END>', 'b', 'd', 'a', 'a']

# test 2
m = NgramModel(2)
m.update("a b c d")
m.update("a b a b")
random.seed(2)
print([m.random_token(("<START>",)) for i in range(6)] == ['a', 'a', 'a', 'a', 'a', 'a'])
print([m.random_token(("b",)) for i in range(6)] == ['c', '<END>', 'a', 'a', 'a', '<END>'])

### TEST: random_text()
# test 1
m = NgramModel(1)
m.update("a b c d")
m.update("a b a b")
random.seed(1)
print(m.random_text(13) == '<END> c b a a a b b <END> <END> c a b')

# test 2
m = NgramModel(2)
m.update("a b c d")
m.update("a b a b")
random.seed(2)
print(m.random_text(15) == 'a b <END> a b c d <END> a b a b a b c')

### TEST: create_ngram_model()

m = create_ngram_model(1, "frankenstein.txt")
m.random_text(15)
'beat astonishment brought his for how , door <END> his . pertinacity to I felt'

m = create_ngram_model(2, "frankenstein.txt")
m.random_text(15)
'As the great was extreme during the end of being . <END> Fortunately the sun'

m = create_ngram_model(3, "frankenstein.txt")
m.random_text(15)
'I had so long inhabited . <END> You were thrown , by returning with greater'

m = create_ngram_model(4, "frankenstein.txt")
m.random_text(15)
'We were soon joined by Elizabeth . <END> At these moments I wept bitterly and'

