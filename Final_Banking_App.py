from tkinter import *
from PIL import ImageTk,Image
import os
import mysql.connector
win=Tk()
win.title('Banking App')
win.iconbitmap('sbi.ico')
win.geometry('1368x768+0+0')

def finish_openacc():
    name=temp_name.get()
    accno=temp_accno.get()
    dob=temp_dob.get()
    address=temp_address.get()
    contact=temp_contact.get()
    openbal=temp_openbal.get()
    all_accounts=os.listdir()
    for i in all_accounts:
        if name==i:
            notif.config(fg='red',text='Account Already Exist!')
            return
    if name=="" or accno=="" or dob=="" or address=="" or contact=="" or openbal=="":
        notif.config(fg='red',text='All Field is required!')
        return    
    else:
        mydb=mysql.connector.connect(host='localhost',user='root',password='Pranshu@1603',database='bank')
        data1=(name,accno,dob,address,contact,openbal)
        sql1=('insert into account values(%s,%s,%s,%s,%s,%s)')
        data2=(name,accno,openbal)
        sql2=('insert into amount values(%s,%s,%s)')
        x=mydb.cursor()
        x.execute(sql1,data1)
        x.execute(sql2,data2)
        mydb.commit()
        print('Data entered successfully')
def openacc():
    global temp_name
    global temp_accno
    global temp_dob
    global temp_address
    global temp_contact
    global temp_openbal
    global notif
    temp_name=StringVar()
    temp_accno=StringVar()
    temp_dob=StringVar()
    temp_address=StringVar()
    temp_contact=StringVar()
    temp_openbal=StringVar()
    screen=Toplevel(win)
    screen.title('Create New Account Page')
    screen.iconbitmap('sbi.ico')
    screen.geometry('1368x768+0+0')
    Label(screen,text='Please Enter Your Details below For Registeration',font=('calibri',12)).grid(row=1,sticky=N)
    Label(screen,text='Name',font=('calibri',12)).grid(row=2,sticky=W)
    Label(screen,text='AccNo',font=('calibri',12)).grid(row=3,sticky=W)
    Label(screen,text='DOB',font=('calibri',12)).grid(row=4,sticky=W)
    Label(screen,text='Address',font=('calibri',12)).grid(row=5,sticky=W)
    Label(screen,text='Contact',font=('calibri',12)).grid(row=6,sticky=W)
    Label(screen,text='Openbal',font=('calibri',12)).grid(row=7,sticky=W) 
    Entry(screen,textvariable=temp_name).grid(row=2)
    Entry(screen,textvariable=temp_accno).grid(row=3)
    Entry(screen,textvariable=temp_dob).grid(row=4)
    Entry(screen,textvariable=temp_address).grid(row=5)
    Entry(screen,textvariable=temp_contact).grid(row=6)
    Entry(screen,textvariable=temp_openbal).grid(row=7)
    Button(screen,text='Create New Account',font=('calibri',12),command=finish_openacc).grid(row=8)
    notif=Label(screen,font=('Calibri',12))
    notif.grid(row=9)

def finish_depamt():    
    accno=temp_accno.get()
    amount=temp_amount.get()
    all_accounts=os.listdir()   
    if accno=="" or amount=="":
        notif.config(fg='red',text='All Field is required!')
        return    
    else:
        mydb=mysql.connector.connect(host='localhost',user='root',password='Pranshu@1603',database='bank')
        a='select bal from amount where accno=%s'
        data=(accno,)
        x=mydb.cursor()
        x.execute(a,data)
        result=x.fetchone()
        t=result[0]+int(amount)
        sql=('update amount set bal=%s where accno=%s')
        d=(t,accno)
        x.execute(sql,d)
        mydb.commit()
        print('Amount Depoisted Successfully :: Transaction Completed')
def depamt():    
    global temp_accno
    global temp_amount
    global notif
    temp_accno=StringVar()
    temp_amount=StringVar()
    screen=Toplevel(win)
    screen.title('Deposit Amount Page')
    screen.iconbitmap('sbi.ico')
    screen.geometry('1368x768+0+0')
    Label(screen,text='Please Enter Your Account Details For Transaction Such As "Account No" and "Deposit Amount"',font=('calibri',12)).grid(row=1,sticky=N)
    Label(screen,text='Account Number',font=('calibri',12)).grid(row=2,sticky=W)
    Label(screen,text='Deposit Amount',font=('calibri',12)).grid(row=3,sticky=W)    
    Entry(screen,textvariable=temp_accno).grid(row=2)
    Entry(screen,textvariable=temp_amount).grid(row=3)
    Button(screen,text='Deposit Account',font=('calibri',12),command=finish_depamt).grid(row=4)
    notif=Label(screen,font=('Calibri',12))
    notif.grid(row=5)

