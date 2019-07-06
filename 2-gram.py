# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 14:39:59 2019

@author: Argust
"""

host = """
host = 寒暄 报数 询问 服务 结尾 
报数 = 您是第 数字 位顾客 ,
数字 = 单个数字 | 数字 单个数字 
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
寒暄 = 称谓 恭祝 
称谓 = 人称 ,
人称 = 先生 | 女士 | 小朋友
恭祝 = 欢迎你  
询问 = 请问你要 | 您需要
服务 = 动作 | 动作1 具体业务
动作 = 点点什么 | 来点什么 
动作1= 点点 | 来点
具体业务 = 红酒 | 啤酒 | 白酒 | 饮料
结尾 = 吗？"""


import random
import pandas as pd
import re
import jieba
from collections import Counter
def create_grammar(grammar_str, split='=', line_split='\n'):
    grammar = {}
    for line in grammar_str.split(line_split):
        if not line.strip(): continue
        exp, stmt = line.split(split)
        grammar[exp.strip()] = [s.split() for s in stmt.split('|')]
    return grammar

def generate(gram,target):
    if target not in gram:return target
    expaned=[generate(gram,t) for t in random.choice(gram[target])]
    return ''.join([e if e !='/n' else '\n' for e in expaned if e !='null'])

example_grammar=create_grammar(host)
    
def generate_n(n):
    for i in range(n):
      print(generate(gram=example_grammar,target='host'))  
    return
n=random.randint(1,100)

filename='C:/Users/Argust/Downloads/movie_comments.csv'
content=pd.read_csv(filename)
articles=content['comment'].tolist()
def token(string):
    return re.findall('\w+',string)
with_jieba_cut=Counter(jieba.cut(str(content)))

articles_clean=[''.join(token(str(a))) for a in articles]
with open('123.txt','w',encoding='utf-8') as f:
    for a in articles_clean:
        f.write(a+'\n')


def cut(string): 
    return list(jieba.cut(string))

TOKEN=[]

for i,line in enumerate((open('123.txt',encoding='utf-8'))):
    TOKEN+=cut(line)
words_count=Counter(TOKEN)
TOKEN=[str(r) for r in TOKEN]
TOKEN_2_GRAM=[''.join(TOKEN[i:i+2]) for i in range(len(TOKEN[:-2]))]
words_count_2=Counter(TOKEN_2_GRAM)

def pro_1(word):
    return words_count[word]/len(TOKEN)

def pro_2(word1,word2):
    if word1+word2 in words_count_2:
        return words_count_2[word1+word2]/len(TOKEN_2_GRAM)
    else:
        return 1/len(TOKEN_2_GRAM)

def get_probablity(host):
    words=cut(host)
    host_pro=1
    for i,word in enumerate(words[:-1]):
        next_=words[i+1]
        probability=pro_2(word,next_)
        host_pro*=probability
    return host_pro

ls=[]
for sen in [generate(gram=example_grammar,target='host') for i in range(n)]:
    ls.append([sen,get_probablity(sen)])

def generate_best():
    a=sorted(ls,key=lambda x:x[1],reverse=True)   
    return a

print(generate_best())



