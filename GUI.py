import tkinter
import random

def click_btn():
    button["text"]=random.choice["クリックしました","クリックしました2"]

root=tkinter.Tk()
root.title("初めてのウィンドウ")
root.geometry("800x600")
button=tkinter.Button(root,text="クリックして下さい",font=("System",36),command=click_btn)
button.place(x=200,y=75)
root.mainloop()