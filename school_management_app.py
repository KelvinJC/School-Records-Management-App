
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
from PIL import ImageTk, Image

from db_school import Database
from student import Course

db = Database('school.db')
ca = Course('Computer Appreciation')

class SRMSApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, *kwargs)
        tk.Tk.wm_title(self, 'School Records Management System')
        #tk.Tk.iconbitmap(self, default='png-to-ico.ico')
        tk.Tk.geometry(self, '1350x700')
        tk.Tk.resizable(self, width= False, height = False)


        container = tk.Frame(self)

        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, SignUp, Login, TeacherDashboard, AdminDashboard, StudentDetails, ClassDetails):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Image import
        self.img = Image.open("alexandre-van-thuan-mr9FouttLGY-unsplash.jpg")
        self.img = self.img.resize((1348,698))

        # There is the need to specify the master tk instance since ImageTK is a second instance of tkinter
        self.img = ImageTk.PhotoImage(self.img, master=self)

        # Define canvas
        self.my_canvas = tk.Canvas(self, width=1350, height=700)
        self.my_canvas.grid(row=0, column = 0)

        # Put the image on the canvas
        self.my_canvas.create_image(0,0, image=self.img, anchor='nw')

        # Add label
        self.my_canvas.create_text(180, 250, text = 'SRMS 1.0', font=("Arial black", 40, 'bold italic'), fill='white')
        self.my_canvas.create_text(120, 285, text = 'All your records at the touch of a button.', font=("Arial black", 10), fill='white', anchor='nw')

        # Add buttons
        login_button = ttk.Button(self, text = 'Login', width = 25, command=lambda: controller.show_frame(Login))
        register_button = ttk.Button(self, text = 'Register', width = 25, command=lambda: controller.show_frame(SignUp))
        # Button windows
        login_button_window = self.my_canvas.create_window(500, 350, anchor= 'nw', window=login_button)
        register_button_window = self.my_canvas.create_window(700, 350, anchor= 'nw', window=register_button)

        '''
        # Binding
        self.bind('<Configure>', self.resizer)

    def resizer(self, e):
        # Open our image
        self.bg1 = Image.open("pexels-olenka-sergienko-3646172.jpg")
        # Resize the image
        self.resized_bg = self.bg1.resize((e.width, e.height), Image.ANTIALIAS)
        # Define our image again
        self.new_img = ImageTk.PhotoImage(self.resized_bg)
        # Add it back to the canvas
        self.my_canvas.create_image(0,0, image=self.new_img, anchor='nw')
        # Add text back
        self.my_canvas.create_text(180, 330, text = 'SRMS 1.0', font=("Arial black", 40, 'bold italic'), fill='white')

        '''

class SignUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Image import
        self.img = Image.open("alexandre-van-thuan-DPwd8uWFb0k-unsplash.jpg")
        self.img = self.img.resize((1348,698))

        # There is the need to specify the master tk instance since ImageTK is a second instance of tkinter
        self.img = ImageTk.PhotoImage(self.img, master=self)
        # Define canvas
        self.my_canvas = tk.Canvas(self, width=1350, height=700)
        self.my_canvas.grid(row=0, column = 0)
        # Put the image on the canvas
        self.my_canvas.create_image(0,0, image=self.img, anchor='nw')
        # Add label
        self.my_canvas.create_text(450, 208, text = 'Enter your username or ID.', font=("Arial black", 12, 'italic'), fill='white', anchor='nw')
        self.my_canvas.create_text(450, 278, text = 'Enter your password.', font=("Arial black", 12, 'italic'), fill='white', anchor='nw')
        self.my_canvas.create_text(450, 348, text = 'Retype password.', font=("Arial black", 12, 'bold italic'), fill='white', anchor='nw')

        # Variables
        self.temp_username = tk.StringVar()
        self.temp_password = tk.StringVar()
        self.temp_confirm_password = tk.StringVar()
       # Add entry
        self.username_entry = tk.Entry(self, textvariable=self.temp_username, font=('Helvetica', 18), width=30, fg="#336d92", bd=0)
        self.password_entry = tk.Entry(self, textvariable=self.temp_password, show='*', font=('Helvetica', 18), width=30, fg="#336d92", bd=0)
        self.confirm_password_entry = tk.Entry(self, textvariable=self.temp_confirm_password, show='*', font=('Helvetica', 18), width=30, fg="#336d92", bd=0)

        # Buttons
        sign_up_button=tk.Button(self, text='CREATE ACCOUNT', font=('Calibri', 12, 'bold'), width=48, height=2,
                          command=self.register)
        login_button=ttk.Button(self, text='Login', width=20,
                          command=lambda: controller.show_frame(Login))
        back_to_home_button=ttk.Button(self, text='Back to Home', width=20,
                          command=lambda: controller.show_frame(StartPage))

        # Create button windows
        username_entry_window = self.my_canvas.create_window(450, 230, anchor= 'nw', window=self.username_entry)
        pw_entry_window = self.my_canvas.create_window(450, 300, anchor= 'nw', window=self.password_entry)
        confirm_pw_entry_window = self.my_canvas.create_window(450, 370, anchor= 'nw', window=self.confirm_password_entry)
        sign_up_button_window = self.my_canvas.create_window(450, 440, anchor= 'nw', window=sign_up_button)
        login_button_window = self.my_canvas.create_window(1000, 50, anchor= 'nw', window=login_button)
        back_to_home_button_window = self.my_canvas.create_window(1150, 50, anchor= 'nw', window=back_to_home_button)

    def register(self):
        # Validation

        if self.temp_password.get() != self.temp_confirm_password.get():
            messagebox.showerror('Password Error', 'Your passwords do not match.')
            return

        list_of_files = os.listdir()
        if 'single user' not in list_of_files:
            username_info = self.temp_username.get()
            password_info = self.temp_password.get()

            file = open('single user', 'w')
            file.write(username_info+'\n')
            file.write(password_info)
            file.close()

            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.confirm_password_entry.delete(0, tk.END)

            label5 = tk.Label(self, text = "Registration successful.\nClick login to log into your account", fg = "green", font = ("Calibri", 11))
            label5.grid(row=9, padx=10, sticky=tk.W)
        else:
            label5 = tk.Label(self, text = "Registration unsuccessful.\n(Single User App)", fg = "red", font = ("Calibri", 11))
            label5.grid(row=9,padx=10, sticky=tk.W)

class Login(tk.Frame):
    login_name = ''

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Image import
        self.img = Image.open("pexels-olenka-sergienko-3646172.jpg")
        self.img = self.img.resize((1348,698))
        # There is the need to specify the master tk instance since ImageTK is a second instance of tkinter
        self.img = ImageTk.PhotoImage(self.img, master=self)
        # Define canvas
        self.my_canvas = tk.Canvas(self, width=1350, height=700)
        self.my_canvas.grid(row=0, column = 0)

        # Put the image on the canvas
        self.my_canvas.create_image(0,0, image=self.img, anchor='nw')

        # Add label
        self.my_canvas.create_text(450, 208, text = 'Enter your username or ID.', font=("Arial black", 12, 'bold italic'), fill='white', anchor='nw')
        self.my_canvas.create_text(450, 278, text = 'Enter your password.', font=("Arial black", 12, 'bold italic'), fill='white', anchor='nw')

        # Variables
        self.temp_login_name = tk.StringVar()
        self.temp_login_password = tk.StringVar()
        self.login_name = ''
        self.login_attempt = 0

        # Add entry
        self.username_entry1 = tk.Entry(self, textvariable=self.temp_login_name, font=('Helvetica', 18), width=30, fg="#336d92", bd=0)
        self.password_entry1 = tk.Entry(self, textvariable=self.temp_login_password, show='*', font=('Helvetica', 18), width=30, fg="#336d92", bd=0)

        # Buttons
        login_button = tk.Button(self, text = 'SIGN IN', font=('Calibri', 12, 'bold'), width=48, height=2,
                            command= lambda : controller.show_frame(TeacherDashboard) if self.verify_login() == 1 else ((controller.show_frame(AdminDashboard), self.clear_entry()) if self.verify_login() == 2 else messagebox.showerror('', 'Login Unsuccessful.')))

        back_to_home_button=ttk.Button(self, text='Back to Home', width=20,
                          command=lambda: controller.show_frame(StartPage))
        sign_up_button=ttk.Button(self, text='Sign Up', width=20,
                          command=lambda: controller.show_frame(SignUp))

        # Create button windows
        username_entry_window = self.my_canvas.create_window(450, 230, anchor= 'nw', window=self.username_entry1)
        pw_entry_window = self.my_canvas.create_window(450, 300, anchor= 'nw', window=self.password_entry1)
        login_button_window = self.my_canvas.create_window(450, 400, anchor= 'nw', window=login_button)
        sign_up_button_window = self.my_canvas.create_window(1000, 50, anchor= 'nw', window=sign_up_button)
        back_to_home_button_window = self.my_canvas.create_window(1150, 50, anchor= 'nw', window=back_to_home_button)

    def verify_login(self):
        # check if login username entry matches username and if login password entry matches password
        with open("single user", "r") as file:
            file_data = file.read()

        file_data = file_data.split('\n')

        # Validation
        if self.temp_login_name.get() == file_data[0]:
            if self.temp_login_password.get() == file_data[1]:
                self.login_attempt = 1
                # clear user's entries from input bar after login button is clicked
                self.clear_entry()
            else:
                messagebox.showerror('Password Error', 'Incorrect password.')
                # clear user's entries from input bar after message popup button is clicked
                self.clear_entry()
                return
        elif self.temp_login_name.get() == file_data[2]:
            if self.temp_login_password.get() == file_data[3]:
               self.login_attempt = 2
               # clear user's entries from input bar after login button is clicked
               # self.clear_entry()
            else:
                messagebox.showerror('Password Error', 'Incorrect password.')
                # clear user's entries from input bar after message popup button is clicked
                self.clear_entry()
                return
        else:
            self.login_attempt = 0
            #messagebox.showerror('Account Error', 'No account found!')
        return self.login_attempt

    def clear_entry(self):
        self.username_entry1.delete(0, tk.END)
        self.password_entry1.delete(0, tk.END)

class TeacherDashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Image import
        self.img = Image.open("pexels-element-digital-1370296.jpg")
        self.img = self.img.resize((1348,698))

        # There is the need to specify the master tk instance since ImageTK is a second instance of tkinter
        self.img = ImageTk.PhotoImage(self.img, master=self)

        # Define canvas
        my_canvas = tk.Canvas(self, width=1350, height=700)
        my_canvas.grid(row=0, column = 0)

        # Put the image on the canvas
        my_canvas.create_image(0,0, image=self.img, anchor='nw')

        # Add label
        my_canvas.create_text(170, 120, text = 'REPORTS', font=("Arial black", 30, 'bold italic'), fill='white', anchor= 'nw')
        my_canvas.create_text(850, 130, text = 'Welcome '+self.get_name()+'!', font=("Arial black", 18, 'bold italic'), fill='green', anchor= 'nw')

        # Add buttons
        button1 = tk.Button(self, text='Student Report Dashboard', font=('Calibri', 12), width=23, command = lambda: controller.show_frame(StudentDetails))
        button2 = tk.Button(self, text="Class Report Dashboard", font=('Calibri', 12), width=23, command=lambda: controller.show_frame(ClassDetails))
        # Create button windows
        button1_window = my_canvas.create_window(50, 260, anchor= 'nw', window=button1)
        button2_window = my_canvas.create_window(310, 260, anchor= 'nw', window=button2)

    def get_name(self):
        # check if login username entry matches username and if login password entry matches password
        with open("single user", "r") as file:
            file_data = file.read()

        file_data = file_data.split('\n')
        self.name = file_data[0].title()

        return self.name

class AdminDashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Image import
        self.img = Image.open("kyo-azuma-x_TJKVU1FJA-unsplash.jpg")
        self.img = self.img.resize((1348,698))

        # There is the need to specify the master tk instance since ImageTK is a second instance of tkinter
        self.img = ImageTk.PhotoImage(self.img, master=self)

        # Define canvas
        my_canvas = tk.Canvas(self, width=1350, height=700)
        my_canvas.grid(row=0, column = 0)

        # Put the image on the canvas
        my_canvas.create_image(0,0, image=self.img, anchor='nw')

        # Add label
        my_canvas.create_text(170, 120, text = 'REPORTS', font=("Arial black", 30, 'bold italic'), fill='white', anchor= 'nw')
        my_canvas.create_text(850, 130, text = 'Welcome Admin!', font=("Arial black", 18, 'bold italic'), fill='white', anchor= 'nw')

        # Add buttons
        button1 = tk.Button(self, text='Student Report Dashboard', font=('Calibri', 12), width=23, command = lambda: controller.show_frame(StudentDetails))
        button2 = tk.Button(self, text="Class Report Dashboard", font=('Calibri', 12), width=23, command=lambda: controller.show_frame(ClassDetails))
        # Create button windows
        button1_window = my_canvas.create_window(50, 260, anchor= 'nw', window=button1)
        button2_window = my_canvas.create_window(310, 260, anchor= 'nw', window=button2)

    def get_name(self):
        # check if login username entry matches username and if login password entry matches password
        with open("single user", "r") as file:
            file_data = file.read()

        file_data = file_data.split('\n')
        self.name = file_data[0].title()

        return self.name
