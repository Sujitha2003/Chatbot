from cProfile import label
from tkinter import *
import tkinter

root=Tk()
root.title("chatbot")
root.geometry('400x500')

Logopic = PhotoImage(file='bot.png')
LogopicLabel = Label(root,image= Logopic,bg='white')
LogopicLabel.pack()



file_menu=Menu(root)
file_menu.add_command(label='New...')
file_menu.add_command(label='Save as...')
file_menu.add_command(label='exit...')
main_menu=Menu(root)
main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_command(label='Edit')
main_menu.add_command(label='Quit')
root.config(menu=main_menu)
def button():
   button ="You:" +messagewin.get()
   chatwin.insert(END,"\n"+button)
   if(messagewin.get()=="hi" or messagewin.get()=="hello"):
    chatwin.insert(END,"\n"+"Bot:Hi,Nice to meet you")
   elif(messagewin.get()=="how are you?" ):
    chatwin.insert(END,"\n"+"Bot:Fine and you")
   elif(messagewin.get()=="fine" ):
    chatwin.insert(END,"\n"+"Bot:Nice to hear")
   elif(messagewin.get()=="" or messagewin.get()=="hello"):
    chatwin.insert(END,"\n"+"Bot:Hi,Nice to meet you")
   elif(messagewin.get()=="" or messagewin.get()=="what about this app spell checker?"):
    chatwin.insert(END,"\n"+"Bot:This app is created in motto to correct the wrong spelling.\nMaking spelling mistake is normal everyone one of us did it atleast a time.To rectify this owner created a this app.In home there is button 'click me'so  by clicking that you enter to a new page where you can input a wrong text and get corrected")
   else:
    chatwin.insert(END,"\n"+"Bot:Sorry I didn't get you")
   messagewin.delete(0,END)

chatwin=Text(root,bd=1,background="pink",width=50,height=8)
chatwin.place(x=6,y=6,width=370,height=385)
messagewin=Text(root,foreground='white',width=30,height=4)
messagewin=Entry(root)
messagewin.place(x=128,y=400,width=260,height=88)
button=Button(root,text='SEND',background="skyblue",command=button,width=12,height=5,font=('Arial',18))
button.place(x=6,y=400,height=88,width=120)

scroll_bar=Scrollbar(chatwin)

scroll_bar.place(relheight=1,relx=0.974)






root.mainloop()