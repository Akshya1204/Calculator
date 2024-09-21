import tkinter as tk
import customtkinter as ctk
import re

root=tk.Tk()  
root.geometry('280x465')
root.title("Calculator")

def display_input(_input):
    input_box.insert(index=tk.INSERT,string=_input)
    display_result()

def display_result():
    try:
        calculation=input_box.get()
        if re.search(pattern=r'[\+\-\*\%/]',string=calculation):
            result=eval(calculation)
            result_lb.config(text=f'={result}')
        else:
            result_lb.config(text="")
    except Exception as error:
        print("error")

def delete_input():
    index=input_box.index(tk.INSERT)-1
    input_box.delete(index)
    display_result()

def clear_input():
    input_box.delete(0,tk.END)
    result_lb.config(text=" ")
    input_box.config(font=('Bold',20))
    result_lb.config(font=('Bold',20))

def highlight_result():
    input_box.config(font=('Bold',15))
    result_lb.config(font=('Bold',25))

def theme_changing():
    if root.cget('bg')=="SystemButtonFace":
        root.tk_setPalette("black")
        input_box.config(bg="black")
        theme_btn.config(text="🌞")
    else:
        root.tk_setPalette("SystemButtonFace")
        theme_btn.config(text="🌙")

input_box=tk.Entry(root,font=('bold',20),justify=tk.RIGHT,bd=0,bg="SystemButtonFace")
input_box.place(x=15,y=10,width=250,height=50)
# print(root.cget("bg"))    #To get the root window background color

result_lb=tk.Label(root,font=("bold",20),fg='gray',anchor=tk.E,bg='SystemButtonFace')
result_lb.place(x=15,y=70,width=250,height=50)

clear_btn=ctk.CTkButton(master=root,text="C",fg_color="#FF7433",height=40,width=40,font=("Bold",30),corner_radius=8,command=clear_input)
clear_btn.place(x=15,y=120)

delete_btn=ctk.CTkButton(master=root,text="D",fg_color="#FF7433",height=40,width=40,font=("Bold",30),corner_radius=8,command=delete_input)
delete_btn.place(x=80,y=120)

per_btn=ctk.CTkButton(master=root,text="%",fg_color="#FF7433",height=40,width=40,font=("Bold",30),corner_radius=8,command=lambda:display_input(_input='%'))
per_btn.place(x=145,y=120)

div_btn=ctk.CTkButton(master=root,text="÷",fg_color="#FF7433",height=40,width=40,font=("Bold",30),corner_radius=8,command=lambda:display_input(_input='÷'))
div_btn.place(x=215,y=120)

btn_7=ctk.CTkButton(master=root,text="7",height=40,width=40,font=("Bold",20),corner_radius=8,command=lambda:display_input(_input='7'))
btn_7.place(x=15,y=190)

btn_8=ctk.CTkButton(master=root,text="8",height=40,width=40,font=("Bold",20),corner_radius=8,command=lambda:display_input(_input='8'))
btn_8.place(x=80,y=190)

btn_9=ctk.CTkButton(master=root,text="9",height=40,width=40,font=("Bold",20),corner_radius=8,command=lambda:display_input(_input='9'))
btn_9.place(x=145,y=190)

mul_btn=ctk.CTkButton(master=root,text="×",fg_color="#FF7433",height=40,width=40,font=("Bold",30),corner_radius=8,command=lambda:display_input(_input='×'))
mul_btn.place(x=215,y=190)


btn_4=ctk.CTkButton(master=root,text="4",height=40,width=40,font=("Bold",20),corner_radius=8,command=lambda:display_input(_input='4'))
btn_4.place(x=15,y=265)

btn_5=ctk.CTkButton(master=root,text="5",height=40,width=40,font=("Bold",20),corner_radius=8,command=lambda:display_input(_input='5'))
btn_5.place(x=80,y=265)

btn_6=ctk.CTkButton(master=root,text="6",height=40,width=40,font=("Bold",20),corner_radius=8,command=lambda:display_input(_input='6'))
btn_6.place(x=145,y=265)

sub_btn=ctk.CTkButton(master=root,text="-",fg_color="#FF7433",height=40,width=40,font=("Bold",30),corner_radius=8,command=lambda:display_input(_input='-'))
sub_btn.place(x=215,y=265)

btn_1=ctk.CTkButton(master=root,text="1",height=40,width=40,font=("Bold",20),corner_radius=8,command=lambda:display_input(_input='1'))
btn_1.place(x=15,y=340)

btn_2=ctk.CTkButton(master=root,text="2",height=40,width=40,font=("Bold",20),corner_radius=8,command=lambda:display_input(_input='2'))
btn_2.place(x=80,y=340)

btn_3=ctk.CTkButton(master=root,text="3",height=40,width=40,font=("Bold",20),corner_radius=8,command=lambda:display_input(_input='3'))
btn_3.place(x=145,y=340)

add_btn=ctk.CTkButton(master=root,text="+",fg_color="#FF7433",height=40,width=40,font=("Bold",30),corner_radius=8,command=lambda:display_input(_input='+'))
add_btn.place(x=215,y=340)

theme_btn=tk.Button(root,text="🌙",font=("Bold",20),bd=0,command=theme_changing)
theme_btn.place(x=15,y=410,width=40,height=40)

zero_btn=ctk.CTkButton(master=root,text="0",height=40,width=40,font=("Bold",20),corner_radius=8,command=lambda:display_input(_input='0'))
zero_btn.place(x=80,y=410)

dot_btn=ctk.CTkButton(master=root,text=".",height=40,width=40,font=("Bold",20),corner_radius=8,command=lambda:display_input(_input='.'))
dot_btn.place(x=145,y=410)

equal_btn=ctk.CTkButton(master=root,text="=",fg_color="#FF7433",height=40,width=40,font=("Bold",30),corner_radius=8,command=highlight_result)
equal_btn.place(x=215,y=410)


root.mainloop()