class StudentDetails(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Student
        self.student_text = tk.StringVar()
        student_label = tk.Label(self, text='Student *', font=('Calibri', 12))
        student_label.grid(row=2, column=0, sticky=tk.W, pady=20, padx=10)
        self.student_entry = tk.Entry(self, textvariable=self.student_text, width=30)
        self.student_entry.grid(row=2, column=1, padx=5)

        # Course
        self.course_text = tk.StringVar()
        course_label = tk.Label(self, text='Course *', font=('Calibri', 12))
        course_label.grid(row=2, column=2, sticky=tk.E, padx=10)
        self.course_entry = tk.Entry(self, textvariable=self.course_text, width=30)
        self.course_entry.grid(row=2, column=3, sticky=tk.W)

        # Gender
        self.gender_text = tk.StringVar()
        gender_label = tk.Label(self, text='Gender *', font=('Calibri', 12))
        gender_label.grid(row=3, column=0, sticky=tk.W,  padx=10)
        self.gender_entry = tk.Entry(self, textvariable=self.gender_text, width=10)
        self.gender_entry.grid(row=3, column=1, padx=5, sticky=tk.W)

        # Tests
        self.test1_text = tk.StringVar()
        test1_label = tk.Label(self, text='Test 1 *', font=('Calibri', 12))
        test1_label.grid(row=4, column=0, padx=10, sticky=tk.W)
        self.test1_entry = tk.Entry(self, textvariable=self.test1_text, width=10)
        self.test1_entry.grid(row=4, column=1, padx=5, sticky=tk.W)

        self.test2_text = tk.StringVar()
        test2_label = tk.Label(self, text='Test 2 *', font=('Calibri', 12))
        test2_label.grid(row=5, column=0, padx=10, sticky=tk.W)
        self.test2_entry =tk.Entry(self, textvariable=self.test2_text, width=10)
        self.test2_entry.grid(row=5, column=1, padx=5, sticky=tk.W)

        # Project
        self.project_text = tk.StringVar()
        project_label = tk.Label(self, text='Project *', font=('Calibri', 12))
        project_label.grid(row=6, column=0, padx=10, sticky=tk.W)
        self.project_entry =tk.Entry(self, textvariable=self.project_text, width=10)
        self.project_entry.grid(row=6, column=1, padx=5, sticky=tk.W)

        # Exam
        self.exam_text = tk.StringVar()
        exam_label =tk.Label(self, text='Examination *', font=('Calibri', 12))
        exam_label.grid(row=7, column=0, sticky=tk.W, padx=10)
        self.exam_entry =tk.Entry(self, textvariable=self.exam_text, width=10)
        self.exam_entry.grid(row=7, column=1, padx=5, sticky=tk.W)

        # Total score
        total_score_label =tk.Label(self, text='Total score', font=('Calibri', 12))
        total_score_label.grid(row=8, column=0, sticky=tk.W, padx=10)
        self.total_score_notif =tk.Label(self, font=('Calibri', 12))
        self.total_score_notif.grid(row=8, column=1, sticky=tk.W)

        # Position

        # Students List (Listbox)
        self.students_list = tk.Listbox(self, height=12, width=78)
        self.students_list.grid(row=3, column=2, columnspan=3, rowspan=6, padx=(5, 5))

        # Create scrollbar
        scrollbar= tk.Scrollbar(self)
        scrollbar.grid(row=3, column=5,rowspan=6, sticky=(tk.N, tk.S, tk.W))
        # Set scroll to listbox
        self.students_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.students_list.yview)

        # Bind select
        self.students_list.bind('<<ListboxSelect>>', self.select_item)

        # Add Buttons
        add_button =tk.Button(self, text='Add Student Report', width=20, command=self.add_report)
        add_button.grid(row=9, column=2, pady=10, padx=5, sticky=tk.W)

        remove_button =tk.Button(self, text='Remove Student Report', width=20, command=self.remove_report)
        remove_button.grid(row=9, column=3, padx=5, sticky=tk.W)

        update_button =tk.Button(self, text='Update Student Report', width=20, command=self.update_report)
        update_button.grid(row=10, column=2, padx=5, sticky=tk.W)

        clear_button =tk.Button(self, text='Clear Text', width=20, command=self.clear_text)
        clear_button.grid(row=10, column=3, padx=5, sticky=tk.W)

        # Navigation
        button1=ttk.Button(self, text='Class Report', width=15,
                          command=lambda: controller.show_frame(ClassDetails))
        button1.grid(row=1, column=7, pady=(10, 0), padx=5)

        home_button=ttk.Button(self, text='Back to Home', width=15,
                          command=lambda: controller.show_frame(StartPage))
        home_button.grid(row=1, column=8, pady=(10, 0))

        self.populate_list()

    def populate_list(self):
        self.students_list.delete(0, tk.END)
        # prin = ''
        for row in db.fetch():
            self.students_list.insert(tk.END, row) # To remove the curly brackets, 'row' can be replaced with something like (str(row[0]) +'  '+ str(row[2]))

    def select_item(self, event):
        try:
            #global selected_item
            index = self.students_list.curselection()[0]
            self.selected_item = self.students_list.get(index)

            self.course_entry.delete(0, tk.END)
            self.course_entry.insert(tk.END, self.selected_item[1])
            self.student_entry.delete(0, tk.END)
            self.student_entry.insert(tk.END, self.selected_item[2])
            self.gender_entry.delete(0, tk.END)
            self.gender_entry.insert(tk.END, self.selected_item[3])
            self.test1_entry.delete(0, tk.END)
            self.test1_entry.insert(tk.END, self.selected_item[4])
            self.test2_entry.delete(0, tk.END)
            self.test2_entry.insert(tk.END, self.selected_item[5])
            self.project_entry.delete(0, tk.END)
            self.project_entry.insert(tk.END, self.selected_item[6])
            self.exam_entry.delete(0, tk.END)
            self.exam_entry.insert(tk.END, self.selected_item[7])
            self.total_score_notif.config(fg = 'green', text = self.selected_item[8])
            # Use this should you choose to add the position as a label
            #position_entry.delete(0, END)
            #position_entry.insert(END, self.selected_item[9])
        except IndexError:
             pass

    def calculate_total_score(self):
        # Calculate the student's total score
        try:
            total_score = float(self.test1_text.get()) + float(self.test2_text.get()) + float(self.project_text.get()) + (float(self.exam_text.get())/ 100) * 60
            total_score = round(total_score, 1)
            total_score = str(total_score)

            self.total_score_notif.config(fg = 'green', text = total_score)
        # to handle the event of user entering a string as deposit
        except ValueError:
            messagebox.showerror("Wrong Values", "Please fill all fields correctly") # come back for a closer look. maybe remove try block
        return total_score

    def score_lister(self):
        # Create a list of scores to feed into get_position function
        list_of_scores = []
        for row in db.fetch():
            list_of_scores.append(row[8])
        return list_of_scores

    def add_report(self):
        if self.student_text.get() == "" or self.course_text.get() == "" or self.gender_text.get() == "" or self.test1_text.get() == "" or self.test2_text.get() == "" or self.project_text.get() == "" or self.exam_text.get() == "":
            messagebox.showerror("Required Fields", "Please fill all fields marked with an asterisk '*' ")
            return
        # call function to calc position
        db.insert(self.course_text.get(), self.student_text.get(), self.gender_text.get(), self.test1_text.get(),
                  self.test2_text.get(), self.project_text.get(), self.exam_text.get(), self.calculate_total_score(), 0)

        self.students_list.delete(0, tk.END)
        self.clear_text()
        self.populate_list()

    def remove_report(self):
        db.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()

    def update_report(self):
        # update a single student's record
        db.update(self.selected_item[0], self.course_text.get(), self.student_text.get(), self.gender_text.get(),
                  self.test1_text.get(), self.test2_text.get(), self.project_text.get(), self.exam_text.get(),
                  self.calculate_total_score(), ca.get_position(self.selected_item[8], self.score_lister()))

        # update all positions in student's records
        for row in db.fetch():
            new_position = ca.get_position(row[8], self.score_lister())
            db.update(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], new_position)
        self.populate_list()

    def clear_text(self):
        self.course_entry.delete(0, tk.END)
        self.student_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.test1_entry.delete(0, tk.END)
        self.test2_entry.delete(0, tk.END)
        self.project_entry.delete(0, tk.END)
        self.exam_entry.delete(0, tk.END)
        self.total_score_notif.config(fg = 'green', text = '') # need no text here
        #position_entry.delete(0, END)