def finish_wtdamt():    
    accno=temp_accno.get()
    amount=temp_amount.get()
    all_accounts=os.listdir()   
    if accno=="" or amount=="":
        notif.config(fg='red',text='All Field is required!')
        return    
    else:
        mydb=mysql.connector.connect(host='localhost',user='root',password='Pranshu@1603',database='bank')
        a='select bal from amount where accno=%s'
        data=(accno,)
        x=mydb.cursor()
        x.execute(a,data)
        result=x.fetchone()
        t=result[0]-int(amount)
        sql=('update amount set bal=%s where accno=%s')
        d=(t,accno)
        x.execute(sql,d)
        mydb.commit()
        print('Amount Withdraw Successfully :: Transaction Completed')
def wtdamt():    
    global temp_accno
    global temp_amount
    global notif
    temp_accno=StringVar()
    temp_amount=StringVar()
    screen=Toplevel(win)
    screen.title('Widthdraw Amount Page')
    screen.iconbitmap('sbi.ico')
    screen.geometry('1368x768+0+0')
    Label(screen,text='Please Enter Your Account Details Such As "Account No" and "Withdraw Amount" For Withdrawing Amount',font=('calibri',12)).grid(row=1,sticky=N)
    Label(screen,text='Account Number',font=('calibri',12)).grid(row=2,sticky=W)
    Label(screen,text='Withdraw Amount',font=('calibri',12)).grid(row=3,sticky=W)    
    Entry(screen,textvariable=temp_accno).grid(row=2)
    Entry(screen,textvariable=temp_amount).grid(row=3)
    Button(screen,text='Withdraw Amount',font=('calibri',12),command=finish_wtdamt).grid(row=4)
    notif=Label(screen,font=('Calibri',12))
    notif.grid(row=5)

def finish_balenq():    
    accno=temp_accno.get()    
    all_accounts=os.listdir()   
    if accno=="":
        notif.config(fg='red',text='All Field is required!')
        return    
    else:
        mydb=mysql.connector.connect(host='localhost',user='root',password='Pranshu@1603',database='bank')
        a='select bal from amount where accno=%s'
        data=(accno,)
        x=mydb.cursor()
        x.execute(a,data)
        result=x.fetchone()        
        mydb.commit()
        print("Your account balance is:", result)        
def balenq():    
    global temp_accno    
    global notif
    temp_accno=StringVar()    
    screen=Toplevel(win)
    screen.title('Balance Enquiry Page')
    screen.iconbitmap('sbi.ico')
    screen.geometry('1368x768+0+0')
    Label(screen,text='Please Enter Your Account Details i.e "Account No" for balance enquiry',font=('calibri',12)).grid(row=1,sticky=N)
    Label(screen,text='Account Number',font=('calibri',12)).grid(row=2,sticky=W)   
    Entry(screen,textvariable=temp_accno).grid(row=2)   
    Button(screen,text='Balance Enquiry',font=('calibri',12),command=finish_balenq).grid(row=3)
    notif=Label(screen,font=('Calibri',12))
    notif.grid(row=4)

def finish_displaydetails():    
    accno=temp_accno.get()    
    all_accounts=os.listdir()   
    if accno=="":
        notif.config(fg='red',text='All Field is required!')
        return    
    else:
        mydb=mysql.connector.connect(host='localhost',user='root',password='Pranshu@1603',database='bank')
        a='select * from account where accno=%s'
        data=(accno,)
        x=mydb.cursor()
        x.execute(a,data)
        result=x.fetchone()        
        mydb.commit()
        print("Customer Details are:",result)        
def displaydetails():    
    global temp_accno    
    global notif
    temp_accno=StringVar()    
    screen=Toplevel(win)
    screen.title('Account Details  Page')
    screen.iconbitmap('sbi.ico')
    screen.geometry('1368x768+0+0')
    Label(screen,text='Please Enter Your "Account No" for Viewing Your Account Details',font=('calibri',12)).grid(row=1,sticky=N)
    Label(screen,text='Account Number',font=('calibri',12)).grid(row=2,sticky=W)   
    Entry(screen,textvariable=temp_accno).grid(row=2)   
    Button(screen,text='Dispaly Customer Details',font=('calibri',12),command=finish_displaydetails).grid(row=3)
    notif=Label(screen,font=('Calibri',12))
    notif.grid(row=4)

def finish_closeacc():    
    accno=temp_accno.get()    
    all_accounts=os.listdir()   
    if accno=="":
        notif.config(fg='red',text='All Field is required!')
        return    
    else:
        mydb=mysql.connector.connect(host='localhost',user='root',password='Pranshu@1603',database='bank')
        a='delete from amount where accno=%s'
        b='delete from account where accno=%s'
        data=(accno,)
        x=mydb.cursor()
        x.execute(a,data)
        result=x.fetchone()        
        mydb.commit()
        print("Your Account is Deleted Now:",result)        
