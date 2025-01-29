from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
class Student :

    #        -------------------------- انشاء نافذه البرنامج -------------------------

    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x690-1+1')    #width x length  -> screen
        self.root.title("برنامج ادارة المدارس")
        self.root.configure(background='silver')
        self.root.resizable(True,True)         #مشان ما تقدر تصغر الشاشة ولا تقدر تتحكم في قياسها       width , length
        title = Label(self.root ,
                      text='[نظام تسجيل الطلاب ]',
                      bg="#DEB887",
                      font=('monospace',14,'bold'),         #  درجة الخط   حجمه  نوع الخط
                      fg='white'
                      )
        title.pack(fill=X)                  #مشان تقدر تظهر هاد العنوان في المشروع             FILL =مشان يعبي السطر ب نفس اللون المطلوب

        #=============================variable===================
        self.id_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.phon_var=StringVar()
        self.mohalt_var = StringVar()
        self.gender_var = StringVar()
        self.address_var = StringVar()
        self.se_by=StringVar()
        self.se_var=StringVar()
        self.delete_var=StringVar()
        # ---------------------ادوات التحكم بالبرنامج---------------------------
        Manage_Frame=Frame(self.root,bg="#FFEBCD")       #مشان يظهر في root
        Manage_Frame.place(x=1100,y=30,width=210,height=400)

        lab_ID=Label(Manage_Frame,text=':الرقم التسلسلي' , bg="#FFEBCD")
        lab_ID.pack()
        ID_Entry=Entry(Manage_Frame ,textvariable=self.id_var,bd='2',justify='right')     # bd = board يعني انه يظهر من الاربع جهات    justify =بتحدد من وين تكتب Arabic , English
        ID_Entry.pack()                                          # entry حقل ادخل

        lab_name=Label(Manage_Frame,bg='#FFEBCD',text=": اسم الطالب ")
        lab_name.pack()
        name_Entry=Entry(Manage_Frame,textvariable=self.name_var,bd='2', justify='center')
        name_Entry.pack()

        lab_email=Label(Manage_Frame,bg='#FFEBCD',text=": ايميل الطالب ")
        lab_email.pack()
        name_email=Entry(Manage_Frame,textvariable=self.email_var,bd='2', justify='center')
        name_email.pack()

        lab_phone=Label(Manage_Frame,bg='#FFEBCD',text=": رقم الطالب ")
        lab_phone.pack()
        phone_Entry=Entry(Manage_Frame,textvariable=self.phon_var,bd='2', justify='center')
        phone_Entry.pack()

        lab_cirte=Label(Manage_Frame,bg='#FFEBCD',text=": مؤهلات الطالب ")
        lab_cirte.pack()
        cirte_Entry=Entry(Manage_Frame,textvariable=self.mohalt_var,bd='2', justify='center')
        cirte_Entry.pack()

        lab_gender=Label(Manage_Frame,text= ": اختر جنس الطالب ",bg='#FFEBCD')
        lab_gender.pack()
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var)
        combo_gender['value']=('ذكر',"انثى")
        combo_gender.pack()

        lab_address=Label(Manage_Frame ,bg='#FFEBCD',text=": عنوان الطالب ")
        lab_address.pack()
        address_entry=Entry(Manage_Frame,textvariable=self.address_var ,bd='2',justify='right')
        address_entry.pack()

        lab_delete=Label(Manage_Frame , fg='red' , bg='#FFEBCD' , text=' : حذف الطالب بالاسم')
        lab_delete.pack()
        delete_entry=Entry(Manage_Frame,textvariable=self.delete_var,bd='2',justify="center")
        delete_entry.pack()

        #===================================== button =================================
        bto_frame=Frame(self.root,bg='#008B8B')
        bto_frame.place(x=1100,y=435,width=210,height=210)
        title1=Label(bto_frame,text=" : لوحة التحكم",font=('Doce',14),fg='white',bg='#2980B9')
        title1.pack(fill=X)

        add_bto=Button(bto_frame,text=' اضافة طالب',bg='#85929E',fg='white',command=self.add_student)
        add_bto.place(x=33,y=33,width=150,height=30)

        del_bto=Button(bto_frame,text=' حذف طالب',bg='#85929E',fg='white',command=self.delete)
        del_bto.place(x=33, y=63, width=150, height=30)

        update_bot=Button(bto_frame,text='تعديل بيانات طالب ',bg='#85929E',fg='white',command=self.update)
        update_bot.place(x=33, y=93, width=150, height=30)

        clear_bto=Button(bto_frame,text=' افراغ الحقول ',bg='#85929E',fg='white',command=self.clear)
        clear_bto.place(x=33, y=123, width=150, height=30)

        about_bto=Button(bto_frame,text='  من نحن ',bg='#85929E',fg='white',command=self.about)
        about_bto.place(x=33, y=153, width=150, height=30)

        exit_bto=Button(bto_frame,text='اغلاق البرنامج',bg='#85929E',fg='white',command=root.quit)
        exit_bto.place(x=33, y=183, width=150, height=30)

