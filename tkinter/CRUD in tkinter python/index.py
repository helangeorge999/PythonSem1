from tkinter import *
import tkinter.messagebox as messagebox
import mysql.connector as mysql



def Create():
    if(id ==""or name =="" or phone ==""):
        messagebox.showinfo("ALERT","Insert value!")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="helan_george", port=3306)
        cursor = con.cursor()

        query = "insert into students values(%s, %s, %s)"
        values = (id, name, phone)
        cursor.execute(query, values)
        cursor.execute("commit")

        messagebox.showinfo("Status","Successfully Inserted!")
        con.close();

def Update():
    if(id ==""or name =="" or phone ==""):
        messagebox.showinfo("ALERT","Update value!")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="helan_george", port=3306)
        cursor = con.cursor()
        query = "update students set name = %s, phone = %s where id = %s"
        values = (name, phone, id)
        cursor.execute(query, values)
        cursor.execute("commit")

        messagebox.showinfo("Status","Successfully Updated!")
        con.close();

def Read():
    if(id ==""):
        messagebox.showinfo("ALERT","Enter ID to Read!")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="helan_george", port=3306)
        cursor = con.cursor()
        query = "select * from students where id = %s"
        values = (id)
        cursor.execute(query, values)
        cursor.execute("commit")

        messagebox.showinfo("Status","Successfully Read!")
        con.close();

def Delete():
    if(id ==""):
        messagebox.showinfo("ALERT","Enter ID to Delete!")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="helan_george", port=3306)
        cursor = con.cursor()
        query = "delete from students where id = %s"
        values = (id)
        cursor.execute(query, values)
        cursor.execute("commit")

        messagebox.showinfo("Status","Successfully Deleted!")
        con.close();

Create_Button = Button(root, text="Create", command=Create, bg='green').place(x=150, y=160)
Update_Button = Button(root, text='Update', command=Update, bg='yellow').place(x=200, y=160)
Delete_Button = Button(root, text="Delete", command=Delete, bg='red').place(x=253, y=160)
Read_Button = Button(root, text="Select", command=Read, bg="grey").place(x=303, y=160)

#create form in tkinter
root = Tk()
root.geometry("350x200")
root.title("CRUD")
root.eval('tk::PlaceWindow . Center')
user_id = Label(root, test = "Id:")

user_id.place(x=50, y=30)
user_entry = Entry(root, width=32)
user_entry.place(x=150, y=30)

name = Label (root, text="Full name:")
name.place(x=50, y=80)
name_entry = Entry(root, width=32)
name_entry.place(x=150, y=80)

phone = Label(root,text="'Phone:")
phone.place(x=50, y=130)
phone_entry= Entry(root, width=32)
phone_entry.place(x=150, y=130)


root.mainloop()