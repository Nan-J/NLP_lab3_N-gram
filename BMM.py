word_list = 'wordlist.txt'
file_in = 'test.txt'
file_out = 'text_out_BMM.txt'

# 将字典内容存入list
def get_dic(test_file):
    with open(test_file, 'r', encoding='utf-8', ) as f:
        try:
            file_content = f.read().split()
        finally:
            f.close()
    chars = list(set(file_content))
    return chars


dic = get_dic(word_list)


def readfile(file_in):
    max_length = 5

    h = open(file_out, 'w', encoding='utf-8', )
    with open(file_in, 'r', encoding='utf-8', ) as f:
        lines = f.readlines()

    #正向最大匹配算法
    for line in lines:
        my_stack = []
        len_row = len(line)
        while len_row > 0:
            tryWord = line[-max_length:]
            while tryWord not in dic:
                if len(tryWord) == 1:
                    break
                tryWord = tryWord[1:]
            my_stack.append(tryWord)
            line = line[0:len(line) - len(tryWord)]
            len_row = len(line)

        # 切分的词存入栈
        while len(my_stack):
            t = my_stack.pop()
            #写入文件
            if t == '\n':
                h.write('\n')
            else:
                h.write(t + "  ")

    h.close()


if __name__ == "__main__":
    readfile(file_in)
