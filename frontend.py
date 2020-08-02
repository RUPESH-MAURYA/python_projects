from tkinter import * 
import backend 

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple =list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def insert_command():
    list1.delete(0,END)
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.insert(END, backend.view()[-1])

def update_command():
    print "up"
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    view_command()


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()


#Create window
window =Tk()
 
window.wm_title("Book Store")

#labels
title =Label(window,text="Title")
title.grid(row=0,column=0)

author =Label(window,text="Author")
author.grid(row=0,column=3)

Year =Label(window,text="Year")
Year.grid(row=1,column=0)

ISBN =Label(window,text="ISBN")
ISBN.grid(row=1,column=3)

#text 
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=4)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=4)
#list
list1 =Listbox(window,height=8,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=3,rowspan=6)

sb2=Scrollbar(window,orient=HORIZONTAL)
sb2.grid(row=9,column=0,columnspan=3)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.configure(xscrollcommand=sb2.set)
sb2.configure(command=list1.xview)

list1.bind("<<ListboxSelect>>",get_selected_row)
#Buttons 
b1=Button(window,text="View all" ,width =12 ,command = view_command)
b1.grid(row=2,column=4)

b2=Button(window,text="Search entry",width =12,command=search_command)
b2.grid(row=3,column=4)

b3=Button(window,text="Add entry",width =12,command=insert_command)
b3.grid(row=4,column=4)

b4=Button(window,text="Update selected",width =12,command=update_command)
b4.grid(row=5,column=4)

b5=Button(window,text="Delete selected",width =12,command=delete_command)
b5.grid(row=6,column=4)

b6=Button(window,text="Close",width =12,command=window.destroy)
b6.grid(row=7,column=4)





window.mainloop()
