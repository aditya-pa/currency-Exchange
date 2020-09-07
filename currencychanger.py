import tkinter
from tkinter import ttk
from tkinter import *
import requests
from bs4 import BeautifulSoup
import csv

def simple():     
    def writing_data():
        with open("money_list.csv",'w',newline="") as csv_file:
            csv_writer=csv.writer(csv_file)
            for i in whole_list:
                csv_writer.writerow(i)

    def getting_data():
        return_list=[]
        with open("money_list.csv",'r') as csv_file:
            csv_reader=csv.reader(csv_file)
            for i in csv_reader:
                return_list.append(i)
        return(return_list)
    def convert(destination,money):
        dict1={}
        final_data=getting_data()
        for i in final_data:
            dict1[i[0]]=i[1]
        rate=float(dict1[destination])
        return money*rate

    def convert2(destination,money):
        dict1={}
        final_data=getting_data()
        for i in final_data:
            dict1[i[0]]=i[2]
        rate=float(dict1[destination])
        return money*rate

    def solve():
        s=clicked.get()
        d=clicked1.get()
        m=float(entry.get())
        if s==d:
            displaychar.set(str(m))
        elif s=='Rupee':
            displaychar.set(round(convert(d,m),2))
        elif d=='Rupee':
            displaychar.set(convert2(s,m))
        else:
            displaychar.set(round(convert(d,(convert2(s,m))),2))
    def clear():
        displaychar.set("0")
        entry.delete(0,END)
        entry.insert(0,"0")
            

        

    URL="https://www.x-rates.com/table/?from=INR&amount=1"
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/80.0.3987.163 Safari/537.36"}
    whole_list={}
    try:
        page=requests.get(URL,headers = headers)
        soup=BeautifulSoup(page.content,"html.parser")
        table=soup.find("table",attrs = {"class":"ratesTable"})
        for row in table.tbody.findAll("tr"):
            print("*")
            cells=row.findAll("td")
            row=[i.text for i in cells]
            whole_list[row[0]]=row[2]
        writing_data()
        final_data=getting_data()
        
    except:
        final_data=getting_data()



    root=tkinter.Tk()
    root.geometry("300x310")
    #root.resizable(0,0)
    root.title("Currency Converter")
    icon=PhotoImage(file = "calculator.png")
    root.tk.call('wm','iconphoto',root._w,icon)

    frame_1=Frame(root)
    frame_1.pack(expand=True,fill='both')
    frame_2=Frame(root)
    frame_2.pack(expand=True,fill='both')
    frame_3=Frame(root)
    frame_3.pack(expand=True,fill='both')
    frame_4=Frame(root)
    frame_4.pack(expand=True,fill='both')

    option=["Rupee",
    "US Dollar",
    "Euro",
    "British Pound",
    "Australian Dollar",
    "Canadian Dollar",
    "Singapore Dollar",
    "Swiss Franc",
    "Malaysian Ringgit",
    "Japanese Yen",
    "Chinese Yuan Renminbi"]
    clicked=StringVar()
    clicked.set(option[0])
    clicked1=StringVar()
    clicked1.set(option[0])
    displaychar=StringVar()
    drop=ttk.Combobox(frame_1,textvariable=clicked,)
    drop['values']=option
    drop.pack(anchor='nw',expand=True,fill='both')
    drop.config(font=('verdana',12),)
    entry=Entry(frame_1,font=('Verdana',20),background='#000000',fg='#c0c0c0',justify='center')
    entry.pack(expand=True,fill='both',anchor='n')
    entry.insert(0,"0.0")
    drop2=ttk.Combobox(frame_2,textvariable=clicked1)
    drop2['values']=option 
    drop2.config(font=('verdana',12),)
    drop2.pack(anchor='nw',expand=True,fill='both')
    label=Label(frame_2,font=('Verdana',20),background='#000000',fg='#c0c0c0',textvariable = displaychar,)
    label.pack(expand=True,fill='both')
    button_1=ttk.Button(frame_3,text="Convert",command=solve)
    button_1.pack(expand=True,fill='both')
    button_3=Button(frame_3,text="clear",relief='raised',command=clear)
    button_3.pack(expand=True,fill='both')
    ##button_3.config(bg='#696969',fg='#c0c0c0',font=('verdana',20),height=2)

    root.mainloop()


simple()
        
