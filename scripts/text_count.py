"""
功能：字数统计
    1. 统计特点词语出现的次数及位置
    2. 统计出现最多的N个词语
"""

import jieba
# import nltk  # 第一次统计英文文本出现最多的N个词语时需要执行
# nltk.download('punkt')  # 第一次统计英文文本出现最多的N个词语时需要执行
from nltk.tokenize import word_tokenize
from collections import Counter
from language_detection import detection
import argparse

def argv_parse():
    """
    创建命令行参数解析器
    """
    parser = argparse.ArgumentParser(description="实现英文文本的大小写调节")

    parser.add_argument("-s", "--src_file", type=str, 
                            help="目标文件所在路径")
    parser.add_argument("-d", "--dst_file", type=str, default=None,
                            help="生成文件所在路径")
    parser.add_argument("-w", "--word", type=str,
                            help="待统计词语")
    parser.add_argument("-o", "--output_format", type=str, default='{}出现{}次',
                            help="输出格式")
    parser.add_argument("-n", "--number", type=int, default=1,
                            help="统计的词语数量")
    parser.add_argument("-p", "--list_punctuation", default=False, action='store_true',
                            help="是否输出标点符号")

    args = parser.parse_args()
    return args

def word_count(file, word, output_format='{}出现{}次'):
    """
    统计文本文件中word出现的次数
    :params: file 输入文件所在路径（str类型）
    :params: word 待统计词语（str/list/tuple类型）
    :params: output_format 输出格式，默认为{词语}出现{}次（str类型）
    """ 
    count = {word: 0}
    
    with open(file, 'r', encoding='utf-8') as r:
        while True:
            text = r.read(1024)
            if not text:
                break
            for key, _ in count.items():
                count[key] += text.count(key)
    
    print(output_format.format(word, count[word]))


def list_n_most_common_words(file, n=1, save_file=None, output_format='{}出现{}次', \
    list_punctuation=False):
    """
    列举出中/英文文本文件中出现最多的N个词语/单词
    :params: file 输入文件所在路径（str类型）
    :params: n 统计的词语数量（int类型）
    :params: save_file 保存文件所在路径（str/None类型）
    :params: output_format 输出格式，默认为{词语}出现{}次（str类型）
    :params: list_punctuation 是否输出标点符号（bool类型）
    """ 
    # 语种检测
    punctuation = ['\t', '\n', ' ', '\r', '\v', '\f', '——']
    with open(file, 'r', encoding='utf-8') as r:
        text = r.read(1024)
        if detection(text).lang.lower().startswith('zh'):
            _func = jieba.lcut
            punctuation += ['。', '？', '！', '，', '、', '：', '；', '“', '”', '（', '）', '《', '》', '···', '······']
        elif detection(text).lang.lower().startswith('en'):
            _func = word_tokenize
            punctuation += ['.', '?', '!', ',', ':', ';', '"', '"', '\'', '(', ')', '...', '-', '_']
        else:
            print('不支持该语言')
            return

    # 分词计数
    count = Counter()
    with open(file, 'r', encoding='utf-8') as r:
        while True:
            text = r.read(1024)
            if not text:
                break               
            token = _func(text)
            count += Counter(token)    
    
    # 删除标点符号
    if not list_punctuation:
        for p in punctuation:
            if count[p] != 0:
                count[p] = 0
                del count[p] 
    
    results = count.most_common(n)

    # 输出
    if save_file:
        with open(save_file, 'w', encoding='utf-8') as w:
            for result in results:
                w.write(output_format.format(result[0], str(result[1])))
                w.write('\n') 
        print(f'文件已保存至{save_file}')

    else:
        for result in results:
            print(output_format.format(result[0], str(result[1])))


if __name__ == '__main__':
    
    # # 统计单词出现的次数
    # word_count('temp3.txt', ['how', 'are'], save_file='temp4.txt')

    # # 统计英文文本中出现最多的3个单词
    # list_n_most_common_words('temp3.txt', n=3, lang='en')

    args = argv_parse()
    if args.word:
        word_count(args.src_file, args.word, args.output_format)
    elif args.number:
        list_n_most_common_words(args.src_file, args.number, args.dst_file, args.output_format, args.list_punctuation)


