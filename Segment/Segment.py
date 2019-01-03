import jieba
import json


def segment(text):
    text_seg = jieba.cut(text)
    seg = []
    for word in text_seg:
        seg.append({"word": word})
    seg = json.dumps(seg, indent=4, ensure_ascii=False)
    return seg

