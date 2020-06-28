from tkinter import *
from  tkinter import messagebox

class Applicaction(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()


    def createWidget(self):
        self.s1 = StringVar()
        self.input_new = Entry(self, text="123456", textvariable=self.s1)
        self.input_new
        self.input_new.grid(column=0, row=0, columnspan=4)

        # 第二行
        self.btn_11 = Button(self, text="MC")
        self.btn_11.grid(column=0, row=1, sticky="EW")
        self.btn_12 = Button(self, text="M+")
        self.btn_12.grid(column=1, row=1, sticky="EW")
        self.btn_13 = Button(self, text="M-")
        self.btn_13.grid(column=2, row=1, sticky="EW")
        self.btn_14 = Button(self, text="MR")
        self.btn_14.grid(column=3, row=1, sticky="EW")

        # 第三行
        self.btn_21 = Button(self, text="C")
        self.btn_21.grid(column=0, row=2, sticky="EW")
        self.btn_22 = Button(self, text="**")
        self.btn_22.grid(column=1, row=2, sticky="EW")
        self.btn_23 = Button(self, text="/")
        self.btn_23.grid(column=2, row=2, sticky="EW")
        self.btn_24 = Button(self, text="*")
        self.btn_24.grid(column=3, row=2, sticky="EW")

        # 第四行
        self.btn_31 = Button(self, text="7")
        self.btn_31.grid(column=0, row=3, sticky="EW")
        self.btn_32 = Button(self, text="8")
        self.btn_32.grid(column=1, row=3, sticky="EW")
        self.btn_33 = Button(self, text="9")
        self.btn_33.grid(column=2, row=3, sticky="EW")
        self.btn_34 = Button(self, text="-")
        self.btn_34.grid(column=3, row=3, sticky="EW")
