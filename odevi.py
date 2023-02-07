# pip install PyMySQL
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

# connection for phpmyadmin


def connection():
    conn = pymysql.connect(
        host='**.**.***.***',
        user='username',
        password='password',
        db='databasename',
    )
    return conn


def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array,
                       text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)


root = Tk()
root.title("Student Registration System")
root.geometry("1600x1400")
my_tree = ttk.Treeview(root)

# placeholders for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

# placeholder set value function


def setph(word, num):
    if num == 1:
        ph1.set(word)
    if num == 2:
        ph2.set(word)
    if num == 3:
        ph3.set(word)
    if num == 4:
        ph4.set(word)
    if num == 5:
        ph5.set(word)


def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM musteri")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def add():
    id = str(idEntry.get())
    cariadi = str(cariadiEntry.get())
    vno = str(vnoEntry.get())
    vergidairesi = str(vergidairesiEntry.get())
    adres = str(adresEntry.get())
    telefon = str(telefonEntry.get())
    sehir = str(sehirEntry.get())

    if (id == "null" or id == "null") or (cariadi == "" or cariadi == " ") or (vno == "" or vno == " ") or (vergidairesi == "" or vergidairesi == " ") or (adres == "" or adres == " ") or (telefon == "" or telefon == " ") or (sehir == "" or sehir == " "):
        messagebox.showinfo("Hata", "Lütfen boş alanı doldurun")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO musteri VALUES ('"+id+"','" +
                           cariadi+"','"+vno+"','"+vergidairesi+"','"+adres+"','"+telefon+"','"+sehir+"') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
            return

    refreshTable()


def reset():
    decision = messagebox.askquestion("Uyarı!!", "Hepsini silmek istediğinize Emin misiniz?")
    if decision != "evet":
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM musteri")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Hata", "Üzgünüm bir hata oluştu")
            return

        refreshTable()


def delete():
    decision = messagebox.askquestion("Uyarı!!", "Silmek istediğinize Emin misiniz?")
    if decision != "evet":
        return
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM musteri WHERE id='" +
                           str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Hata", "Üzgünüm bir hata oluştu")
            return

        refreshTable()


def select():
    try:
        selected_item = my_tree.selection()[0]
        id = str(my_tree.item(selected_item)['values'][0])
        cariadi = str(my_tree.item(selected_item)['values'][1])
        vno = str(my_tree.item(selected_item)['values'][2])
        vergidairesi = str(my_tree.item(selected_item)['values'][3])
        adres = str(my_tree.item(selected_item)['values'][4])

        setph(id, 1)
        setph(cariadi, 2)
        setph(vno, 3)
        setph(vergidairesi, 4)
        setph(adres, 5)
    except:
        messagebox.showinfo("Error", "Please select a data row")


