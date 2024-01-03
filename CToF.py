
import tkinter as tk 


wn = tk.Tk()


wn.config(background='white')



class object:

    def __init__(self,master):
        self.master = master
        self.entry1 = self.entry(0,1)
        self.entry2 = self.entry(1,1)
        

    def showresults(self,event=None):
        if self.entry2.get() == '' or self.entry2.get() == ' ':
            expressionF = float(self.entry1.get())/(5/9)+32
            
            self.entry2.insert(True,expressionF)
            self.entry1.delete(0,tk.END)

        elif self.entry1.get() == '' or self.entry1.get() == ' ':
            expressionC = (float(self.entry2.get())-32) * 5/9
            self.entry1.delete(0,tk.END)
            self.entry1.insert(True,expressionC)
            self.entry2.delete(0,tk.END)
    
    def button(self,image):
        tk.Button(self.master,image=image,font=20,command=self.showresults).grid(columnspan=1)

    def label(self,text,row,colomn):
        tk.Label(self.master,text=text,font=('Arial',20)).grid(row=row,column=colomn)

    def entry(self,row,colomn):
        e = tk.Entry(self.master,width=20,font=20)
        e.grid(row=row,column=colomn)
        return e
submitImg = tk.PhotoImage(file = '/Users/uptri/Documents/Pics/png files/Unknown.png')
frame = tk.Frame(wn)
frame.place(x=100,y=0)
Object=object(frame)




wn.geometry('550x200')
wn.title('Temp converter')

label = Object.label('C: ',0,0)
label = Object.label('F: ',1,0)



button_submit = Object.button(submitImg)

wn.mainloop()





