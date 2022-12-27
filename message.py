from tkinter import *
import time
import random
import tkinter.messagebox
import sqlite3

Logged = False

db= sqlite3.connect("users.db")
cs=db.cursor()
cs.execute("create table if not exists Cust(User_ID integer PRIMARY KEY, Username text UNIQUE, Password text NOT_NULL,Phone text UNIQUE,Address text NOT_NULL)")



#################################################################    Page1   ###########################################################################
def page1():
    
    global win1
    win1 = Toplevel()
    win1.geometry("1350x750+0+0")
    win1.configure(background='orange')
    win1.title("User Info")
    lblTitle=Label(win1,font=('arial',60,'bold'),text='Ωmega\n',bg='orange',
                   fg='white',justify=CENTER)
    lblTitle.pack(side=TOP)
    Button(win1,text="Login",bd=0,fg="black",bg="orange",font=('arial',30,'bold'),pady=10,command=login).pack(side=TOP)
    Button(win1,text="Signup",bd=0,fg="black",bg="orange",font=('arial',30,'bold'),pady=10,command=register).pack(side=TOP)
    Button(win1,text="Back",bd=0,fg="black",bg="orange",font=('arial',30,'bold'),pady=10,command=lambda: win1.destroy()).pack(side=BOTTOM)

######################################################################################################################################################     
#register menu
def register():
    global registMenu
    registMenu = Toplevel()
    registMenu.configure(background='orange')
    registMenu.title("Register")
    registMenu.geometry("720x500+0+0")
    
    global username
    global password
    global num
    global address
    
    
    username = StringVar()
    password = StringVar()
    address = StringVar()
    num = StringVar()
    
    Label(registMenu, text="Please enter details below",font=('arial',30,'bold'),fg="white",justify="center", bg="orange").pack(side=TOP)
    
    Label(registMenu,font=('arial',20,'bold'), bg="orange", text="Username  ").place(x=25,y=100)
    
    Entry(registMenu, textvariable=username).place(x=200,y=110)
    
    Label(registMenu,font=('arial',20,'bold'), bg="orange", text="Password  ").place(x=25,y=200)
    
    Entry(registMenu, textvariable=password, show='*').place(x=200,y=210)
    
    Label(registMenu,font=('arial',20,'bold'), bg="orange", text="Address  ").place(x=25,y=300)
    
    Entry(registMenu, textvariable=address).place(x=200,y=310)

    Label(registMenu,font=('arial',20,'bold'), bg="orange", text="Phone  ").place(x=25,y=400)
    
    Entry(registMenu, textvariable=num).place(x=200,y=410)
    
    Button(registMenu,bd=0, text="Register",font=('arial',20,'bold'), width=10, height=1, bg="orange",command=registuser).place(x=370,y=420)
    Button(registMenu,bd=0, text="Close",font=('arial',20,'bold'), width=10, height=1, bg="orange",command=lambda: registMenu.destroy()).place(x=520,y=420)

######################################################################################################################################################
    #registering users
def registuser():
    username_info = username.get()
    password_info = password.get()
    Uaddress=address.get()
    Phone=num.get()
    rand=random.randint(1,500876)
    if username_info == "" or password_info == "" or Uaddress == "" or Phone == "":
        Label(registMenu, text="Registration error", fg="red",bg="orange", font=("calibri", 11),justify="center").place(x=130,y=50)
    else:
        cs.execute(f"insert into Cust(User_ID , Username , Password ,Phone ,Address) values({rand},'{username_info}','{password_info}','{Phone}','{Uaddress}')")
        db.commit()
        
        Label(registMenu, text="Registration Success", fg="green",bg="orange", font=("calibri", 11),justify="center").place(x=130,y=50)
    
