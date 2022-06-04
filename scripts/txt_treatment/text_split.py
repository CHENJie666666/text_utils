"""
功能：按照特定字符对txt文件中每一行进行切分，选取需要内容
"""

def text_split(src_file, dst_file, sep='', number=1):
    """
    单个文件处理
    参数：
    src_file: 源文件路径
    dst_file: 保存文件路径
    sep: 分隔符
    number: 需要保留第几组文本
    """
    with open(src_file, 'r', encoding='utf-8') as r:
        lines = r.readlines()
    
    lines = [line.rsplit('\n', 1)[0] for line in lines if line != '\n']
    
    with open(dst_file, 'w', encoding='utf-8') as w:
        for line in lines:
            text = line.split(sep)[number-1]
            w.write(text)
            w.write('\n')

if __name__ == '__main__':

    # 单个文本处理
    text_split('../../tests/42537条伪原创词库.txt', './test.txt', '→', 2)
