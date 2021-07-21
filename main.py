from tkinter import *

root = Tk()

class Calc:
    btns_text = (
        ('AC', 'AC', 'C', 'C'),
        ('7', '8', '9', '/'),
        ('4', '5', '6', '*'),
        ('1', '2', '3', '-'),
        ('0', '.', '+', '=')
    )
    def __init__(self, root):
        # self.string = []
        self.txt = '0'
        self.root = root
        self.root.title('calculator')
        self.root.geometry("360x400")
        self.e = Entry(
            self.root,
            # state = DISABLED,
        )
        self.e.grid(row = 0, column = 0, columnspan = 4)
        for i_i, i_item in enumerate(self.btns_text):
            for j_i, j_item in enumerate(i_item):
                # print(j_item)
                temp_btn = Button(
                    self.root,
                    text = j_item,
                    padx = '10',
                    pady = '3',
                    font = '16',
                    )
                temp_btn.config(command = lambda btn = temp_btn:self.getValue(btn))
                temp_btn.grid(row = i_i+1, column=j_i)

    def __del__(self):
        print('DESTRUCTOR')

    def loop(self):
        self.root.mainloop()

    def getValue(self, btn=None):
        s = btn['text']
        if s == '=':
            self.equal_btn()
        elif s == 'AC':
            self.txt = ''
            self.e.delete(0, END)
            self.txt = '0'
            self.e.insert(0, self.txt)
        elif s == 'C':
            self.txt = self.txt[:-1]
            self.e.delete(0, END)
            self.e.insert(0, self.txt)
        else:
            self.txt += s
            self.e.delete(0, END)
            self.e.insert(0, self.txt)
        # if s.isdigit() or s == '.':
        #     if self.string == []:
        #         self.string.append(s)
        #     else:
        #         self.string[-1] += s
        # else:
        #     self.string.append(s)
        #     self.string.append('')
        # print(self.string)

    def equal_btn(self):
        if self.txt != '':
            self.txt = str(eval(self.txt))
            self.e.delete(0,END)
            self.e.insert(0, self.txt)

calc = Calc(root)
calc.loop()

"""
TODO: fix issues: 
1. when user press C btn few times and text entirely deleted, put '0'
2. if user want to start calculate after equal btn(after result has gotten) put pressed digit, 
else if pressed operand - continue calculating with this result
3. save last Entry string in file and load this in constructor
"""