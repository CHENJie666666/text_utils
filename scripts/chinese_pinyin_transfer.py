"""
功能：实现汉字与拼音的相互转化
"""

import pypinyin
from Pinyin2Hanzi import DefaultDagParams, dag, simplify_pinyin
# import unicodedata


def hanzi_to_pinyin(sentence, with_tone=True):
    """
    将汉语转化为拼音
    :params sentence 待转换句子
    :params with_tone 是否带声调
    return new_sentence 拼音
    """
    new_sentence = ''
    if with_tone:
        for word in pypinyin.pinyin(sentence):
            new_sentence += ''.join(word) + ' '
    else:
        for word in pypinyin.pinyin(sentence, style=pypinyin.NORMAL):
            new_sentence += ''.join(word) + ' '
    return new_sentence


def pinyin_2_hanzi(sentence, k=1):
    """
    将拼音转化为汉字
    :params sentence 待转换句子
    :params k 可能性最高的k个结果
    return new_sentence 汉字
    """
    dagParams = DefaultDagParams()
    # sentence = unicodedata.normalize('NFKD', sentence).encode('ascii','ignore').decode()
    sentence = simplify_pinyin(sentence)
    pinyinList = [i for i in sentence.split(' ') if i != '']

    result = dag(dagParams, pinyinList, path_num=k, log=True)
    new_sentence = ''
    for i, item in enumerate(result):
        _res = item.path # 转换结果
        res = ''.join(_res)
        new_sentence += res
        if i != len(result) - 1:
            new_sentence += '\n'
    
    return new_sentence

if __name__ == '__main__':
    
    # 汉字转拼音
    s = '大家好我是安德鲁'
    print(hanzi_to_pinyin(s))
    
    # 拼音转汉字
    s = 'dà jiā hǎo wǒ shì ān dé lǔ'
    print(pinyin_2_hanzi(s, 5))



"""
参考：
https://github.com/mozillazg/python-pinyin
https://github.com/letiantian/Pinyin2Hanzi
"""
