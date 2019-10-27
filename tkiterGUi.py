from tkinter import Tk, StringVar, ttk, messagebox
from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Button
from tkinter import *
import time
import datetime

root = Tk()
root.geometry('800x400+0+0')
root.title("Converter Currency")
root.configure(background='black')

LeftMainFrame = Frame(root, width=1000, height=600, bd=8, relief="raise")
LeftMainFrame.pack(side=LEFT)
RightMainFrame = Frame(root, width=800, height=600, bd=8, relief="raise")
RightMainFrame.pack(side=RIGHT)

DateOfOrder = StringVar()
value0 = StringVar()
convert = DoubleVar()
currency = DoubleVar()

def ConCurrency():
    if value0.get()=="USA":
        convert1= float(convert.get()*0.012)
        convert2="USA DOLLERS", str('%.2f' %(convert1))
        currency.set(convert2)

    elif value0.get()=="India":
         convert1= float(convert.get()* 0.84)
         convert2="Rupee", str('%.2f' %(convert1))
         currency.set(convert2)

    elif value0.get() == "British":
        convert1 = float(convert.get() * 0.0095)
        convert2 = "Pound", str('%.2f' % (convert1))
        currency.set(convert2)

    elif value0.get() == "Canada":
        convert1 = float(convert.get()*0.016)
        convert2 = "Dollar", str('%.2f' %(convert1))
        currency.set(convert2)

    elif value0.get() == "Singapore":
        convert1 = float(convert.get()* 0.016)
        convert2 = "Singapore Dollar", str('%.2f' %(convert1))
        currency.set(convert2)

    elif value0.get() == "Kuwait":
        convert1 = float(convert.get()*0.0036)
        convert2 = "Dinar", str('%.2f' %(convert1))
        currency.set(convert2)

    elif value0.get() == "AUS":
        convert1 = float(convert.get() * 0.017)
        convert2 = "Dollar", str('%.2f' %(convert1))
        currency.set(convert2)

    elif value0.get() == "Euro":
        convert1 = float(convert.get() * 0.011)
        convert2 = "Dollar", str('%.2f' %(convert1))
        currency.set(convert2)

#Function exit reset

def qExit():
    qExit = messagebox.askyesno("Do You Want to Quit?")
    if qExit > 0:
        root.destroy()
        return
def Reset():
    value0.set("")
    convert.set("0.0")
    currency.set("0.0")
#Date
DateOfOrder.set(time.strftime("%d/%m/%y"))

EntCurrency = Entry(LeftMainFrame, font=('arial', 10, 'bold'), textvariable=convert, bd=2, width=28, justify='center')
EntCurrency.grid(row=0, column=1)

lblBritishPound = Label(LeftMainFrame, font=('arial',10,'bold'),
                        text='BDT', padx=2, pady=2, bd=2, fg='black', width=18)
lblBritishPound.grid(row=0, column=2, sticky=W)

box = ttk.Combobox(LeftMainFrame, textvariable=value0, state='readonly', font=('arial', 10, 'bold'), width=20)
box['values'] = ('', 'Kuwait','Canada','Euro', 'India', 'British', 'Singapore','AUS','USA')
box.current(0)
box.grid(row=4, column=2)

lblCurrency = Label(LeftMainFrame, font=('arial', 10, 'bold'), textvariable=currency,
                  bd=2, width=25, bg='white', padx=2, pady=2, relief='sunken')
lblCurrency.grid(row=4, column=1)


lblDateOfOrder = Label(RightMainFrame,font=('arial', 10, 'bold'), padx=2, pady=2, bd=2,
                     textvariable=DateOfOrder, fg='black', width=12, justify='center')
lblDateOfOrder.grid(row=2, column=0, sticky=W)

btnConvert = Button(RightMainFrame, text='Convert', padx=2, pady=2, bd=2,fg='black',
                    font=('arial', 10, 'bold'), width=18, height=1, command=ConCurrency).grid(row=3, column=0)
btnReset = Button(RightMainFrame, text='Reset', padx=2, pady=2, bd=2, fg='black',
                    font=('arial', 10, 'bold'), width=18, height=1, command=Reset).grid(row=4, column=0)
btnExit = Button(RightMainFrame, text='Exit', padx=2, pady=2, bd=2, fg='black',
                    font=('arial', 10, 'bold'), width=18, height=1, command=qExit).grid(row=5, column=0)

root.mainloop()
