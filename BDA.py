from tkinter import *
import tkinter as tk
import pymysql

def adjustWindow0(window):
     w = 900 # width for the window size
     h = 900 # height for the window size
     ws = screen0.winfo_screenwidth() # width of the screen
     hs = screen0.winfo_screenheight() # height of the screen
     x = (ws/2) - (w/2) # calculate x and y coordinates for the Tk window
     y = (hs/2) - (h/2)
     window.geometry('%dx%d+%d+%d' % (w, h, x, y))
     window.configure(bg="#191414")# set the dimensions of the screenand where it is placed
     window.resizable(False, False)

def retriver1():

    a=list()
    f=list()
    if mname.get():
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="music") # database connection
        cursor = connection.cursor()
        insert_query = "SELECT genres from songs where music_name = '"+mname.get()+"'"
        cursor.execute(insert_query) # executing the queries
        result = cursor.fetchall()
        result = str(result).replace(",)", "")
        result = str(result).replace("(", "")
        result = str(result).replace("'", "")
        select_query = "SELECT artist from songs where genres = '"+result+"'"
        cursor.execute(select_query)
        result2 = cursor.fetchall()
        connection.commit() # commiting the connection then closing it.
        connection.close()
        for i in range (len(result2)):
            a.append(result2[i])
        f=list(dict.fromkeys(a))
        screen2=Toplevel(screen1)
        screen2.title("Artist list")
        adjustWindow0(screen2)
        for i in range(len(f)):
            tk.Label(screen2, text=str(f[i]).replace(",)","").replace("(",""),font=("Calibri", 22, 'bold'), fg='#fb8767', bg='#191414').place(x=300,y=i*100)
    
        

def retriver2():
    a=list()
    f=list()
    if aname.get():
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="music") # database connection
        cursor = connection.cursor()
        insert_query = "SELECT genres from songs where artist = '"+aname.get()+"'"
        cursor.execute(insert_query) # executing the queries
        result = cursor.fetchall()
        result=list(dict.fromkeys(result))
        result = str(result).replace(",)", "")
        result = str(result).replace("(", "")
        result = str(result).replace("'", "")
        result = str(result).replace("[", "")
        result = str(result).replace("]", "")
        print(result)
        select_query = "SELECT artist from songs where genres = '"+result+"'"
        cursor.execute(select_query)
        result2 = cursor.fetchall()
        connection.commit() # commiting the connection then closing it.
        connection.close()
        for i in range (len(result2)):
            a.append(result2[i])
        f=list(dict.fromkeys(a))
        screen4=Toplevel(screen3)
        screen4.title("Artist list")
        adjustWindow0(screen4)
        for i in range(len(f)):
            tk.Label(screen4, text=str(f[i]).replace(",)","").replace("(",""),font=("Calibri", 22, 'bold'), fg='#fb8767', bg='#191414').place(x=300,y=i*100)

def retriver3():
    a=list()
    f=list()
    if gname.get():
        connection = pymysql.connect(host="localhost", user="root", passwd="", database="music") # database connection
        cursor = connection.cursor()
        select_query = "SELECT artist from songs where genres = '"+gname.get()+"'"
        cursor.execute(select_query)
        result2 = cursor.fetchall()
        connection.commit() # commiting the connection then closing it.
        connection.close()
        for i in range (len(result2)):
            a.append(result2[i])
        f=list(dict.fromkeys(a))
        screen6=Toplevel(screen5)
        screen6.title("Artist list")
        adjustWindow0(screen6)
        for i in range(len(f)):
            tk.Label(screen6, text=str(f[i]).replace(",)","").replace("(",""),font=("Calibri", 22, 'bold'), fg='#fb8767', bg='#191414').place(x=300,y=i*100)


def genre():     
    global screen5,gname
    gname =  StringVar()
    screen5 = Toplevel(screen0)
    screen5.title("Artist Recommender") 
    adjustWindow0(screen5)
    Label(screen5, text="GENRE SECTION", width="500", height="2",font=("Calibri", 40, 'bold'), fg='black', bg='#1DB954').pack()
    Label(screen5, text="Enter the genre name:", width="500", height="2",font=("Times New Roman", 30, 'bold'), fg='black', bg='#1DB954').pack()
    Entry(screen5, textvar=gname,width=40,font=("Open Sans", 15)).place(x=220,y=380)
    Button(screen5, text="Search",bg="#1DB954", width=17, height=1, font=("Open Sans",20, 'bold'), fg='black',command=retriver3).place(x=300,y=480)

def artist():     
    global screen3,aname
    aname =  StringVar()
    screen3 = Toplevel(screen0)
    screen3.title("Artist Recommender") 
    adjustWindow0(screen3)
    Label(screen3, text="ARTIST SECTION", width="500", height="2",font=("Calibri", 40, 'bold'), fg='black', bg='#1DB954').pack()
    Label(screen3, text="Enter the artist name:", width="500", height="2",font=("Times New Roman", 30, 'bold'), fg='black', bg='#1DB954').pack()
    Entry(screen3, textvar=aname,width=40,font=("Open Sans", 15)).place(x=220,y=380)
    Button(screen3, text="Search",bg="#1DB954", width=17, height=1, font=("Open Sans",20, 'bold'), fg='black',command=retriver2).place(x=300,y=480)
 
def music():     
    global screen1,mname
    mname =  StringVar()
    screen1 = Toplevel(screen0)
    screen1.title("Artist Recommender") 
    adjustWindow0(screen1)
    Label(screen1, text="MUSIC SECTION", width="500", height="2",font=("Calibri", 40, 'bold'), fg='black', bg='#1DB954').pack()
    Label(screen1, text="Enter the music name:", width="500", height="2",font=("Times New Roman", 30, 'bold'), fg='black', bg='#1DB954').pack()
    Entry(screen1, textvar=mname,width=40,font=("Open Sans", 15)).place(x=220,y=380)
    Button(screen1, text="Search",bg="#1DB954", width=17, height=1, font=("Open Sans",20, 'bold'), fg='black',command=retriver1).place(x=300,y=480)
    
    
def welcome():
    global screen0
    screen0 = Tk() # initializing the tkinter window
    screen0.title("Artist Recommender") # mentioning title of the window
    adjustWindow0(screen0)  #configuring the window
    Label(screen0, text="WELCOME", width="500", height="2",font=("Calibri", 40, 'bold'), fg='black', bg='#1DB954').pack()
    Label(screen0, text="Select the basis for your recommendation:", width="500", height="2",font=("Times New Roman", 30, 'bold'), fg='black', bg='#1DB954').pack()
    Button(screen0, text="Music Name", bg="#1DB954", width=17, height=1, font=("Open Sans",20, 'bold'), fg='black',command=music).place(x=300,y=380)
    Button(screen0, text="Artist Name", bg="#1DB954", width=17, height=1, font=("Open Sans",20, 'bold'), fg='black',command=artist).place(x=300,y=480)
    Button(screen0, text="Genre", bg="#1DB954", width=17, height=1, font=("Open Sans",20, 'bold'), fg='black',command=genre).place(x=300,y=580)
    screen0.mainloop()
welcome()
