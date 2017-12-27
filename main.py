import os 
import os.path as op

import sys
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

import datastore 

class Window (ttk.Frame):

    def __init__(self, master=None):
        # とりあえず親のinit
        super().__init__(master, padding=2)
        
        # tk用変数
        self.testVal = tk.StringVar()
　　　　
        # combobox 作成
 　       # widget(コンボボックス)作成　ここでself与えてるからたぶん親との紐づけは済んでいる
        self.testCombobox = ttk.Combobox(self,textvariable=self.testVal)

　        #layout 設定
        self.testCombobox.grid(row=0,column=0,sticky=(tk.W, tk.E), padx="0.5m", pady="0.5m")
          #追加でいりそうなので念のため
        self.testCombobox.state(("readonly",))
        self.testCombobox.config(values="HOGE")
        self.testCombobox.current(0)

        # TreeView設定
        self.testTreeview = ttk.Treeview(self)
        self.testTreeview["columns"]=("Type","Discription","Example")

        self.testTreeview.column("Type", width=40 ,stretch=True)
        self.testTreeview.column("Discription", width=100,stretch=True)
        self.testTreeview.column("Example", width=100,stretch=True)
        self.testTreeview.heading("Type", text="type")
        self.testTreeview.heading("Discription",text="discription")
        self.testTreeview.heading("Example", text="Example ")
       
        self.testTreeview.insert("" , 0,    text="Line 1", values=("1A","1b","3sfasdfasdfasdfasdfasfsdfsafs"))
        self.testTreeview.insert("" , 0,    text="Line 1", values=("1A","1b","3sfasdfasdfasdfasdfasfsdfsafs"))
        self.testTreeview.insert("" , 0,    text="Line 1", values=("1A","1b","3sfasdfasdfasdfasdfasfsdfsafs"))
        self.testTreeview.grid(row=1,column=0,sticky=(tk.N, tk.S, tk.E, tk.W), padx="0.5m", pady="0.5m")


        # gridの設定
        self.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W),) # ←　これだった。



        # windowリサイズ対応
        tk.Grid.rowconfigure(master, 0, weight=1)
        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)
        
        # たぶんwindow最小設定
        master.minsize(150, 40)

        master.title("Window")       
        # スケールの変更
        master.call('tk', 'scaling', 2.0)
        
        # styleの設定　グローバルっぽい
        style = ttk.Style()
        style.configure("Treeview",font=("Meiryo UI",9))

        # 開始
        master.mainloop()


def main():
    if sys.stdout.isatty():
    
        app = tk.Tk()
        Window(app)
        
if __name__ == '__main__':
    main()