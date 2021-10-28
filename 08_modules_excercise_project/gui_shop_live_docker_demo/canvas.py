from tkinter import Tk
def create_app():
    # Tkinter Window
    root_window = Tk()
    # Window Settings
    root_window.title('My Cool GUI Register')
    root_window.geometry('600x500+0+0')
    return root_window

app_window = create_app()