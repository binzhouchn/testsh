#!/usr/bin/env python
# encoding:utf-8
import os
from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
from pyltp import Parser


class MYLTP:
    def __init__(self, ltp_dir):
        self.LTP_DATA_DIR = ltp_dir
        # 分句模型
        self.sentencesplitter = SentenceSplitter
        # 加载分词模型
        self.cws_model_path = os.path.join(self.LTP_DATA_DIR, 'cws.model')
        self.segmentor = Segmentor()
        self.segmentor.load(self.cws_model_path)
        # 加载词性标注模型
        self.pos_model_path = os.path.join(self.LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
        self.postagger = Postagger()  # 初始化实例
        self.postagger.load(self.pos_model_path)  # 加载模型
        # 加载NER模型
        self.ner_model_path = os.path.join(self.LTP_DATA_DIR, 'ner.model')
        self.recognizer = NamedEntityRecognizer()  # 初始化实例
        self.recognizer.load(self.ner_model_path)  # 加载模型
        # 加载依存句法分析模型
        self.par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')
        self.parser = Parser()  # 初始化实例
        self.parser.load(self.par_model_path)  # 加载模型


# 实例化
ltp_dir = '/home/flygan/zhoubin1010/ltp_data_v3.4.0'
myltp = MYLTP(ltp_dir)
