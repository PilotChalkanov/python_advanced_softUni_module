from gui_shop_live_docker_demo.canvas import app_window

def clean_screen():
    for el in app_window.grid_slaves():
        el.destroy()
