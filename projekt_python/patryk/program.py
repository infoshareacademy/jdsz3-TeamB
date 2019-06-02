import pandas as pd

# Dataframe
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition_v2.csv")
df2 = pd.get_dummies(df["Gender"])
df["GenderNumeric"] = df2["Male"]
df2 = pd.get_dummies(df["OverTime"])
df["OverTimeNumeric"] = df2["Yes"]

pd.set_option('display.max_column',30)
pd.set_option('display.max_rows',10)
pd.set_option('display.max_seq_items',None)
pd.set_option('display.max_colwidth', 500)
pd.set_option('expand_frame_repr', True)

import tkinter as tk
from tkinter import font  as tkfont
from tkinter import ttk


class TheProgram(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.title_font = tkfont.Font(family='Helvetica', size=22, weight="bold")
        self.text_font = tkfont.Font(family='Helvetica', size=12, weight="bold")


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Page_2, Page_3):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame


            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="The Program", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label2 = tk.Label(self, text="Choose your destiny", font=controller.text_font)
        label2.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Podgląd tabeli",
                            command=lambda: controller.show_frame("Page_2"))
        button2 = tk.Button(self, text="strona 2",
                            command=lambda: controller.show_frame("Page_3"))
        button1.pack()
        button2.pack()



class Page_2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="randomowy tekst", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        global df

        #text = tk.Text(self, wrap="none")
        #text.insert(tk.END, str(df))
        #text.pack()
        txt_frm = tk.Frame(self, width=600, height=600)
        txt_frm.pack(fill="both", expand=True)
        # ensure a consistent GUI size
        txt_frm.grid_propagate(False)
        # implement stretchability
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)

        # create a Text widget
       # self.txt = tk.Text(txt_frm, borderwidth=3, relief="sunken")
        #self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        #self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        self.txt = tk.Text(txt_frm, wrap="none")
        self.txt.insert(tk.END, str(df))
        self.txt.pack()
        # create a Scrollbar and associate it with txt
        xscrollb = tk.Scrollbar(txt_frm, command=self.txt.yview)
        xscrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = xscrollb.set



        button = tk.Button(self, text="Wstecz",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(side=tk.BOTTOM)

class Page_3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="inny randomowy tekst", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Wstecz",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack(side=tk.BOTTOM)

if __name__ == "__main__":
    app = TheProgram()
    app.mainloop()