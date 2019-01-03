# -*- encoding:utf-8 -*-

'''
Interface: KPextEN(text, keyphrasenum=4, stoppath="SmartStoplist.txt"))
SupportFile：SmartStoplist.txt   RAKE.py  
Fuction: 英文关键短语提取
Algorithm: RAKE(rapid automatic keyword extraction)
'''

import RAKE
import operator
import json

def KPextEN(text, keyphrasenum=4, stoppath="SmartStoplist.txt"):
    sentenceList = RAKE.split_sentences(text)
    stopwordpattern = RAKE.build_stop_word_regex(stoppath)
    phraseList = RAKE.generate_candidate_keywords(sentenceList, stopwordpattern)    # generate candidate keywords
    wordscores = RAKE.calculate_word_scores(phraseList)    # calculate individual word scores
    keywordcandidates = RAKE.generate_candidate_keyword_scores(phraseList, wordscores)    # generate candidate keyword scores
    sortedKeywords = sorted(keywordcandidates.items(), key=operator.itemgetter(1), reverse=True)
    totalKeywords = len(sortedKeywords)
    keyphrase = []
    for keyword in sortedKeywords[0:keyphrasenum]:
        keyphrase.append({"phrase": keyword[0], "weight": keyword[1]})
    keyphrase = json.dumps(keyphrase, indent=4)
    return keyphrase