######################################################################################################################################################
#login menu
def login():
    
    global logMenu
    logMenu = Toplevel()
    logMenu.configure(background='orange')
    logMenu.title("Login")
    logMenu.geometry("720x500+0+0")
    
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 

 
    Label(logMenu, text="Fill Your Information Please",fg="white",font=('arial',30,'bold'),justify="center", bg="orange").pack(side=TOP)
    
    Label(logMenu,font=('arial',15,'bold'), bg="orange", text="Username  ").place(x=198,y=150)
    Entry(logMenu, textvariable=username_verify).place(x=333,y=155)
    
    Label(logMenu,font=('arial',15,'bold'), bg="orange", text="Password  ").place(x=198,y=200)
    Entry(logMenu, textvariable=password_verify, show='*').place(x=333,y=205)
    
    Button(logMenu,bd=0, text="Login",font=('arial',20,'bold'), width=10, height=1, bg="orange",command=Verfying).place(x=370,y=420)
    Button(logMenu,bd=0, text="Close",font=('arial',20,'bold'), width=10, height=1, bg="orange",command=lambda : logMenu.destroy()).place(x=520,y=420) 
######################################################################################################################################################     

#Verfying users
def Verfying(): 
     
    userV=username_verify.get()
    passV=password_verify.get()
    with sqlite3.connect("users.db") as db:
        cs=db.cursor()
        cs.execute(f"select * from Cust WHERE Username='{userV}' AND Password='{passV}'")
        global results
        results= cs.fetchall()
        
        if results:
            global Logged
            Logged = True
            global ID
            ID = results[0][0]
            Label(logMenu, text=f"\t\tWelcome Home {userV}\t\t\n", fg="green",bg="orange", font=("calibri", 20),justify="center").place(x=30,y=50)

        else:
            Label(logMenu, text="  UserName Not Found\t\n Try Again", fg="red",bg="orange", font=("calibri", 20),justify="center").place(x=220,y=50)
        

######################################################################################################################################################           
def update():
    if Logged==True:
        global Upmenu
        Upmenu=Toplevel()
        Upmenu.configure(background='orange')
        Upmenu.title("Update")
        Upmenu.geometry("720x500+0+0")

        global new_username
        global new_Password
        global newNum
        global new_address

        new_username = StringVar()
        new_Password=StringVar()
        newNum=StringVar()
        new_address=StringVar()


        
        Label(Upmenu, text="  Choose What you Want To update\n\n", fg="White",bg="orange", font=('arial',30,'bold'),justify="center").pack(side=TOP)

        Entry(Upmenu, textvariable=new_username).place(x=200,y=125)
    
        Entry(Upmenu, textvariable=new_Password).place(x=200,y=225)
    
        Entry(Upmenu, textvariable=new_address).place(x=200,y=325)
    
        Entry(Upmenu, textvariable=newNum).place(x=200,y=425)
        
        Button(Upmenu,text="Username",bd=0,fg="black",bg="orange",font=('arial',20,'bold'),pady=10,command=updateUser).place(x=25,y=100)
        Button(Upmenu,text="Password",bd=0,fg="black",bg="orange",font=('arial',20,'bold'),pady=10,command=updatePass).place(x=25,y=200)
        Button(Upmenu,text="Address",bd=0,fg="black",bg="orange",font=('arial',20,'bold'),pady=10,command=updateAdd).place(x=25,y=300)
        Button(Upmenu,text="Phone",bd=0,fg="black",bg="orange",font=('arial',20,'bold'),pady=10,command=updateNum).place(x=25,y=400)
        Button(Upmenu,bd=0, text="Close",font=('arial',20,'bold'), width=10, height=1, bg="orange",command=lambda : Upmenu.destroy()).place(x=520,y=420)
    else:
        tkinter.messagebox.showerror(title="Caution",message="You have to Login First")
######################################################################################################################################################
def updateUser():
    name0=new_username.get()   
    with sqlite3.connect("users.db") as db:
        cr=db.cursor()
        cr.execute(f"update Cust set Username ='{name0}' Where User_ID={ID}")
    time.sleep(1)    
    
     
