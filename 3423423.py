# -*- coding: utf-8 -*-
from pyltp  import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer

ldir='AgriKG\\ltp\\cws.model'  #分词模型
dicdir='word'                           #外部字典
text = "贵州财经大学要举办大数据比赛吗？那让欧几里得去问问看吧！其实是在贵阳花溪区吧。"

#中文分词
segmentor = Segmentor()                             #初始化实例
segmentor.load_with_lexicon(ldir, 'word')    #加载模型
words = segmentor.segment(text)                 #分词
print(' '.join(words))                                     #分词拼接
words = list(words)                                      #转换list
print(u"分词:", words)
segmentor.release()
