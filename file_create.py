import random


def random_write(text_len, lr):
    res = ""
    text_len = int(text_len)
    if lr == 'l':
        text_len = int(text_len-1)
        for i in range(text_len):
            res += random.choice(letters)
    elif lr == 'r':
        text_len = int(text_len/2)
        for i in range(text_len):
            res += random.choice(letters)
    else:
        text_len = int(text_len)
        for i in range(text_len):
            res += random.choice(letters)
    return res

# 乱码字符集
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', ' ']

def create_file(file_text, file_pos):

    a = open("message.txt", 'w')

    # 待加密文字
    text = file_text
    text_len = len(text)
    # 加密位置
    pos = str(int(file_pos) ** 10)
    # print(pos)
    pos_lst = []

    for i in pos:
        pos_lst.append(int(i))


    # print(pos_lst)
    max_pos = len(pos_lst)

    index = 0
    for i in text:
        a.write(random_write(pos_lst[index % max_pos], 'l'))
        a.write(i)
        a.write(random_write(text_len, 'r'))
        a.write('\n')
        index += 1

    add = random.randint(3, 13)
    while add > 0:
        a.write(random_write(pos_lst[add % max_pos], 'l'))
        a.write(random.choice(letters))
        a.write(random_write(text_len, 'r'))
        a.write('\n')
        add -= 1

    a.close()
    
    return text_len, file_pos