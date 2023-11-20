#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
import pysentiment2 as ps

text_1 = "I like this flower."
text_2 = "I hate this flower."
hiv4 = ps.HIV4()
tokens_1 = hiv4.tokenize(text_1)
tokens_2 = hiv4.tokenize(text_2)

score_1 = hiv4.get_score(tokens_1)
score_2 = hiv4.get_score(tokens_2)
print(score_1)
print(score_2)