class ClassDetails(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Labels
        report_label = tk.Label(self, text='Course: Computer Appreciation 101', font=('Calibri', 12, 'bold'))
        report_label.grid(row=2, column=0, sticky=tk.W, pady=10, padx=10)
        class_names_label = tk.Label(self, fg='blue', text='Name', font=('Calibri', 12, 'bold italic'))
        class_names_label.grid(row=3, column=0, sticky=tk.W, pady=10, padx=10)
        total_score_label =  tk.Label(self, text='Total Score (%)', font=('Calibri', 12, 'bold italic'))
        total_score_label.grid(row=3, column=1, sticky=tk.W, padx=10)
        positions_label = tk.Label(self, text='Position in Course', font=('Calibri', 12, 'bold italic'))
        positions_label.grid(row=3, column=2, sticky=tk.W, padx=10)
        avg_score_male_label =  tk.Label(self, text='Average Score Male Students (%)', font=('Calibri', 12, 'bold italic'))
        avg_score_male_label.grid(row=3, column=3, sticky=tk.W, padx=10)
        avg_score_female_label =  tk.Label(self, text='Average Score Female Students (%)', font=('Calibri', 12, 'bold italic'))
        avg_score_female_label.grid(row=3, column=4, sticky=tk.W, padx=10)
        avg_score_male_value_label =  tk.Label(self, text= str(self.avg_score_male()), font=('Calibri', 12))
        avg_score_male_value_label.grid(row=4, column=3, sticky=tk.N)
        avg_score_female_value_label =  tk.Label(self, text=str(self.avg_score_female()), font=('Calibri', 12))
        avg_score_female_value_label.grid(row=4, column=4, sticky=tk.N)

         # Navigation
        button1=ttk.Button(self, text='Student Reports', width=20,
                          command=lambda: controller.show_frame(StudentDetails))
        button1.grid(row=0, column=5, pady=(10, 0), padx=(0, 5))

        home_button=ttk.Button(self, text='Back to Home', width=15,
                          command=lambda: controller.show_frame(StartPage))
        home_button.grid(row=0, column=6, pady=(10, 0))


        refresh_button = tk.Button(self, text="Refresh", font=('Calibri', 12), width=15, command=self.refresh())

        refresh_button.grid(row=0, column=4, pady=(10, 0), padx=(0, 5))

    def label(self):
        # Loop the labelling of each row to accomodate an unknown number of students
        for row in db.fetch():
            student_name_label = tk.Label(self, text=str(row[2]), fg='blue', font=('Calibri', 12))
            student_name_label.grid(row=4+int(row[0]), column=0, sticky=tk.W, padx=10)

        for row in db.fetch():
            student_name_label = tk.Label(self, text=str(row[8]), font=('Calibri', 12))
            student_name_label.grid(row=4+int(row[0]), column=1, sticky=tk.N, padx=10)

        for row in db.fetch():
            student_position_label = tk.Label(self, text=str(row[9]), font=('Calibri', 12))
            student_position_label.grid(row=4+int(row[0]), column=2, sticky=tk.N, padx=10)


    def avg_score_female(self):
        score_list_female = []
        for row in db.fetch():
            if row[3] == 'Female':
                score_list_female.append(row[8])
                self.avg_score_fem = sum(score_list_female)/(len(score_list_female))
                self.avg_score_fem = round(self.avg_score_fem, 1)
        return self.avg_score_fem

    def avg_score_male(self):
        score_list_male = []
        for row in db.fetch():
            if row[3] == 'Male':
                score_list_male.append(row[8])
                self.avg_score_males= sum(score_list_male) /(len(score_list_male))
                self.avg_score_males = round(self.avg_score_males, 1)
        return self.avg_score_males

        # need to find a way to refresh either through lambd OR SIME OTHER WAY
    def refresh(self):
        self.label()
        self.avg_score_female()
        self.avg_score_male()


app = SRMSApp()
app.mainloop()
