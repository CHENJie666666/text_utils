# text_utils
Some useful utils for common text processing

## 1. 文本基本处理





## 2. 语种转换

### 2.1 繁体简体互转

实现单一txt文件或目录下所有txt文件的繁体简体互转

- 安装包

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

使用谷歌翻译API实现多语种翻译功能

- 官方文档

https://py-googletrans.readthedocs.io/en/latest/

- 安装包

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



### 2.3 语种检测

使用谷歌翻译API实现语种检测功能

- 安装包

```shell
pip install googletrans==3.1.0a0 -i https://mirror.baidu.com/pypi/simple/
```

- 检测文本，输出为语种及置信度

```shell
python language_detection.py -t '你好'
```