def search():
    id = str(idEntry.get())
    cariadi = str(cariadiEntry.get())
    vno = str(vnoEntry.get())
    vergidairesi = str(vergidairesiEntry.get())
    adres = str(adresEntry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM musteri WHERE id='" +
                   id+"' or cariadi='" +
                   cariadi+"' or vno='" +
                   vno+"' or vergidairesi='" +
                   vergidairesi+"' or adres='" +
                   adres+"' ")

    try:
        result = cursor.fetchall()

        for num in range(0, 5):
            setph(result[0][num], (num+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")


def update():
    selectedid = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedid = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Hata", "Lütfen veri satırını seçin")

    id = str(idEntry.get())
    cariadi = str(cariadiEntry.get())
    vno = str(vnoEntry.get())
    vergidairesi = str(vergidairesiEntry.get())
    adres = str(adresEntry.get())
    telefon = str(telefonEntry.get())
    sehir = str(sehirEntry.get())


    if (id == "" or id == " ") or (cariadi == "" or cariadi == " ") or (vno == "" or vno == " ") or (vergidairesi == "" or vergidairesi == " ") or (adres == "" or adres == " ") or (telefon == "" or telefon == " ") or (sehir == "" or sehir == " "):
        messagebox.showinfo("Hata", "Lütfen boş alanı doldurun")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE musteri SET id='" +
                           id+"', cariadi='" +
                           cariadi+"', vno='" +
                           vno+"', vergidairesi='" +
                           vergidairesi+"', adres='" +
                           adres+"', telefon='" +
                           telefon+"', sehir='" +
                           sehir+"' WHERE id='" +
                           selectedid+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
            return

    refreshTable()


label = Label(root, text="MÜŞTERİ BİLGİLERİ",
              font=('Arial Bold', 20))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=20, pady=20)

idLabel = Label(root, text="ID", font=('Arial', 15))
cariadiLabel = Label(root, text="Cari Adı", font=('Arial', 15))
vnoLabel = Label(root, text="VNO", font=('Arial', 15))
vergidairesiLabel = Label(root, text="Vergi Dairesi", font=('Arial', 15))
adresLabel = Label(root, text="Adres", font=('Arial', 15))
telefonLabel = Label(root, text="Telefon", font=('Arial', 15))
sehirLabel = Label(root, text="Şehir", font=('Arial', 15))

idLabel.grid(row=3, column=0, columnspan=1, padx=20, pady=5)
cariadiLabel.grid(row=4, column=0, columnspan=1, padx=20, pady=5)
vnoLabel.grid(row=5, column=0, columnspan=1, padx=20, pady=5)
vergidairesiLabel.grid(row=6, column=0, columnspan=1, padx=20, pady=5)
adresLabel.grid(row=7, column=0, columnspan=1, padx=20, pady=5)
telefonLabel.grid(row=8, column=0, columnspan=1, padx=20, pady=5)
sehirLabel.grid(row=9, column=0, columnspan=1, padx=20, pady=30)

idEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph1)
cariadiEntry = Entry(root, width=55, bd=5, font=(
    'Arial', 15), textvariable=ph2)
vnoEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph3)
vergidairesiEntry = Entry(root, width=55, bd=5,
                          font=('Arial', 15), textvariable=ph4)
adresEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph5)
telefonEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph5)
sehirEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable=ph5)

idEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
cariadiEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
vnoEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
vergidairesiEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
adresEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)
telefonEntry.grid(row=8, column=1, columnspan=4, padx=5, pady=0)
sehirEntry.grid(row=9, column=1, columnspan=4, padx=5, pady=0)

addBtn = Button(
    root, text="Ekle", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84F894", command=add)
updateBtn = Button(
    root, text="Güncelle", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84E8F8", command=update)
deleteBtn = Button(
    root, text="Sil", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#FF9999", command=delete)
resetBtn = Button(
    root, text="Sıfırla", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F398FF", command=reset)
selectBtn = Button(
    root, text="Listele", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#EEEEEE", command=select)

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
resetBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=13, column=5, columnspan=1, rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree['columns'] = ("id", "cariadi", "vno",
                      "vergidairesi", "adres", "telefon", "sehir")
               

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("id", anchor=W, width=170)
my_tree.column("cariadi", anchor=W, width=150)
my_tree.column("vno", anchor=W, width=150)
my_tree.column("vergidairesi", anchor=W, width=165)
my_tree.column("adres", anchor=W, width=180)
my_tree.column("telefon", anchor=W, width=135)
my_tree.column("sehir", anchor=W, width=120)

my_tree.heading("id", text="ID", anchor=W)
my_tree.heading("cariadi", text="Cari Adı", anchor=W)
my_tree.heading("vno", text="VNO", anchor=W)
my_tree.heading("vergidairesi", text="Vergi Dairesi", anchor=W)
my_tree.heading("adres", text="Adres", anchor=W)
my_tree.heading("telefon", text="Telefon", anchor=W)
my_tree.heading("sehir", text="Şehir", anchor=W)

refreshTable()

root.mainloop()
