from tkinter import *#* imports every class
from tkinter import messagebox #messagebox is not in * of tkinter
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_letters=[random.choice(letters) for _ in range(nr_letters)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list=password_letters+password_numbers+password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)#jions every letter for password

    password_entry.insert(0,password)#inseret the password when generate button is clicked and insert it from index 0
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops" , message="please make sure you haven't left any of the field empty!!!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password}\n Is it ok to save?")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n ")
                website_entry.delete(0,END)#delete every thing from 0 to last letter
                password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
logo_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

website_label=Label(text="Website")
website_label.grid(row=1,column=0)

website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()#so that entry is prepopulated

email_label=Label(text="Email/Username")
email_label.grid(row=2,column=0)

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0, "umakant@gmail.com")#pre populated example email

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

generate_password_button=Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)

add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

# b.grid(row=2,column=0,columnspan=2) #here columnspan allows to take 2 column

window.mainloop()