def closeacc():    
    global temp_accno    
    global notif
    temp_accno=StringVar()    
    screen=Toplevel(win)
    screen.title('Closing Account Page')
    screen.iconbitmap('sbi.ico')
    screen.geometry('1368x768+0+0')
    Label(screen,text='Please Enter Your "Account No" for Closing Your Account',font=('calibri',12)).grid(row=1,sticky=N)
    Label(screen,text='Account Number',font=('calibri',12)).grid(row=2,sticky=W)   
    Entry(screen,textvariable=temp_accno).grid(row=2)   
    Button(screen,text='Close Account',font=('calibri',12),command=finish_closeacc).grid(row=3)
    notif=Label(screen,font=('Calibri',12))
    notif.grid(row=4)
    
def finish_login():
    name=temp_name.get()
    password=temp_password.get()
    all_accounts=os.listdir()
    if name=="" or password=="":
        notif.config(fg='red',text='All Field is required!')
        return        
    else:
        mydb=mysql.connector.connect(host='localhost',user='root',password='Pranshu@1603',database='bank')
        x=mydb.cursor()
        x.execute('select * from register where name=%s and password=%s',(name,password))
        result=x.fetchone()
        if result==None:
            return
        else:
            notif.config(fg='green',text='Correct Cereditials!')
            mydb.commit()
            funct()
def login():
    global temp_name
    global temp_password
    global notif
    temp_name=StringVar()
    temp_password=StringVar()
    screen=Toplevel(win)
    screen.title('SBI Login Page')
    screen.iconbitmap('sbi.ico')
    screen.geometry('1368x768+0+0')
    Label(screen,text='Please Enter Your Ceredential To Login',font=('calibri',12)).grid(row=1,sticky=N)
    Label(screen,text='Name',font=('calibri',12)).grid(row=2,sticky=W)
    Label(screen,text='Password',font=('calibri',12)).grid(row=3,sticky=W)
    Entry(screen,textvariable=temp_name).grid(row=2)
    Entry(screen,textvariable=temp_password,show='*').grid(row=3)
    Button(screen,text='Login',font=('calibri',12),command=finish_login).grid(row=4)
    notif=Label(screen,font=('Calibri',12))
    notif.grid(row=5,sticky=N)
    
def finish_reg():
    name=temp_name.get()
    password=temp_password.get()
    all_accounts=os.listdir()
    for i in all_accounts:
        if name==i and password==i:
            notif.config(fg='red',text='Already Registered!')
            return
    if name=="" or password=="":
        notif.config(fg='Red',text='All Field is required')
        return    
    else:
        mydb=mysql.connector.connect(host='localhost',user='root',password='Pranshu@1603',database='bank')
        data1=(name,password)
        sql1=('insert into register values(%s,%s)')
        x=mydb.cursor()
        x.execute(sql1,data1)
        mydb.commit()
        notif.config(fg='green',text='You Have Been Successfully Registered')
        login()

def reg():
    global temp_name
    global temp_password
    global notif
    temp_name=StringVar()
    temp_password=StringVar()
    screen=Toplevel(win)
    screen.title('SBI Registeration Page')
    screen.iconbitmap('sbi.ico')
    screen.geometry('1368x768+0+0')
    Label(screen,text='Please Enter Your Details below For Registeration',font=('calibri',12)).grid(row=1,sticky=N)
    Label(screen,text='Name',font=('calibri',12)).grid(row=2,sticky=W)
    Label(screen,text='Password',font=('calibri',12)).grid(row=3,sticky=W)    
    Entry(screen,textvariable=temp_name).grid(row=2)
    Entry(screen,textvariable=temp_password,show='*').grid(row=3)
    Button(screen,text='Register',font=('calibri',12),command=finish_reg).grid(row=4)
    notif=Label(screen,font=('Calibri',12))
    notif.grid(row=5)   
def funct():          
    screen=Toplevel(win)
    screen.title('SBI Login Page')
    screen.iconbitmap('sbi.ico')
    screen.geometry('1368x768+0+0')
    Button(screen,text='Open Account',font=('calibri',12),width=30,command=openacc).grid(row=3)
    Button(screen,text='Deposit Amount',font=('calibri',12),width=30,command=depamt).grid(row=4)
    Button(screen,text='Withdraw Amount',font=('calibri',12),width=30,command=wtdamt).grid(row=5)
    Button(screen,text='Balance Enquiry',font=('calibri',12),width=30,command=balenq).grid(row=6)
    Button(screen,text='Customer Details',font=('calibri',12),width=30,command=displaydetails).grid(row=7)
    Button(screen,text='Close Account',font=('calibri',12),width=30,command=closeacc).grid(row=8)
    
Label(win,text='SBI Customer Banking Services Beta Version',font=('calibri',20)).grid(row=0,sticky=N)
Label(win,text='The Most Secure Bank You have probably used',font=('calibri',16)).grid(row=1,sticky=N)
img=Image.open('bank.png')
img=img.resize((1368,400))
img=ImageTk.PhotoImage(img)
Label(win,image=img).grid(row=2,sticky=N)
Button(win,text='Register',font=('calibri',12),width=30,command=reg).grid(row=3)
Button(win,text='Login',font=('calibri',12),width=30,command=login).grid(row=4)
win.mainloop()

