import jieba.posseg as pseg
import json


def tagCN(text):
    words = pseg.cut(text)
    tags = []
    for w in words:
        tags.append({"word": w.word, "tag": str(w.flag)})
    tags = json.dumps(tags, ensure_ascii=False, indent=4)
    return tags
