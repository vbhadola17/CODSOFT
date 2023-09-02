from tkinter import *
import string 
import random       # to generate random password importing random module

def generator():
    small_alphabets=string.ascii_lowercase        #to print lowercase alphabets 
    capital_alphabets=string.ascii_uppercase      #to print uppercase alphabets
    numbers=string.digits                         #to print digits
    special_characters=string.punctuation         #to print special characters 

    whole=small_alphabets+capital_alphabets+numbers+special_characters
    password_length=int(length_box.get())   #length box generate password in form of string so converting it to int data type
    if choice.get()==1:
        passwordfield.insert(0,random.sample(small_alphabets,password_length))
    if choice.get()==2:
        passwordfield.insert(0,random.sample(small_alphabets + capital_alphabets,password_length))
    
    if choice.get()==3:
        passwordfield.insert(0,random.sample(whole,password_length))
    
    #password=random.sample(whole,password_length)
    #passwordfield.insert(0,password)
 


a=Tk()
a.config(bg='white')                              # for background color
choice=IntVar()
Font=('arial',15,'bold')
passwordlabel=Label(a,text='password generator',font=('roman',20,'bold'),bg='white',fg='black')
passwordlabel.grid(pady=10)
weakradiobutton=Radiobutton(a,text='weak',value=1,variable=choice,font=Font)
#here,if choice value choosen by user is 1 then weak radio button is enabled which generate weak password
weakradiobutton.grid(pady=5)                       #vertical padding

mediumradiobutton=Radiobutton(a,text='medium',value=2,variable=choice,font=Font) 
#here,if choice value is choosen 2 by user it generate medium password
mediumradiobutton.grid(pady=5)                     #vertical padding

strongradiobutton=Radiobutton(a,text='strong',value=3,variable=choice,font=Font)
#here if choice is 3 then strong password is generated
strongradiobutton.grid(pady=5)                     #vertical padding

lengthlabel=Label(a,text='password length',font=Font,bg='white',fg='black')
lengthlabel.grid()

length_box=Spinbox(a,from_=7,to_=18,width=5,font=Font)  #used to create spinbox
length_box.grid()

generatebutton=Button(a,text='generate',font=Font,command=generator)
generatebutton.grid(pady=5)         # vertical padding of 5

passwordfield=Entry(a,width=25,bd=2)
passwordfield.grid()


a.mainloop()
