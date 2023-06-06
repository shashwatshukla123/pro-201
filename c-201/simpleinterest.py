from tkinter import *
window=Tk()


def calculate_interest():
    p=float(principal_entry.get())
    r=float(rate_entry.get())
    t=float(time_entry.get())
    i=(p*r*t)/100
    interest= round(i,2)
    
    
    
    

    show_label.destroy()


    message=Label(result_frame,text="Interest on Rs."+str(p)+" at the rate of interest "+str(r)+" for "+str(t)+" years is"+str(interest), bg = "#42ecf5", font=("Calibri", 12), width=42)
    message.place(x=20,y=40)
    message.pack()

window.title('Interest Calculator')
window.geometry("430x500")
window.configure(bg='#42ecf5')

app_label=Label(window, text="     INTEREST CALCULATOR", fg = "black", bg = "#42ecf5", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)


principal_label=Label(window, text="Enter principal", fg = "black", bg = "#42ecf5", font=("Calibri", 12),bd=1)
principal_label.place(x=20, y=90)

principal_entry=Entry(window, text="", bd=2, width=22)
principal_entry.place(x=150, y=92)


rate_label=Label(window, text="Enter Rate", fg = "black", bg = "#42ecf5", font=("Calibri", 12),bd=10)
rate_label.place(x=11, y=140)

rate_entry=Entry(window, text="", bd=5, width=22)
rate_entry.place(x=150,y=142)


time_label=Label(window, text="Enter time(year)", fg = "black", bg = "#42ecf5", font=("Calibri", 12),bd=15)
time_label.place(x=8,y=185)

time_entry=Entry(window, text="", bd=5, width=22)
time_entry.place(x=150,y=187)


calculate_button=Button(window, text="Calculate", fg="black", bg="white", bd=20,command=calculate_interest)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result", bg = "black", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=350)

show_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
show_label.place(x=20,y=20)
show_label.pack()

window.mainloop()