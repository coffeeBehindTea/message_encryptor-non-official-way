from tkinter import *
from tkinter import Button, ttk
import tkinter
from tkinter import messagebox
import sv_ttk

import os
import easygui

import file_read as fr
import file_create as fc

SCREEN_WIDTH = 450
SCREEN_HEIGHT = 500


root = tkinter.Tk()
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}+350+200")
root.resizable(0, 0)

# magic happence
sv_ttk.use_dark_theme()

#! 开关灯按钮
theme_change_button = ttk.Button(
    root, text="change theme", command=sv_ttk.toggle_theme)
theme_change_button.place(x=SCREEN_WIDTH-5, y=10, anchor='ne')
# theme_change_button.pack()


#! 加密文字输入部分
input_text = tkinter.Text(root, width=40, height=10)
input_text.insert("0.0", "在这里输入待加密的内容")
input_text.pack(anchor='nw', padx=10, pady=10)

#! 加密种子输入框
pos_label = ttk.Label(root, text="加密种子（不要太大）")
pos_label.pack(side= LEFT, anchor= "nw", padx=10)

file_pos = ttk.Entry(root)
file_pos.place(x=10, y=240, anchor='w')


#! 生成加密文件
def create():
    #! 获取输入栏的输入
    pos = file_pos.get()
    txt = input_text.get("0.0","end")
    if pos and txt:
        #! 生成加密文件
        length, pos = fc.create_file(txt, pos)
        #! 清除输入栏
        input_text.delete("0.0", "end")
        file_pos.delete(0,"end")
        #! 解密信息提示
        messagebox.showinfo("必要的解密信息", f"length:\n{length}\npos:\n{pos}")
    else:
        messagebox.showwarning("警告", "加密内容和种子都是必须的")

def read():
    if os.path.exists("message.txt"):
        #! 获取解密信息
        msg = "解密请提供一下信息"
        title = "请输入信息"
        inputs_need = ["length","解密种子"]
        inputs = []
        inputs = easygui.multenterbox(msg, title, inputs_need)
        #! 解密并显示
        result = fr.read_file(inputs[0], inputs[1])
        easygui.textbox("解密内容为", "解密内容", result)
    else:
        messagebox.showwarning("警告", "没有发现目标文件")
    

#! 加密按钮
create_button = ttk.Button(root, text="加密", command=create)
create_button.place(x=205, y=240, anchor='center')

#! 解密按钮
read_button = ttk.Button(root, text="解密", command=read)
read_button.place(x=270, y=240, anchor='center')

#! 显示窗口，开始循环
root.mainloop()
