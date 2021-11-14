import jieba
import re
from zhon.hanzi import punctuation
from _overlapped import NULL
import math


def Modify(s):
    # 将结尾标点符号截掉
    if s[-1] in (r"[%s]+" % punctuation):
        s = s[:-1]  # 截取字符串从开头到倒数一个字符的子串

    # 添加起始符BOS和终止符EOS
    s_modify1 = re.sub(r"[%s]+" % punctuation, "EOSBOS", s)
    s_modify2 = "BOS" + s_modify1 + "EOS"
    return s_modify2
def Partition_Statistics(s, lists, dicts = NULL):
    jieba.suggest_freq(("BOS", "EOS"), True)
    s = jieba.cut(s, HMM = False)  #精确模式，自动计算的词频在使用 HMM 新词发现功能时可能无效,所以设为False
    format_s = ",".join(s)
    #将词按","分割后依次填入数组
    lists = format_s.split(",")
    #统计词频
    if dicts != NULL:
        for word in lists:
            if word not in dicts:
                dicts[word] = 1
            else:
                dicts[word] += 1
    return lists
def CompareList(ori_list,test_list):
    #申请空间
    count_list=[0]*(len(test_list)-1)
    #遍历测试的字符串
    for i in range(0, len(test_list)-1):
        for j in range(0,len(ori_list)-2):
            if test_list[i]==ori_list[j]:
                if test_list[i+1]==ori_list[j+1]:
                    count_list[i]+=1
    return count_list
def Probability(test_list,count_list,ori_dict):
    flag=0
    #概率值为p
    p=1
    for i in range(len(test_list) - 1):
        p *= ((float(count_list[flag] + 1)) / (float(ori_dict[test_list[i]]) + 1))
        flag += 1
    return p


if __name__ == "__main__":
    p_list=[]
    with open('test.txt','r',encoding='utf-8') as f:
        lines=f.readlines()
    for s_test in lines:
        s_test = s_test.strip('\n')
        with open('all_train_cleaned.txt', 'r', encoding='utf-8', ) as f:
            lines = f.readlines()
        s = ''
        for line in lines:
            s = line + s

        ori_list = []
        ori_dict = {}

        # 测试句子
        test_list = []
        count_list = []

        # 分词并将结果存入一个list，词频统计结果存入字典
        s_ori = Modify(s)
        ori_list = Partition_Statistics(s_ori, ori_list, ori_dict)

        s_test = Modify(s_test)
        test_list = Partition_Statistics(s_test, test_list)


        count_list = CompareList(ori_list, test_list)
        p=Probability(test_list, count_list, ori_dict)
        #p=round(p,4)
        print(p)
        p_list.append(math.log(p))

    print(p_list)
