import pandas as pd
import jieba
from nltk.classify import accuracy as nltk_accuracy
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import PlaintextCorpusReader
import random


#引入数据集
data = pd.read_csv("whole.txt",encoding='utf-8',sep='\t',header=None)
data.head()
#对短信内容按照不同的类型（正常短信和垃圾短信）进行分割和分词
spam = data[data[1] == 1].copy()   # 正常短信
spam[2] = spam[2].map(lambda x:' '.join(jieba.cut(x)))
spam.head()

normal = data[data[1] == 0].copy() # 垃圾短信 
normal[2] = normal[2].map(lambda x:' '.join(jieba.cut(x)))
normal.head()

#分别将不同类型分词后的短信保存为不同的文件
spam.to_csv('soam.csv',encoding='utf-8',header=False,index=False,columns=[2])
normal.to_csv('normal.csv',encoding='utf-8',header=False,index=False,columns=[2])

#加载刚刚导出的短信文件
message_corpus = PlaintextCorpusReader('./',['soam.csv','normal.csv'])
all_message = message_corpus.words()

#定义一个特征函数，用于生成特征
def massage_feature(word,num_letter=1):
    return {'feature':word[-num_letter:]}


#对短信特征进行标记提取    
labels_name = ([(massage,'垃圾') for massage in message_corpus.words('soam.csv')]+[(massage,'正常') for massage in message_corpus.words('normal.csv')])
random.seed(7)
random.shuffle(labels_name)  

#训练并预测模型
featuresets = [(massage_feature(n),massage) for (n,massage) in labels_name]
train_set,test_set = featuresets[100000:],featuresets[:100000]
classifier = NaiveBayesClassifier.train(train_set)
print('结果准确率：',str(100*nltk_accuracy(classifier,test_set))+str('%'))