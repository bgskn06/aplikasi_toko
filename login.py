from kivymd.app import MDApp
from kivymd.uix.toolbar import MDTopAppBar
class Login(MDApp):
    def build(self):
        toolbar = MDTopAppBar(title="My Toolbar")
        toolbar.pos_hint = {"top": 1} # Menempatkan toolbar di atas
        return toolbar
if __name__ == '__main__':
            Login().run()