from tkinter import *

import wikipedia as wk

root  = Tk()

def clear():

    my_entry.delete(0,END)
    text.delete(0.0,END)


def search():

    data = wk.page(my_entry.get())

    clear()

    text.insert(4.0,data.content)



root.title('LineByLineCode')

ph = PhotoImage(file='favicon.png')
root.iconphoto(False,ph)
#frame

my_labelFrame = LabelFrame(root, text="Search Wikipedia")
my_labelFrame.pack(pady=20)

#entry box

my_entry = Entry(my_labelFrame,font=("Helvetica",18),width=47)
my_entry.pack(pady=20,padx=20)

#text box frame

my_frame = Frame(root,width=20)
my_frame.pack(pady=4)

#scroll bar

scroll_frame = Scrollbar(my_frame)
scroll_frame.pack(side =RIGHT ,fill= Y)



hor_scroll = Scrollbar(my_frame,orient= 'horizontal')
hor_scroll.pack(side=BOTTOM,fill=X)




#textbox

text = Text(my_frame, yscrollcommand=scroll_frame.set,wrap="none", xscrollcommand=hor_scroll.set)
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")
text.pack()

scroll_frame.config(command=text.yview)
hor_scroll.config(command=text.xview)

#but5tons

btn_frame = Frame(root)
btn_frame.pack(pady=10)

#buttons

search_button = Button(btn_frame,text="Lookup",font=("Helvetica",29),fg="cyan",bg="black",command=search)
search_button.grid(row=0,column=0,padx=20)


clear_button = Button(btn_frame, text="Clear", font=("Helvetica", 29), fg="cyan",bg="black",command=clear)
clear_button.grid(row=0, column=1)

root.mainloop()
