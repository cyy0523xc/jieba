from __future__ import absolute_import
from .tfidf import TFIDF
from .textrank import TextRank

"""
# import but not used!
try:
    from .analyzer import ChineseAnalyzer
except ImportError:
    pass
"""

default_tfidf = TFIDF()
default_textrank = TextRank()

extract_tags = tfidf = default_tfidf.extract_tags
set_idf_path = default_tfidf.set_idf_path
textrank = default_textrank.extract_tags

# 设置分隔符
set_idf_seperator = default_tfidf.set_idf_seperator


def set_stop_words(stop_words_path):
    default_tfidf.set_stop_words(stop_words_path)
    default_textrank.set_stop_words(stop_words_path)
