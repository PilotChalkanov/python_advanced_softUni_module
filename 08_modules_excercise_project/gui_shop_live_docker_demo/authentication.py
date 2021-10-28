from tkinter import Button, Entry, Label
from gui_shop_live_docker_demo.canvas import app_window
from gui_shop_live_docker_demo.helpers import clean_screen
from pyravendb.store import document_store

def register(**kwargs):
    store = document_store.DocumentStore(urls=["http://localhost:8080"], database="User_Register")
    store.initialize()

    """"User Info"""
    class User:
        def __init__(self,username,password,first_name,last_name,email):
            self.username = username
            self.password = password
            self.first_name = first_name
            self.last_name = last_name
            self.email = email
        def register_completed(self):
            clean_screen()
            Label(app_window, text="Registration Completed! Thank you!").grid(row=0, column=0)
    user = User(**kwargs)
    """Storing data in Raven"""


    with store.open_session() as session:
        session.store(user)
        session.save_changes()




def render_reg():
    clean_screen()
    Label(app_window,text = "Username").grid(row = 0, column = 0)
    username = Entry(app_window)
    username.grid(row=0, column=1)

    Label(app_window, text="Password").grid(row=1, column=0)
    password = Entry(app_window, show ="*")
    password.grid(row=1, column=1)

    Label(app_window, text="First Name").grid(row=2, column=0)
    first_name = Entry(app_window)
    first_name.grid(row=2, column=1)

    Label(app_window, text="Last Name").grid(row=3, column=0)
    last_name = Entry(app_window)
    last_name.grid(row=3, column=1)

    Label(app_window, text="email").grid(row=4, column=0)
    email = Entry(app_window)
    email.grid(row=4, column=1)
    enter_button = Button(app_window, text="Register", bg="green",
                          command = lambda: register( username=username.get(),
                                                      password=password.get(),
                                                      first_name=first_name.get(),
                                                      last_name=last_name.get(),
                                                      email = email.get()),
                          )



    enter_button.grid(row=5, column=0)
def render_login():
    clean_screen()
    username = Entry(app_window)
    username.grid(row=0,column =0)
    password = Entry(app_window)
    password.grid(row=1, column=0)
    enter_button = Button(app_window,text="Login",bg="green")
    enter_button.grid(row=2, column = 0)

def render_main_enter_screen(app_window):
    login_button = Button(app_window, text = "Login", bg = "green", fg="white", command=render_login)
    login_button.grid(row= 0,column = 0)
    reg_button = Button(app_window, text="Register", bg="yellow", fg="black",command = render_reg)
    reg_button.grid(row=0, column=1)

