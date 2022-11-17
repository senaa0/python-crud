import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['id'])
    e2.insert(0,select['cariadi'])
    e3.insert(0,select['vno'])
    e4.insert(0,select['vergidairesi'])
    e5.insert(0,select['adres'])
    e6.delete(0, select['telefon'])
    e7.delete(0, select['sehir'])
    


def Add():
    id = e1.get()
    cariadi = e2.get()
    vno = e3.get()
    vergidairesi = e4.get()
    adres = e5.get()
    telefon = e6.get()
    sehir = e7.get()

    mysqldb=mysql.connector.connect(host="93.89.225.112",user="pehozgun_admina",password="Admin5050",database="pehozgun_verita")
    mycursor=mysqldb.cursor()

    try:
       sql = "INSERT INTO  musteri (id,cariadi,vno,vergidairesi,adres,telefon,sehir) VALUES (%s, %s, %s, %s, %s, %s, %s)"
       val = (id,cariadi,vno,vergidairesi,adres,telefon,sehir)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Başarıyla eklendi...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e6.delete(0, END)
       e7.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()


def update():
    id = e1.get()
    cariadi = e2.get()
    vno = e3.get()
    vergidairesi = e4.get()
    adres = e5.get()
    telefon = e6.get()
    sehir = e7.get()
    mysqldb=mysql.connector.connect(host="93.89.225.112",user="pehozgun_admina",password="Admin5050",database="pehozgun_verita")
    mycursor=mysqldb.cursor()

    try:
       sql = "Update  musteri set cariadi= %s,vno= %s,vergidairesi= %s,adres= %s,telefon= %s,sehir= %s where id= %s"
       val = (cariadi,vno,vergidairesi,adres,telefon,sehir,id)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Başarıyla Güncellendi...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e6.delete(0, END)
       e7.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()
       

def delete():
    id = e1.get()

    mysqldb=mysql.connector.connect(host="93.89.225.112",user="pehozgun_admina",password="Admin5050",database="pehozgun_verita")
    mycursor=mysqldb.cursor()

    try:
       sql = "delete from musteri where id = %s"
       val = (id,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Başarıyla silindi...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e6.delete(0, END)
       e7.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()
def show():
        mysqldb = mysql.connector.connect(host="93.89.225.112",user="pehozgun_admina",password="Admin5050",database="pehozgun_verita")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT id,cariadi,vno,vergidairesi,adres,telefon,sehir FROM musteri")
        records = mycursor.fetchall()
        print(records)

        for i, (id, cariadi, vno, vergidairesi, adres, telefon, sehir) in enumerate(records, start=1):
            listBox.insert("", "end", values=(id, cariadi, vno, vergidairesi, adres, telefon, sehir))
            mysqldb.close()

root = Tk()
root.geometry("1000x500")
global e1
global e2
global e3
global e4
global e5
global e6
global e7


tk.Label(root, text="ID").place(x=10, y=10)
Label(root, text="Cari adı").place(x=10, y=40)
Label(root, text="VNO").place(x=10, y=70)
Label(root, text="Vergi dairesi").place(x=10, y=100)
Label(root, text="Adres").place(x=370, y=10)
Label(root, text="Telefon").place(x=370, y=40)
Label(root, text="Şehir").place(x=370, y=70)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

e5 = Entry(root)
e5.place(x=450, y=10)

e6 = Entry(root)
e6.place(x=450, y=40)

e7 = Entry(root)
e7.place(x=450, y=70)

Button(root, text="Ekle",command = Add,height=3, width= 13,bg="green",).place(x=30, y=130)
Button(root, text="Güncelle",command = update,height=3, width= 13,bg="blue",).place(x=140, y=130)
Button(root, text="Sil",command = delete,height=3, width= 13,bg="red",).place(x=250, y=130)

cols = ('id', 'cariadi', 'vno', 'vergidairesi', 'adres', 'telefon', 'sehir')
listBox = ttk.Treeview(root, columns=cols, show='headings' )

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=100, y=250)

show()
listBox.bind('<Double-Button-1>',GetValue)

root.mainloop()