###################################################################################################################################################### 
def updatePass():
    pass0=new_Password.get()
    with sqlite3.connect("users.db") as db:
        cr=db.cursor()
        cr.execute(f"update Cust set Password ='{pass0}' Where User_ID={ID}")
    time.sleep(1)    
######################################################################################################################################################
def updateNum():
    num0=newNum.get()
    with sqlite3.connect("users.db") as db:
        cr=db.cursor()
        cr.execute(f"update Cust set Phone ='{num0}' Where User_ID={ID}")
    time.sleep(1)    

######################################################################################################################################################
def updateAdd():
    add0=new_address.get()
    with sqlite3.connect("users.db") as db:
        cr=db.cursor()
        cr.execute(f"update Cust set Address ='{add0}' Where User_ID={ID}")
    time.sleep(1)    
####################################################################################################################################################
def Userinfo():
    if Logged==True:
        U=Toplevel()
        U.configure(background='orange')
        U.title("User's info")
        U.geometry("720x500+0+0")
        Label(U, text="Signed up Users\n\n",fg="white",font=('arial',30,'bold'),justify="center", bg="orange").pack(side=TOP)
        cs.execute(f"select * from Cust WHERE User_ID={ID}")
        user= cs.fetchall()
        userInfo = user[0]
        Label(U,font=('arial',30,'bold'),text=f"User ID: {userInfo[0]}",bg='orange',fg='black',justify=CENTER).pack(side=TOP)
        
        Label(U,font=('arial',30,'bold'),text=f"Username: {userInfo[1]}",bg='orange',fg='black',justify=CENTER).pack(side=TOP)

        Label(U,font=('arial',30,'bold'),text=f"Password: {userInfo[2]}",bg='orange',fg='black',justify=CENTER).pack(side=TOP)

        Label(U,font=('arial',30,'bold'),text=f"Phone: {userInfo[3]}",bg='orange',fg='black',justify=CENTER).pack(side=TOP)

        Label(U,font=('arial',30,'bold'),text=f"Address: {userInfo[4]}",bg='orange',fg='black',justify=CENTER).pack(side=TOP)
        
        Button(U,bd=0, text="Close",font=('arial',20,'bold'), width=10, height=1, bg="orange",command=lambda : U.destroy()).place(x=520,y=420)           
    else:
        tkinter.messagebox.showerror(title="Caution",message="Log in First")    
