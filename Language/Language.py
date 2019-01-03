#coding=utf-8
import langid                             #引入langid模块


def language(text):
    lang = langid.classify(text)
    lang = list(lang)
    if lang[0] == 'zh':
        lang[0] = 'ch'
    return lang[0]