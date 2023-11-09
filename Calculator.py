import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    Entry_Box.delete(0, "end")
    Entry_Box.insert(0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        Entry_Box.delete(0, "end")
        Entry_Box.insert(0, calculation)
        
    except:
        clear_field()
        Entry_Box.insert(0, "Error")
        
def funcBackspace():
    global calculation
    calculation = ""
    length = len(Entry_Box.get())
    Entry_Box.delete(length-1, "end")
    if length==1:
        Entry_Box.insert(0,"0")
    
def clear_field():
    global calculation
    calculation = ""
    length = len(Entry_Box.get())
    Entry_Box.delete(0, "end")
    if length==0:
        Entry_Box.insert(0,"0")

root = tk.Tk()
root.geometry("379x424")
root.resizable(False, False)
root.title("Calculator")

Entry_Box = tk.Entry( width=17, bg="black", fg="white", font=("Roboto", 24), justify='right')
Entry_Box.insert(0, "0")
Entry_Box.grid(columnspan=5)

btn_clear = tk.Button(root, text="C", command=clear_field , width=7, height=2, font="Roboto 14 bold", bg="grey", fg="white")
btn_clear.place(x=0, y=50)
btn_mod = tk.Button(root, text="%", command=lambda: add_to_calculation("%"), width=7, height=2, font="Roboto 15 bold", bg="grey", fg="white")
btn_mod.place(x=90, y=50)
btn_backspace = tk.Button(root, text="←", width=7, height=2, command= funcBackspace,font="Roboto 14 bold", bg="grey", fg="white")
btn_backspace.place(x=180, y=50)

btn_1 = tk.Button(root, text="1", relief='groove', command=lambda: add_to_calculation(1), width=7, height=2, font="Roboto 14 bold", bg="black", fg="white")
btn_1.place(x=0, y=275)
btn_2 = tk.Button(root, text="2",relief='groove', command=lambda: add_to_calculation(2), width=7, height=2, font="Roboto 14 bold", bg="black", fg="white")
btn_2.place(x=90, y=275)
btn_3 = tk.Button(root, text="3",relief='groove', command=lambda: add_to_calculation(3), width=7, height=2, font="Roboto 14 bold", bg="black", fg="white")
btn_3.place(x=180, y=275)
btn_4 = tk.Button(root, text="4",relief='groove', command=lambda: add_to_calculation(4), width=7, height=2, font="Roboto 14 bold", bg="black", fg="white")
btn_4.place(x=0, y=200)
btn_5 = tk.Button(root, text="5", relief='groove',command=lambda: add_to_calculation(5), width=7, height=2, font="Roboto 14 bold", bg="black", fg="white")
btn_5.place(x=90, y=200)
btn_6 = tk.Button(root, text="6",relief='groove', command=lambda: add_to_calculation(6), width=7, height=2, font="Roboto 14 bold", bg="black", fg="white")
btn_6.place(x=180, y=200)
btn_7 = tk.Button(root, text="7",relief='groove', command=lambda: add_to_calculation(7), width=7, height=2, font="Roboto 14 bold", bg="black", fg="white")
btn_7.place(x=0, y=125)
btn_8 = tk.Button(root, text="8",relief='groove', command=lambda: add_to_calculation(8), width=7, height=2, font="Roboto 14 bold", bg="black", fg="white")
btn_8.place(x=90, y=125)
btn_9 = tk.Button(root, text="9",relief='groove', command=lambda: add_to_calculation(9), width=7, height=2, font="Roboto 14 bold", bg="black", fg="white")
btn_9.place(x=180, y=125)

btn_00 = tk.Button(root, text="00",relief='groove', command=lambda: add_to_calculation("00"), width=7, height=2, font="Roboto 14 bold", bg="black", fg="white")
btn_00.place(x=0, y=350)
btn_0 = tk.Button(root, text="0",relief='groove', command=lambda: add_to_calculation(0), width=7, height=2, font="Roboto 14 bold", bg="black", fg="white")
btn_0.place(x=90, y=350)
btn_dot = tk.Button(root, text=".", relief='groove',command=lambda: add_to_calculation("."), width=7, height=2, font="Roboto 14 bold", bg="black", fg="white")
btn_dot.place(x=180, y=350)

btn_div = tk.Button(root, text="/", relief='groove', command=lambda: add_to_calculation("/"), width=7, height=2, font="Roboto 14 bold", bg="grey", fg="white")
btn_div.place(x=270, y=50)
btn_mul = tk.Button(root, text="x", relief='groove',command=lambda: add_to_calculation("*"), width=7, height=2, font="Roboto 14 bold", bg="grey", fg="white")
btn_mul.place(x=270, y=125)
btn_minus = tk.Button(root, text="-", relief='groove',command=lambda: add_to_calculation("-"), width=7, height=2, font="Roboto 14 bold", bg="grey", fg="white")
btn_minus.place(x=270, y=200)
btn_plus = tk.Button(root, text="+", relief='groove',command=lambda: add_to_calculation("+"), width=7, height=2, font="Roboto 14 bold", bg="grey", fg="white")
btn_plus.place(x=270, y=275)

btn_equals = tk.Button(root, text="=",relief='groove', command=evaluate_calculation , width=7, height=2, font="Roboto 14 bold", bg="orange", fg="white")
btn_equals.place(x=270, y=350)


root.mainloop()