##########################################################        PAGE2       ######################################################################
def page2():

    global win2
    win2 = Toplevel()
    
    
    
    win2.geometry("1350x750+0+0")
    win2.title("Menu")
    win2.configure(background='orange')



    lblTitle=Label(win2,font=('arial',60,'bold'),text='Ωmega\'s Menu',bg='orange',
                        fg='white',justify=CENTER)
    lblTitle.pack(side=TOP)

    MenuFrame = Frame(win2,bg='orange',bd=5,relief=RIDGE)
    MenuFrame.pack(side=LEFT)
    Cost_F=Frame(MenuFrame,bg='orange',bd=4)
    Cost_F.pack(side=BOTTOM)

    ReceiptCal_F = Frame(win2,bg='orange',bd=5,relief=RIDGE)
    ReceiptCal_F.pack(side=LEFT)

    Buttons_F=Frame(ReceiptCal_F,bg='orange',bd=3,relief=RIDGE)
    Buttons_F.pack(side=BOTTOM)

    Receipt_F=Frame(ReceiptCal_F,bg='orange',bd=4,relief=RIDGE)
    Receipt_F.pack(side=BOTTOM)

    Drinks_F=Frame(MenuFrame,bg='orange',bd=4,relief=RIDGE)
    Drinks_F.pack(side=LEFT)
    Food_F=Frame(MenuFrame,bg='orange',bd=4,relief=RIDGE)
    Food_F.pack(side=RIGHT)


    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5=IntVar()
    var6=IntVar()
    var7=IntVar()
    var8=IntVar()
    var9=IntVar()
    var10=IntVar()
    var11=IntVar()
    var12=IntVar()
    
    DateofOrder = StringVar()
    Receipt_Ref = StringVar()
    PaidTax = StringVar()
    SubTotal = StringVar()
    TotalCost = StringVar()
    CostofFood = StringVar()
    CostofDrinks = StringVar()


    E_Sprite = StringVar()
    E_Pepsi = StringVar()
    E_DietCoke = StringVar()
    E_Cappuccino = StringVar()
    E_Fanta = StringVar()
    E_CocaCola = StringVar()
    E_HotDog = StringVar()
    E_Pasta = StringVar()
    E_HamBurger = StringVar()
    E_Sandwich = StringVar()
    E_Fries = StringVar()
    E_Spagetti = StringVar()
    
    E_Sprite.set("0")
    E_Pepsi.set("0")
    E_DietCoke.set("0")
    E_Cappuccino.set("0")
    E_Fanta.set("0")
    E_CocaCola.set("0")
    E_HotDog.set("0")
    E_Pasta.set("0")
    E_HamBurger.set("0")
    E_Sandwich.set("0")
    E_Fries.set("0")
    E_Spagetti.set("0")


    DateofOrder.set(time.strftime("%d/%m/%y"))
    ##########################################Function Declaration####################################################
    def Reset():
        PaidTax.set("")
        SubTotal.set("")
        TotalCost.set("")
        CostofFood.set("")
        CostofDrinks.set("")
        txtReceipt.delete("1.0",END)

        E_Sprite.set("0")
        E_Pepsi.set("0")
        E_DietCoke.set("0")        
        E_Cappuccino.set("0")
        E_Fanta.set("0")
        E_CocaCola.set("0")        
        E_HotDog.set("0")        
        E_Pasta.set("0")
        E_HamBurger.set("0")
        E_Sandwich.set("0")
        E_Fries.set("0")
        E_Spagetti.set("0")
        
        
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        

        txtSprite.configure(state=DISABLED)
        txtPepsi.configure(state=DISABLED)
        txtDietCoke.configure(state=DISABLED)        
        txtCappuccino.configure(state=DISABLED)
        txtFanta.configure(state=DISABLED)
        txtCocaCola.configure(state=DISABLED)        
        txtHotDog.configure(state=DISABLED)        
        txtPasta.configure(state=DISABLED)
        txtHamBurger.configure(state=DISABLED)
        txtSandwich.configure(state=DISABLED)
        txtFries.configure(state=DISABLED)
        txtSpagetti.configure(state=DISABLED)
        
            

    def CostofItem():
        Item1=float(E_Sprite.get())
        Item2=float(E_Pepsi.get())
        Item3=float(E_DietCoke.get())
        Item4=float(E_Cappuccino.get())
        Item5=float(E_Fanta.get())
        Item6=float(E_CocaCola.get())
        Item7=float(E_HotDog.get())
        Item8=float(E_Pasta.get())
        Item9=float(E_HamBurger.get())
        Item10=float(E_Sandwich.get())
        Item11=float(E_Fries.get())
        Item12=float(E_Spagetti.get())

        PriceofDrinks =(Item1 * 2) + (Item2 * 2) + (Item3 * 1)  + (Item4 * 1) + (Item5 * 1) + (Item6 * 1)
        PriceofFood =(Item7 * 5)  + (Item8 * 5) + (Item9 * 5) + (Item10 * 2) + (Item11 * 4) + (Item12 * 2) 

        DrinksPrice = "$" + str('%.2f'%(PriceofDrinks))
        FoodPrice =  "$" + str('%.2f'%(PriceofFood))
        CostofFood.set(FoodPrice)
        CostofDrinks.set(DrinksPrice)

        SubTotalofITEMS = "$" + str('%.2f'%(PriceofDrinks + PriceofFood))
        SubTotal.set(SubTotalofITEMS)

        Tax = "$" + str('%.2f'%((PriceofDrinks + PriceofFood) * 0.15))
        PaidTax.set(Tax)

        TT=((PriceofDrinks + PriceofFood) * 0.15)
        TC="$" + str('%.2f'%(PriceofDrinks + PriceofFood + TT))
        TotalCost.set(TC)


    def chkSprite():
        if(var1.get() == 1):
            txtSprite.configure(state = NORMAL)
            txtSprite.focus()
            txtSprite.delete('0',END)
            E_Sprite.set("")
        elif(var1.get() == 0):
            txtSprite.configure(state = DISABLED)
            E_Sprite.set("0")

    def chkPepsi():
        if(var2.get() == 1):
            txtPepsi.configure(state = NORMAL)
            txtPepsi.focus()
            txtPepsi.delete('0',END)
            E_Pepsi.set("")
        elif(var2.get() == 0):
            txtPepsi.configure(state = DISABLED)
            E_Pepsi.set("0")

    def chk_DietCoke():
        if(var3.get() == 1):
            txtDietCoke.configure(state = NORMAL)
            txtDietCoke.delete('0',END)
            txtDietCoke.focus()
        elif(var3.get() == 0):
            txtDietCoke.configure(state = DISABLED)
            E_DietCoke.set("0")


    def chk_Cappuccino():
        if(var4.get() == 1):
            txtCappuccino.configure(state = NORMAL)
            txtCappuccino.delete('0',END)
            txtCappuccino.focus()
        elif(var4.get() == 0):
            txtCappuccino.configure(state = DISABLED)
            E_Cappuccino.set("0")

    def chk_Fanta():
        if(var5.get() == 1):
            txtFanta.configure(state = NORMAL)
            txtFanta.delete('0',END)
            txtFanta.focus()
        elif(var5.get() == 0):
            txtFanta.configure(state = DISABLED)
            E_Fanta.set("0")

    def chk_CocaCola():
        if(var6.get() == 1):
            txtCocaCola.configure(state = NORMAL)
            txtCocaCola.delete('0',END)
            txtCocaCola.focus()
        elif(var6.get() == 0):
            txtCocaCola.configure(state = DISABLED)
            E_CocaCola.set("0")



    def chk_HotDog():
        if(var7.get() == 1):
            txtHotDog.configure(state = NORMAL)
            txtHotDog.delete('0',END)
            txtHotDog.focus()
        elif(var7.get() == 0):
            txtHotDog.configure(state = DISABLED)
            E_HotDog.set("0")



    def chk_Pasta():
        if(var8.get() == 1):
            txtPasta.configure(state = NORMAL)
            txtPasta.delete('0',END)
            txtPasta.focus()
        elif(var8.get() == 0):
            txtPasta.configure(state = DISABLED)
            E_Pasta.set("0")

    def chk_HamBurger():
        if(var9.get() == 1):
            txtHamBurger.configure(state = NORMAL)
            txtHamBurger.delete('0',END)
            txtHamBurger.focus()
        elif(var9.get() == 0):
            txtHamBurger.configure(state = DISABLED)
            E_HamBurger.set("0")

    def chk_Sandwich():
        if(var10.get() == 1):
            txtSandwich.configure(state = NORMAL)
            txtSandwich.delete('0',END)
            txtSandwich.focus()
        elif(var10.get() == 0):
            txtSandwich.configure(state = DISABLED)
            E_Sandwich.set("0")

    def chk_Fries():
        if(var11.get() == 1):
            txtFries.configure(state = NORMAL)
            txtFries.delete('0',END)
            txtFries.focus()
        elif(var11.get() == 0):
            txtFries.configure(state = DISABLED)
            E_Fries.set("0")

    def chk_Spagetti():
        if(var12.get() == 1):
            txtSpagetti.configure(state = NORMAL)
            txtSpagetti.delete('0',END)
            txtSpagetti.focus()
        elif(var12.get() == 0):
            txtSpagetti.configure(state = DISABLED)
            E_Spagetti.set("0")



    def Receipt():
        txtReceipt.delete("1.0",END)
        x=random.randint(10908,500876)
        randomRef= str(x)
        Receipt_Ref.set("Bill "+ randomRef)
        txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() +'\t'+ DateofOrder.get() +'\n')
        txtReceipt.insert(END,'Items\t\t\t\t'+"number of Items \n")
        txtReceipt.insert(END,'Sprite:\t\t\t\t\t' + E_Sprite.get() +'\n')
        txtReceipt.insert(END,'Pepsi:\t\t\t\t\t'+ E_Pepsi.get()+'\n')
        txtReceipt.insert(END,'DietCoke:\t\t\t\t\t'+ E_DietCoke.get()+'\n')
        txtReceipt.insert(END,'Cappuccino:\t\t\t\t\t'+ E_Cappuccino.get()+'\n')
        txtReceipt.insert(END,'Fanta:\t\t\t\t\t'+ E_Fanta.get()+'\n')
        txtReceipt.insert(END,'CocaCola:\t\t\t\t\t'+ E_CocaCola.get()+'\n')
        txtReceipt.insert(END,'HotDog:\t\t\t\t\t'+ E_HotDog.get()+'\n')
        txtReceipt.insert(END,'Pasta:\t\t\t\t\t'+ E_Pasta.get()+'\n')
        txtReceipt.insert(END,'HamBurger:\t\t\t\t\t'+ E_HamBurger.get()+'\n')
        txtReceipt.insert(END,'Sandwich:\t\t\t\t\t'+ E_Sandwich.get()+'\n')
        txtReceipt.insert(END,'Fries:\t\t\t\t\t'+ E_Fries.get()+'\n')
        txtReceipt.insert(END,'Spagetti:\t\t\t\t\t'+ E_Spagetti.get()+'\n')
        txtReceipt.insert(END,'Cost of Drinks:\t\t\t\t\t'+ CostofDrinks.get()+'\nCost of Foods:\t\t\t\t\t'+ CostofFood.get()+"\n")
        txtReceipt.insert(END,'Tax Paid:\t\t\t\t\t'+PaidTax.get()+'\nSubTotal:\t\t\t\t\t'+str(SubTotal.get())+"\n")
        txtReceipt.insert(END,'Total:\t\t\t\t\t'+ TotalCost.get())
    
        if Logged==True:
            cs.execute(f"select * from Cust WHERE User_ID={ID}")
            INFO = cs.fetchall()
            txtReceipt.insert(END,'\nCustomer\'s info:\n')
            for i in INFO:
                txtReceipt.insert(END,'Name: \t\t\t\t'+i[1]+'\n')
                txtReceipt.insert(END,'Phone: \t\t\t\t'+i[3]+'\n')
                txtReceipt.insert(END,'Address: \t\t\t\t'+i[4])
            
                 
    Checkbutton(Drinks_F,text='Sprite',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='orange',command=chkSprite).grid(row=0,sticky=W)
    Checkbutton(Drinks_F,text='Pepsi',variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='orange',command=chkPepsi).grid(row=1,sticky=W)
    Checkbutton(Drinks_F,text='DietCoke',variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='orange',command=chk_DietCoke).grid(row=2,sticky=W)
    Checkbutton(Drinks_F,text='Cappuccino',variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='orange',command=chk_Cappuccino).grid(row=4,sticky=W)
    Checkbutton(Drinks_F,text='Fanta',variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='orange',command=chk_Fanta).grid(row=5,sticky=W)
    Checkbutton(Drinks_F,text='CocaCola',variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),bg='orange',command=chk_CocaCola).grid(row=6,sticky=W)

    txtSprite = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_Sprite)
    txtSprite.grid(row=0,column=1)

    txtPepsi = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_Pepsi)
    txtPepsi.grid(row=1,column=1)

    txtDietCoke = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_DietCoke)
    txtDietCoke.grid(row=2,column=1)


    txtCappuccino = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED ,textvariable=E_Cappuccino)
    txtCappuccino.grid(row=4,column=1)

    txtFanta = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_Fanta)
    txtFanta.grid(row=5,column=1)

    txtCocaCola = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_CocaCola)
    txtCocaCola.grid(row=6,column=1)


    Checkbutton(Food_F,text="HotDog\t\t\t ",variable=var7,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='orange',command=chk_HotDog).grid(row=0,sticky=W)
    Checkbutton(Food_F,text="Pasta ",variable=var8,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='orange',command=chk_Pasta).grid(row=2,sticky=W)
    Checkbutton(Food_F,text="Burger ",variable=var9,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='orange',command=chk_HamBurger).grid(row=3,sticky=W)
    Checkbutton(Food_F,text="Sandwich ",variable=var10,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='orange',command=chk_Sandwich).grid(row=4,sticky=W)
    Checkbutton(Food_F,text="Fries ",variable=var11,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='orange',command=chk_Fries).grid(row=5,sticky=W)
    Checkbutton(Food_F,text="Spagetti ",variable=var12,onvalue = 1, offvalue=0,font=('arial',16,'bold'),bg='orange',command=chk_Spagetti).grid(row=6,sticky=W)

    txtHotDog=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_HotDog)
    txtHotDog.grid(row=0,column=1)


    txtPasta=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_Pasta)
    txtPasta.grid(row=2,column=1)

    txtHamBurger=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_HamBurger)
    txtHamBurger.grid(row=3,column=1)

    txtSandwich=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_Sandwich)
    txtSandwich.grid(row=4,column=1)

    txtFries=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=E_Fries)
    txtFries.grid(row=5,column=1)

    txtSpagetti=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                      ,textvariable=E_Spagetti)
    txtSpagetti.grid(row=6,column=1)


    lblCostofDrinks=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Drinks\t',bg='orange',
                    fg='black',justify=CENTER)
    lblCostofDrinks.grid(row=0,column=0,sticky=W)
    txtCostofDrinks=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                            insertwidth=2,justify=RIGHT,textvariable=CostofDrinks)
    txtCostofDrinks.grid(row=0,column=1)

    lblCostofFood=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Foods',bg='orange',
                    fg='black',justify=CENTER)
    lblCostofFood.grid(row=1,column=0,sticky=W)
    txtCostofFood=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                            insertwidth=2,justify=RIGHT,textvariable=CostofFood)
    txtCostofFood.grid(row=1,column=1)


    lblPaidTax=Label(Cost_F,font=('arial',14,'bold'),text='\tPaid Tax',bg='orange',bd=7,
                    fg='black',justify=CENTER)
    lblPaidTax.grid(row=0,column=2,sticky=W)
    txtPaidTax=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                            insertwidth=2,justify=RIGHT,textvariable=PaidTax)
    txtPaidTax.grid(row=0,column=3)

    lblSubTotal=Label(Cost_F,font=('arial',14,'bold'),text='\tSub Total',bg='orange',bd=7,
                    fg='black',justify=CENTER)
    lblSubTotal.grid(row=1,column=2,sticky=W)
    txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                            insertwidth=2,justify=RIGHT,textvariable=SubTotal)
    txtSubTotal.grid(row=1,column=3)

    lblTotalCost=Label(Cost_F,font=('arial',14,'bold'),text='\tTotal',bg='orange',bd=7,
                    fg='black',justify=CENTER)
    lblTotalCost.grid(row=2,column=2,sticky=W)
    txtTotalCost=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                            insertwidth=2,justify=RIGHT,textvariable=TotalCost)
    txtTotalCost.grid(row=2,column=3)

    txtReceipt=Text(Receipt_F,width=46,height=17.5,bg='white',bd=4,font=('arial',12,'bold'))
    txtReceipt.grid(row=0,column=0)


    Button(Buttons_F,padx=19,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Total',
                            bg='orange',command=CostofItem).grid(row=0,column=0)
    Button(Buttons_F,padx=18,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Receipt',
                            bg='orange',command=Receipt).grid(row=0,column=1)
    Button(Buttons_F,padx=18,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Reset',
                            bg='orange',command=Reset).grid(row=0,column=2)
    Button(Buttons_F,padx=18,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Close',
                            bg='orange',command=lambda:win2.destroy()).grid(row=0,column=3)
