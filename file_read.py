import os
def read_file(length, file_pos):
    f = open("message.txt", 'r')
    # 密文字数
    target = int(length)
    msg = ""
    # 加密位置
    pos = str(int(file_pos) ** 10)
    # print(pos)
    pos_lst = []

    for i in pos:
        pos_lst.append(int(i))


    # print(pos_lst)
    max_pos = len(pos_lst)

    for i in range(target):
        p = pos_lst[i % max_pos]
        msg += f.readline()[p-1]

    f.close()
    os.remove("message.txt")
    
    return msg
    