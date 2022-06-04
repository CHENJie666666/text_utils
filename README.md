# text_utils
Some useful utils for common text processing

## 1. 文本基本处理

### 1.1 英文文本大小写转换

#### 功能

对英文文本大小写进行调节

- 全部改为大写

- 全部改为小写

- 标题化（每个句子句首单词的首字母大写，其余为小写）

- 断句换行

#### 使用

```shell
# 全部改为大写
python text_case_transfer.py -s 'temp.txt' -d 'temp2.txt' -o 'u'

# 全部改为小写
python text_case_transfer.py -s 'temp.txt' -d 'temp2.txt' -o 'l'

# 全部改为标题化
python text_case_transfer.py -s 'temp.txt' -d 'temp2.txt' -o 'c'

# 断句换行
python text_case_transfer.py -s 'temp.txt' -d 'temp2.txt' -o 'b'
```

### 1.2 词频统计

#### 功能

字数统计

- 统计特点词语出现的次数
- 统计出现最多的N个词语

#### 使用

- 安装依赖库

```shell
pip install jieba  # 统计中文词频
pip install nltk  # 统计英文词频
```

统计出现最多的N个词语功能依赖`language_detection.py`脚本，确保`text_count.py`脚本与其在同一目录下

- 第一次统计英文文本出现最多的N个词语时需要在`text_count.py`脚本中执行如下语句

```python
import nltk
nltk.download('punkt')
```

- 使用

```shell
# 统计单词'how'出现的次数
python text_count.py -s 'temp.txt' -w 'how'
# 统计出现最多的3个词语
python text_count.py -s 'temp.txt' -n 3
```

#### 参考资料

[8.3. collections — High-performance container datatypes — Python 2.7.18 documentation](https://docs.python.org/2/library/collections.html#counter-objects)

[fxsjy/jieba: 结巴中文分词 (github.com)](https://github.com/fxsjy/jieba)

[nltk/nltk: NLTK Source (github.com)](https://github.com/nltk/nltk)





## 2. 语种转换

### 2.1 繁体简体互转

#### 功能

实现单一txt文件或目录下所有txt文件的繁体简体互转

- 繁体转简体
- 简体转繁体

#### 使用

- 安装依赖库

```shell
pip install zhconv
```

- 繁体转简体：调用`simp_and_trad_zh_trans.py`文件

```shell
python simp_and_trad_zh_trans.py './a.txt'
```

- 简体转繁体：调用`simp_and_trad_zh_trans.py`文件

```shell
python simp_and_trad_zh_trans.py './a.txt' -r
```

- 多txt同时转换：调用`simp_and_trad_zh_trans.py`文件

```
python simp_and_trad_zh_trans.py './txt_dir'
```



### 2.2 谷歌翻译

#### 功能

使用谷歌翻译API实现多语种翻译功能

#### 使用

- 安装依赖库

```shell
pip install googletrans==3.1.0a0 -i https://mirror.baidu.com/pypi/simple/
```

- 直接翻译文本（默认语种为英语）

```shell
python google_translation.py -t '你好' -d 'fr'
```

- 翻译txt文件

```shell
python simp_and_trad_zh_trans.py -t './a.txt'
```

#### 参考资料

谷歌翻译API官方文档：https://py-googletrans.readthedocs.io/en/latest/



### 2.3 语种检测

#### 功能

使用谷歌翻译API实现语种检测功能

#### 使用

- 安装依赖库

```shell
pip install googletrans==3.1.0a0 -i https://mirror.baidu.com/pypi/simple/
```

- 检测文本，输出为语种及置信度

```shell
python language_detection.py -t '你好'
```

#### 参考资料

谷歌翻译API官方文档：https://py-googletrans.readthedocs.io/en/latest/