#################################################################    Page3   ###########################################################################
def page3():
    win3=Toplevel()
    win3.title("credits")
    win3.geometry("1350x760+0+0")
    win3.configure(background='orange')
    Label(win3,font=('arial',60,'bold'),text='Credits\n',bg='orange',fg='white',justify=CENTER).pack(side=TOP)
    Label(win3,font=('arial',30,'bold'),text='Moaz Ahmed\n',bg='orange',fg='black',justify=CENTER).pack(side=TOP)
    Label(win3,font=('arial',30,'bold'),text='Mohamed Ashraf\n',bg='orange',fg='black',justify=CENTER).pack(side=TOP)
    Label(win3,font=('arial',30,'bold'),text='Karim Hussien \n',bg='orange',fg='black',justify=CENTER).pack(side=TOP)
    Label(win3,font=('arial',30,'bold'),text='Abdallah Tarek\n',bg='orange',fg='black',justify=CENTER).pack(side=TOP)
    Label(win3,font=('arial',30,'bold'),text='Youssef Mohamed\n',bg='orange',fg='black',justify=CENTER).pack(side=TOP)
    Label(win3,font=('arial',30,'bold'),text='Mohamed Ibrahim\n',bg='orange',fg='black',justify=CENTER).pack(side=TOP)
    
    Button(win3,text="Back",bd=0,fg="black",bg="orange",font=('arial',30,'bold'),pady=10,relief=GROOVE,command=lambda: win3.destroy()).place(x=1200,y=650)
