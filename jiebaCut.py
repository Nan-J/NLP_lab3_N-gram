import jieba

test_file = 'test_line.txt'  # 测试语料
test_file3 = 'text_out_jieba.txt'  # 生成结果

with open(test_file, 'r', encoding='utf-8') as f:
    m=[]
    for line in f:
        seg = jieba.cut(line.strip().encode('utf-8'))
        s = ' '.join(seg)
        m.append(s)
    with open(test_file3, 'w') as f:
        for word in m:
            if word=='\n':
                f.write('\n')
            else:
                f.write(word)
