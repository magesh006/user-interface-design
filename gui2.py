import tkinter as tk
rt=tk.Tk()
rt.title("gui test")
rt.geometry("400x300")
def buttonc():
    ip=inp.get()
    if ip:
        rl.config(text=f"hello {ip} welcome to alaska",fg="red")
    else:
        rl.config("please enter your name")    


rl=tk.Label(rt,text="hello")
rl.pack(padx =30,pady=20)
inp=tk.Entry(rt)
inp.pack(pady=30)
ab=tk.Button(rt,text="greet me",command=buttonc,font=("Arial"))
ab.pack(pady=30)
rt.mainloop()