######################################################################################################################################################     
#but4 For closing app
def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Restaurant System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return
######################################################################################################################################################

root=Tk()
root.title("Main Menu")
root.geometry("1350x750+0+0")
root.configure(background='orange')
PageFrame=Frame(root,bg='orange',bd=200,pady=300,relief=GROOVE).pack(fill=X)

lblTitle=Label(PageFrame,font=('arial',60,'bold'),text='Welcome To Ωmega',bd=20,bg="orange",fg='white',justify=CENTER)
lblTitle.pack(side=TOP)

Button(PageFrame,text="Login Or Singup",bd=0,fg="black",bg="orange",font=('arial',35,'bold'),pady=10,command=page1).pack(side=TOP)

Button(PageFrame,text="Order Now",bd=0,fg="black",bg="orange",font=('arial',35,'bold'),pady=10,command=page2).pack(side=TOP)
Button(PageFrame,text="Update Info",bd=0,fg="black",bg="orange",font=('arial',20,'bold'),pady=10,command=update).place(x=1170,y=650)
Button(PageFrame,text="User's info",bd=0,fg="black",bg="orange",font=('arial',20,'bold'),pady=10,command=Userinfo).place(x=1000,y=650)
Button(PageFrame,text="Credits",bd=0,fg="black",bg="orange",font=('arial',35,'bold'),pady=10,command=page3).pack(side=TOP)
Button(PageFrame,text="Quit App",bd=0,fg="black",bg="orange",font=('arial',35,'bold'),pady=10,command=iExit).pack(side=TOP)

root.mainloop()
