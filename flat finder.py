from Tkinter import *
from tkMessageBox import *
import sqlite3
root1=Tk()
root1.title("Flat Finder")
kl=PhotoImage(file="front.gif")
Label(root1,image=kl).grid(row=0,column=0,rowspan=20,columnspan=20)


Label(root1,text='Garvit Kukreja' ,font='timesnewroman 20 italic').grid(row=0)
Label(root1,text='151292',font='timesnewroman 20 italic').grid(row=1)
Label(root1,text='C.S.E.',font='timesnewroman 20 italic').grid(row=2)
Label(root1,text='B3',font='timesnewroman 20 italic').grid(row=3)
Label(root1,text='garvitkukreja21@gmail.com',font='timesnewroman 20 italic').grid(row=4)
Label(root1,text='+917500024007',font='timesnewroman 20 italic').grid(row=5)
Label(root1,text='Find Flats On Rent',font='timesnewroman 20 italic').grid(row=6)
def cont():
    root1.destroy()
    root=Tk()
    
    root.geometry("1366x768")
    try:
        con=sqlite3.Connection("jk")
    except:
        pass
    cur=con.cursor()
    garvit=PhotoImage(file='app.gif')
    garvit1=Label(root,image=garvit)
    garvit1.grid(row=0,column=0,rowspan=20,columnspan=20)
    cur.execute("create table if not exists flat(Bhk varchar(10) ,fno varchar(10),Appartment varchar(30),Locality varchar(30),city varchar(20),oname varchar(30),Mno number)")
    root.title("FLATS ON RENT")
    Label(root,text="SELECT YOUR CITY:",font="Aerial 40 bold italic",bg='Yellow').grid(row=1,column=5,sticky='w')
    m=[("2 BHK",'Flat no 26','Friends Ashiana','Monikonda','Hyderabad','Ali',9998885552),("3 BHK",'Flat no 10','Vertex Home','Nallan Gandla','Hyderabad','Ramesh',9459835552),("4 BHK",'Flat no 46','Vertex Home','Nallan Gandla','Hyderabad','Ramesh',9459835552),("1 BHK",'Flat no 6','Sanktis Phase 1','Miyapur','Hyderabad','Ansari',75289552879),("1 BHK",'Flat no 46','Sanktis phase 2','Abias','Hyderabad','Arjun Sarawat',8794458562)]
    cur.executemany("insert into flat values(?,?,?,?,?,?,?)",m)
    b=[("1 BHK",'Flat no 25','Vinayak Lifestyle','Raysan','Gandhinagar','Jethalal',9454446552),("4 BHK",'Flat no 34','Pramukh Pacific','Sargasan','Gandhinagar','Jignesh',7797446552),("3 BHK",'Flat no 16','Dolphin Housing','Raysan','Gandhinagar','Rupesh',7458796552),("2 BHK",'Flat no 11','Surya','Chandkheda','Gandhinagar','Jethalal',94544465456)]
    cur.executemany("insert into flat values(?,?,?,?,?,?,?)",b)
    c=[("2 BHK",'Flat no 1','Arctic park east','Sector 21','Chandigarh','Gaurav Gaba',789446552),("2 BHK",'Flat no 50','Omaxe','Sector 5','Chandigarh','Ramesh jhamb',789446589),("1 BHK",'Flat no 45','Swastic 1 ','Sector 17','Chandigarh','Varun Grewal ',889446552),("2 BHK",'Flat no 31','Golden Sand','Sector 19','Chandigarh','Ramesh Oberoi ',789245552)]
    cur.executemany("insert into flat values(?,?,?,?,?,?,?)",c)
    d=[("1 BHK",'Flat no 5','Arctic Flats 1','Naseem Bagh','Shrinagar','A.K.Sharma',8558213552),("2 BHK",'Flat no 16','Arctic Flats 2 ','Badami Bagh','Shrinagar','Shyam lal',7158213552)]
    cur.executemany("insert into flat values(?,?,?,?,?,?,?)",d)
    e=[("1 BHK",'Flat no 2','Swastic Appartment','Indra Nagar','Banglore','R.Kumar',7153246572),("2 BHK",'Flat no 16','Vertix Phase 1 ','Devanahalli','Banglore','Apporv',7668246572),("3 BHK",'Flat no 2','Swastic Appartment','Indra Nagar','Banglore','R.Kumar',7153246572),("1 BHK",'Flat no 25','Vertex Phase 2','Besavangudi','Banglore','Parth',7153246123),("4 BHK",'Flat no 21','Brook Field','Hennur Rode','Banglore','R.Kumar',7553786572)]
    cur.executemany("insert into flat values(?,?,?,?,?,?,?)",e)
    f=[("2 BHK",'Flat no 2','Nikhil Homes Phase 1','Arera Colony','Bhopal','Kailash',8532146552),("3 BHK",'Flat no 8','Imperial City','Nayapura','Bhopal','Usman',8238946552),("1 BHK",'Flat no 16','Nikhil Homes Phase 2','Ashoka Garden','Bhopal','Saif',7832146552),("4 BHK",'Flat no 32','Coral Casa','Vijay Nagar','Bhopal','Pramendra',8556946552)]
    cur.executemany("insert into flat values(?,?,?,?,?,?,?)",f)
    g=[("3 BHK",'Flat no 105','Ashiana Palm','G.K.1','Delhi','Kabir Mehra',8256976342),("2 BHK",'Flat no 206','Puru Appartments','Rohini Sector 13','Delhi','Angad Sachdeva',8656196342),("1 BHK",'Flat no 15','Imperial Appartments','G.K.2','Delhi','Ashish Oberoi',8123976342),("2 BHK",'Flat no 6','Sunrise Appartments','Malviya Nagar','Delhi','Amman Ali',9356976342),("4 BHK",'Flat no 505','The Golden Ring','Dwarka East','Delhi','Firoz Agarwal',9556976342)]
    cur.executemany("insert into flat values(?,?,?,?,?,?,?)",g)
    h=[("1 BHK",'Flat no 25','Parkville','Malad','Mumbai','Bilal Syed',7632496782),("2 BHK",'Flat no 602','Vivan Appartments','Andheri East','Mumbai','Rishi Kumar',7532246782),("3 BHK",'Flat no 703','Surya Lifestyle','Bandra west','Mumbai','Ramesh Sippe',9832346782),("4 BHK",'Flat no 265','Morya Heights','Andheri East','Mumbai','Sunil Kumar',8932496782)]
    cur.executemany("insert into flat values(?,?,?,?,?,?,?)",h)
    i=[("1 BHK",'Flat no 16','Anukampa Platina','Malviya Nagar','Jaipur','Vikrat Khirwar',8759366552),("2 BHK",'Flat no 19','Ruby Imperial','Jagatpura','Jaipur','Ajay Mehra',8759389562),("3 BHK",'Flat no 28','Trimurti Appartments','Vaishali Nagar','Jaipur','Ajeet Kumar',7159389562)]
    cur.executemany("insert into flat values(?,?,?,?,?,?,?)",i)
    j=[("1 BHK",'Flat no 25','Adroit Altius','Anna Nagar','Chennai','Dhanush',8154366342),("2 BHK",'Flat no 65','Landmark Tiwali','Mennambakkam','Chennai','Avik Robinson',8554324342),("3 BHK",'Flat no 25','Adroit Altius','Anna Nagar','Chennai','M.G.Ramachandranan',8359766342)]
    cur.executemany("insert into flat values(?,?,?,?,?,?,?)",j)
    k=[("1 BHK",'Flat no 32','Vineet Khand','Gomti Nagar','Lucknow','Anuj Mohan',8356846552),("2 BHK",'Flat no 52','Alknanda Appartments','Hazratganj','Lucknow','Aditya Jhaa',8356847892),("3 BHK",'Flat no 12','Greenwood ','Mahanagar','Lucknow','Prakash Kumar',7556846552),("4 BHK",'Flat no 45','Jyoti Kunj Appartment','Indra Nagar','Lucknow','Shashwat Singh',9556218552)]
    cur.executemany("insert into flat values(?,?,?,?,?,?,?)",k)
    l=[("1 BHK",'Flat no 15','Sunrise Tower','','Kolkata','Byomkesh',8352786552),("2 BHK",'Flat no 1','Hiland Park','','Kolkata','Momita Chatterjee',8352786127)]
    cur.executemany("insert into flat values(?,?,?,?,?,?,?)",l)
    a=IntVar()
    Radiobutton(root,text='HYDERABAD',variable=a,value=1,font="Aerial 20 bold italic").grid(row=2,column=0,sticky='w')
    Radiobutton(root,text='GANDHINAGAR',variable=a,value=2,font="Aerial 20 bold italic").grid(row=3,column=0,sticky='w')
    Radiobutton(root,text='CHANDIGARH',variable=a,value=3,font="Aerial 20 bold italic").grid(row=4,column=0,sticky='w')
    Radiobutton(root,text='SHRINAGAR',variable=a,value=4,font="Aerial 20 bold italic").grid(row=5,column=0,sticky='w')
    Radiobutton(root,text='BANGLORE',variable=a,value=5,font="Aerial 20 bold italic").grid(row=6,column=0,sticky='w')
    Radiobutton(root,text='BHOPAL',variable=a,value=6,font="Aerial 20 bold italic").grid(row=7,column=0,sticky='w')
    Radiobutton(root,text='DELHI',variable=a,value=7,font="Aerial 20 bold italic").grid(row=2,column=9,sticky='w')
    Radiobutton(root,text='MUMBAI',variable=a,value=8,font="Aerial 20 bold italic").grid(row=3,column=9,sticky='w')
    Radiobutton(root,text='JAIPUR',variable=a,value=9,font="Aerial 20 bold italic").grid(row=4,column=9,sticky='w')
    Radiobutton(root,text='CHENNAI',variable=a,value=10,font="Aerial 20 bold italic").grid(row=5,column=9,sticky='w')
    Radiobutton(root,text='LUCKNOW',variable=a,value=11,font="Aerial 20 bold italic").grid(row=6,column=9,sticky='w')
    Radiobutton(root,text='KOLKATA',variable=a,value=12,font="Aerial 20 bold italic").grid(row=7,column=9,sticky='w')

    
    def city():
        if a.get()==1:
            root.destroy()
            root2=Tk()
            root2.title("Hyderabad")
            t=PhotoImage(file="hyd.gif")
            Label(root2,image=t).grid(row=0,column=0,rowspan=20,columnspan=20)
            cur.execute("select * from flat where city='Hyderabad'")
            
            
            z=cur.fetchall()
            i=0
            for y in z:
                
                Label(root2, text=str(y)).grid(row=i,column=0)#print y
                i+=1  
                #showinfo('Hyderabad',y)
            def exit1():
                root2.destroy()
                
            Button(root2,text="exit",command=exit1).grid(row=10,column=0)
            root2.mainloop()
            
        elif a.get()==2:
            root.destroy()
            root2=Tk()
            root2.title("Gandhinagar")
            t=PhotoImage(file="gan.gif")
            Label(root2,image=t).grid(row=0,column=0,rowspan=20,columnspan=20)
            cur.execute("select * from flat where city='Gandhinagar'")
            
            
            z=cur.fetchall()
            i=0
            for y in z:
                
                Label(root2, text=str(y)).grid(row=i,column=0)#print y
                i+=1  
                #showinfo('Hyderabad',y)
            def exit1():
                root2.destroy()
                
            Button(root2,text="exit",command=exit1).grid(row=10,column=0)
            root2.mainloop()
        elif a.get()==3:
            root.destroy()
            root2=Tk()
            root2.title("Chandigarh")
            t=PhotoImage(file="chan.gif")
            Label(root2,image=t).grid(row=0,column=0,rowspan=20,columnspan=20)
            cur.execute("select * from flat where city='Chandigarh'")
            
            
            z=cur.fetchall()
            i=0
            for y in z:
                
                Label(root2, text=str(y)).grid(row=i,column=0)#print y
                i+=1  
                #showinfo('Hyderabad',y)
            def exit1():
                root2.destroy()
                
            Button(root2,text="exit",command=exit1).grid(row=10,column=0)
            root2.mainloop()

        elif a.get()==4:
            root.destroy()
            root2=Tk()
            root2.title("Shrinagar")
            t=PhotoImage(file="srinagar.gif")
            Label(root2,image=t).grid(row=0,column=0,rowspan=20,columnspan=20)
            cur.execute("select * from flat where city='Shrinagar'")
            
            
            z=cur.fetchall()
            i=0
            for y in z:
                
                Label(root2, text=str(y)).grid(row=i,column=0)#print y
                i+=1  
                #showinfo('Hyderabad',y)
            def exit1():
                root2.destroy()
                
            Button(root2,text="exit",command=exit1).grid(row=10,column=0)
            root2.mainloop()
        elif a.get()==5:

            root.destroy()
            root2=Tk()
            root2.title("Banglore")
            t=PhotoImage(file="ban.gif")
            Label(root2,image=t).grid(row=0,column=0,rowspan=20,columnspan=20)
            cur.execute("select * from flat where city='Banglore'")
            
            
            z=cur.fetchall()
            i=0
            for y in z:
                
                Label(root2, text=str(y)).grid(row=i,column=0)#print y
                i+=1  
                #showinfo('Hyderabad',y)
            def exit1():
                root2.destroy()
                
            Button(root2,text="exit",command=exit1).grid(row=10,column=0)
            root2.mainloop()

        elif a.get()==6:

            root.destroy()
            root2=Tk()
            root2.title("Bhopal")
            t=PhotoImage(file="bhopal.gif")
            Label(root2,image=t).grid(row=0,column=0,rowspan=20,columnspan=20)
            cur.execute("select * from flat where city='Bhopal'")
            
            
            z=cur.fetchall()
            i=0
            for y in z:
                
                Label(root2, text=str(y)).grid(row=i,column=0)#print y
                i+=1  
                #showinfo('Hyderabad',y)
            def exit1():
                root2.destroy()
                
            Button(root2,text="exit",command=exit1).grid(row=10,column=0)
            root2.mainloop()
        elif a.get()==7:
            root.destroy()
            root2=Tk()
            root2.title("Delhi")
            t=PhotoImage(file="del.gif")
            Label(root2,image=t).grid(row=0,column=0,rowspan=20,columnspan=20)
            cur.execute("select * from flat where city='Delhi'")
            
            
            z=cur.fetchall()
            i=0
            for y in z:
                
                Label(root2, text=str(y)).grid(row=i,column=0)#print y
                i+=1  
                #showinfo('Hyderabad',y)
            def exit1():
                root2.destroy()
                
            Button(root2,text="exit",command=exit1).grid(row=10,column=0)
            root2.mainloop()
        elif a.get()==8:
            root.destroy()
            root2=Tk()
            root2.title("Mumbai")
            t=PhotoImage(file="mumbai.gif")
            Label(root2,image=t).grid(row=0,column=0,rowspan=20,columnspan=20)
            cur.execute("select * from flat where city='Mumbai'")
            
            
            z=cur.fetchall()
            i=0
            for y in z:
                
                Label(root2, text=str(y)).grid(row=i,column=0)#print y
                i+=1  
                #showinfo('Hyderabad',y)
            def exit1():
                root2.destroy()
                
            Button(root2,text="exit",command=exit1).grid(row=10,column=0)
            root2.mainloop()
        elif a.get()==9:
            root.destroy()
            root2=Tk()
            root2.title("Jaipur")
            t=PhotoImage(file="jai.gif")
            Label(root2,image=t).grid(row=0,column=0,rowspan=20,columnspan=20)
            cur.execute("select * from flat where city='Jaipur'")
            
            
            z=cur.fetchall()
            i=0
            for y in z:
                
                Label(root2, text=str(y)).grid(row=i,column=0)#print y
                i+=1  
                #showinfo('Hyderabad',y)
            def exit1():
                root2.destroy()
                
            Button(root2,text="exit",command=exit1).grid(row=10,column=0)
            root2.mainloop()
        elif a.get()==10:
            root.destroy()
            root2=Tk()
            root2.title("Chennai")
            t=PhotoImage(file="chennai.gif")
            Label(root2,image=t).grid(row=0,column=0,rowspan=20,columnspan=20)
            cur.execute("select * from flat where city='Chennai'")
            
            
            z=cur.fetchall()
            i=0
            for y in z:
                
                Label(root2, text=str(y)).grid(row=i,column=0)#print y
                i+=1  
                #showinfo('Hyderabad',y)
            def exit1():
                root2.destroy()
                
            Button(root2,text="exit",command=exit1).grid(row=10,column=0)
            root2.mainloop()
        elif a.get()==11:
            root.destroy()
            root2=Tk()
            root2.title("Lucknow")
            t=PhotoImage(file="lucknow.gif")
            Label(root2,image=t).grid(row=0,column=0,rowspan=20,columnspan=20)
            cur.execute("select * from flat where city='Lucknow'")
            
            
            z=cur.fetchall()
            i=0
            for y in z:
                
                Label(root2, text=str(y)).grid(row=i,column=0)#print y
                i+=1  
                #showinfo('Hyderabad',y)
            def exit1():
                root2.destroy()
                
            Button(root2,text="exit",command=exit1).grid(row=10,column=0)
            root2.mainloop()
        elif a.get()==12:
            root.destroy()
            root2=Tk()
            root2.title("Kolkata")
            t=PhotoImage(file="kolkata.gif")
            Label(root2,image=t).grid(row=0,column=0,rowspan=20,columnspan=20)
            cur.execute("select * from flat where city='Kolkata'")
            
            
            z=cur.fetchall()
            i=0
            for y in z:
                
                Label(root2, text=str(y)).grid(row=i,column=0)#print y
                i+=1  
                #showinfo('Hyderabad',y)
            def exit1():
                root2.destroy()
                
            Button(root2,text="exit",command=exit1).grid(row=10,column=0)
            root2.mainloop()
   
    
        
    Button(root,text='OK',command=city,font="Aerial 20 bold italic").grid(row=14,column=10,sticky='ewns')
    
    root.mainloop()
    
    

Button(root1, text='continue',command=cont).grid(row=7,column=1,sticky='ewns')
root1.mainloop()

