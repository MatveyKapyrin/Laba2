import tkinter as tk


def add(chislo):
    s = vvod.get()
    if s[0]=='0' and len(s)==1:
        s=s[1:]
    vvod.delete(0, tk.END)
    vvod.insert(0, s+chislo)

def addc (operation):
    s = vvod.get()
    if (s[-1] in '+-/*%√'):
        s=s[:-1]
    elif '+' in s or '-' in s or '/' in s or '*' in s:
        calc()
        s=vvod.get()
    elif '√' in s:
        kor()
        s=vvod.get()
    vvod.delete(0, tk.END)
    vvod.insert(0, s+operation)
def calc():
    s = vvod.get()
    if '%' in s:
        a=s.find('%')
        procent = float(s[:a])
        number = float(s[a+1:])
        result = (number * procent) / 100
        vvod.delete(0, tk.END)
        vvod.insert(0, result)
    else:
        if s[-1] in '+-/*':
            s=s+s[:-1]
        vvod.delete(0, tk.END)
        vvod.insert(0, str(eval(s)))

def kor():
    s = vvod.get()
    vvod.delete(0, tk.END)
    a=eval(s+'**0.5')
    if a*10%10==0:
        vvod.insert(0,int(a))
    else:
        vvod.insert(0, round(eval(s+'**0.5'),3))
def clear():
    vvod.delete(0, tk.END)
    vvod.insert(0,'0')


#вывод чисел
def dbutton(chislo):
    return tk.Button(text=chislo, bd=5, font=('Times New Roman', 15), command=lambda: add(chislo))
#вывод операций
def doperat(operation):
    return tk.Button(text=operation, bd=5, font=('Times New Roman', 15), command=lambda: addc(operation))
#вывод =
def chet(operation):
    return tk.Button(text=operation, bd=5, font=('Times New Roman', 15), command=calc)

def koren(operation):
    return tk.Button(text=operation, bd=5, font=('Times New Roman', 15), command=kor)
def clearB(operation):
    return tk.Button(text=operation, bd=5, font=('Times New Roman', 15), command=clear)

root = tk.Tk()

root.title("Калькулятор")
root.geometry("320x350")
root['bg'] = 'black'
vvod = tk.Entry(root, justify=tk.RIGHT, font=('Times New Roman', 18), width=20)
vvod.insert(0,'0')
vvod.grid(row=0, column=0, columnspan=3, stick='we',padx=5)
dbutton('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
dbutton('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
dbutton('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
dbutton('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
dbutton('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
dbutton('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
dbutton('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
dbutton('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
dbutton('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
dbutton('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

clearB('C').grid(row=0, column=3, stick='wens', padx=5, pady=5)
doperat('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
doperat('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
doperat('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
doperat('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)
doperat('%').grid(row=4, column=1, stick='wens', padx=5, pady=5)
koren('√').grid(row=4, column=2, stick='wens', padx=5, pady=5)
chet('=').grid(row=5, column=0, stick='wens', columnspan=4,padx=5, pady=5)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)

root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)
root.resizable(width=False, height=False)
root.mainloop()