#=============================search manage ==================================
        search_frame=Frame(self.root,bg="#FFFACD",)
        search_frame.place(x=1,y=30,width=1094,height=50)

        lab_search=Label(search_frame,text=" : البحث عن الطالب ",bg='white')
        lab_search.place(x=980 ,y=12)

        combo_search=ttk.Combobox(search_frame,textvariable=self.se_by,justify='right')
        combo_search['value']=('ID','Name','Email','phone')
        combo_search.place(x=848,y=12)

        search_entry=Entry(search_frame,textvariable=self.se_var,justify='right',bd='2')
        search_entry.place(x=720,y=12)

        se_bto=Button(search_frame,text=" بحث",bg='#3498DB',fg='white',command=self.search)
        se_bto.place(x=610,y=12,width=100,height=25 )

        #============dietals==================

        dietals_frame=Frame(self.root,bg='#F2F4F4')
        dietals_frame.place(x=1,y=82,width=1095,height=604 )

        #=================scrolll=======================

        scroll_x=Scrollbar(dietals_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(dietals_frame,orient=VERTICAL)
        #=============tree view=======================
        self.Student_table=ttk.Treeview(dietals_frame,
                                        columns=('address','gender','certi','phone','email','name','ID'),
                                        xscrollcommand=scroll_x.set,
                                        yscrollcommand=scroll_y.set)
        self.Student_table.place(x=30,y=1,width=1100 ,height=550)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)
        scroll_x.config(command=self.Student_table.xview())
        scroll_y.config(command=self.Student_table.yview())

        self.Student_table['show']='headings'
        self.Student_table.heading('address',text='عنوان الطالب ')
        self.Student_table.heading('gender',text='جنس الطالب ')
        self.Student_table.heading('certi',text='مؤهلات الطالب ')
        self.Student_table.heading('phone',text='رقم الهاتف ')
        self.Student_table.heading('email',text='بريد الاكتروني ')
        self.Student_table.heading('name',text='اسم الطالب ')
        self.Student_table.heading('ID',text='رقم التسلسلي ')

        self.Student_table.column('address',width=15)
        self.Student_table.column('gender', width=30)
        self.Student_table.column('certi', width=20)
        self.Student_table.column('phone', width=25)
        self.Student_table.column('email', width=25)
        self.Student_table.column('name', width=20)
        self.Student_table.column('ID', width=10)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)



#-----------------------add + con ---------------
        self.fetch_all()
    def add_student(self):
            con=pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='stud'
            )
            cur=con.cursor()
            cur.execute("insert into Student values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                self.address_var.get(),
                                                                self.gender_var.get(),
                                                                self.mohalt_var.get(),
                                                                self.phon_var.get(),
                                                                self.email_var.get(),
                                                                self.name_var.get(),
                                                                self.id_var.get()
                                                                ))
            con.commit()
            self.fetch_all()
            self.clear()
            con.close()
    def fetch_all(self):
        con=pymysql.connect(host='localhost',
                user='root',
                password='',
                database='stud'
        )
        cur=con.cursor()
        cur.execute('select * from Student')
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("",END,value=row)
            con.commit()
        con.close()

    def delete(self):
        con = pymysql.connect(host='localhost',
                              user='root',
                              password='',
                              database='stud'
                              )
        cur = con.cursor()
        cur.execute("delete from Student where name=%s",self.delete_var.get())
        con.commit()
        self.fetch_all()
        con.close()
    def clear(self):
        self.id_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.phon_var.set("")
        self.mohalt_var.set("")
        self.gender_var.set("")
        self.address_var.set("")

    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.id_var.set(row[6])
        self.name_var.set(row[5])
        self.email_var.set(row[4])
        self.phon_var.set(row[3])
        self.mohalt_var.set(row[2])
        self.gender_var.set(row[1])
        self.address_var.set(row[0])
    def update(self):
        con = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='stud'
        )
        cur = con.cursor()
        cur.execute("update Student set address=%s,gender=%s,moahel=%s,phone=%s,email=%s,name=%s where id=%s", (
            self.address_var.get(),
            self.gender_var.get(),
            self.mohalt_var.get(),
            self.phon_var.get(),
            self.email_var.get(),
            self.name_var.get(),
            self.id_var.get()
        ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
    def search(self):
        con=pymysql.connect(host='localhost',
                user='root',
                password='',
                database='stud'
        )
        cur=con.cursor()
        cur.execute("select * from Student where " +
        str(self.se_by.get())+" LIKE '%"+str(self.se_var.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("",END,value=row)
            con.commit()
        con.close()
    def about(self):
        messagebox.showinfo("Hello Dr.Maram","Devlopers\nSuhip Majdi \nKhaled\nBaraa")


root=Tk()   # هون اوبجكت مشان يستدعي الكلاس الجاهز من المكتبة
ob=Student(root)
root.mainloop()              #هون تشغيل البرنامج