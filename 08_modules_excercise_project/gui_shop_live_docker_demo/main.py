from gui_shop_live_docker_demo.canvas import app_window
from gui_shop_live_docker_demo.authentication import render_main_enter_screen
from pyravendb.store import document_store

if __name__ == "__main__":
    render_main_enter_screen(app_window)
    app_window.mainloop()

