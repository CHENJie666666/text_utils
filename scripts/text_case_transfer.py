"""
功能：对英文文本大小写进行调节
    1. 全部改为大写
    2. 全部改为小写
    3. 标题化（每个句子句首单词的首字母大写，其余为小写）
    4. 断句换行
"""
import argparse

def argv_parse():
    """
    创建命令行参数解析器
    """
    parser = argparse.ArgumentParser(description="实现英文文本的大小写调节")

    parser.add_argument("-s", "--src_file", type=str, 
                            help="目标文件所在路径")
    parser.add_argument("-d", "--dst_file", type=str,
                            help="生成文件所在路径")
    parser.add_argument("-o", "--option", choices=['u', 'upper', 'l', 'lower', 'c', 'captalize', 'b', 'break'],
                            help="操作选项（大写'u'/'upper'、小写'l'/'lower'、标题化'c'/'capitalize'、断句换行'b'/'break'）")

    args = parser.parse_args()
    return args

def text_case_transfer(src_file, dst_file, option):
    """
    对英文文本的大小写进行转换
    :params: src_file 待处理文件
    :params: dst_file 生成文件 
    :params: option 操作选项（大写、小写、标题化、断句换行）
        'u'/'upper', 'l'/'lower', 'c'/'capitalize', 'b'/'break'
    """
    with open(src_file, 'r', encoding='utf-8') as r:
        text = r.read()
    
    assert text, '文件为空'
    
    if option == 'u' or option == 'upper':
        new_text = text.upper()
    
    elif option == 'l' or option == 'lower':
        new_text = text.lower()
    
    elif option == 'c' or option == 'capitalize':
        new_text = _capitalize(text)
    
    elif option == 'b' or option == 'break':
        new_text = _break(text)
    
    else:
        print(r'请输入正确的 option 参数：u/upper, l/lower, c/capitalize, b/break')
        return

    with open(dst_file, 'w', encoding='utf-8') as w:
        w.write(new_text)
    print(f'文件已保存至{dst_file}')


def _capitalize(text):
    """
    全部改为标题化（句首首字母大写）
    :params: text 待处理文本
    return: new_text 转化后文件
    """
    sentence_list = _get_all_sentence(text)
    new_text = ''
    for s in sentence_list:
        new_text += s.lstrip().capitalize()
    return new_text

def _break(text):
    """
    断句换行
    :params: text 待处理文本
    return: new_text 转化后文件
    """
    sentence_list = _get_all_sentence(text)
    # print(sentence_list)
    new_text = ''
    sep = ['\t', '\n', ' ', '\r', '\v', '\f']
    for s in sentence_list:
        
        while True:
            if s[-1] in sep:
                s = s[:-1]
            else:
                break        
        new_text += s.lstrip()
        new_text += '\n'
    return new_text

def _get_all_sentence(text):
    stop = [':' , '.' , '?' , '!']
    sep = ['\t', '\n', ' ', '\r', '\v', '\f']
    sentence_list = []
    sentence = ''
    flag = False
    
    for i, char in enumerate(text):
        sentence += char
        if char in stop:
            if text[i+1] not in sep:
                sentence_list.append(sentence)
                sentence = ''
            else:
                flag = True
                continue
        if flag:
            sentence_list.append(sentence)
            sentence = ''
            flag = False
    
    return sentence_list


if __name__ == '__main__':

    # # 全部改为大写
    # text_case_transfer('temp.txt', 'temp2.txt', 'u')

    # # 全部改为小写
    # text_case_transfer('temp.txt', 'temp2.txt', 'l')

    # # 全部改为标题化
    # text_case_transfer('temp.txt', 'temp2.txt', 'c')

    # # 断句换行
    # text_case_transfer('temp.txt', 'temp2.txt', 'b')

    args = argv_parse()
    text_case_transfer(args.src_file, args.dst_file, args.option)