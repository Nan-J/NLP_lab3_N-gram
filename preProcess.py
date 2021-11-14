import glob

target_files = glob.glob(pathname='train_Lib/*.txt')
data = []
for file_ in target_files:
    with open(file_, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        data.extend(lines)
with open("all_train.txt", 'w', encoding='utf-8') as f:
    f.writelines(data)


with open("all_train.txt",'r',encoding='utf-8') as f:
    source_text=f.readline()
# 中文标点符号
punctuation = ['–', '—', '‘', '’', '“', '”','|',
               '…', '、', '〈', '〉', '《',
               '》', '「', '」', '『', '』', '【',
               '】', '〔', '〕', '！', '（', '）',
               '，', '．', '：','{','}','‘','“','、']

target_text = [word for word in source_text if word not in punctuation]
s = ''.join(target_text)

with open("all_train_cleaned.txt", 'w', encoding='utf-8') as f:
    f.write(s)