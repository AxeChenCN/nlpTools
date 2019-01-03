import json
import nltk


def tagEN(text):
    words = nltk.word_tokenize(text)
    tags = nltk.pos_tag(words)
    tagr = []
    for tag in tags:
        tagr.append({"word": tag[0], "tag": tag[1]})
    tag = json.dumps(tagr, indent=4)
    return tag