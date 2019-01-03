# -*- encoding:utf-8 -*-

'''
Interface: KPextCN(text, keyphrasenum=4, stoppath='stopword.txt')
SupportFile: stopword.txt
Fuction: 中文关键短语提取
Algorithm: TextRank
'''

import json
from textrank4zh import TextRank4Keyword

def KPextCN(text, keyphrasenum=4, stoppath='stopword.txt'):
    word = TextRank4Keyword(stop_words_file=stoppath)
    word.analyze(text, window=2, lower=True)
    w_list = word.get_keywords(num=keyphrasenum, word_min_len=2)
    keyphrase = []
    for w in w_list:
        keyphrase.append({"phrase": w['word'], "weight": w['weight']})
    keyphrase = json.dumps(keyphrase, indent=4, ensure_ascii=False)
    return keyphrase





