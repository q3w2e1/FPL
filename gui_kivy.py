from kivy.lang import Builder
from kivymd.app import MDApp


class FPL_sys(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.accent_palette = 'Gray'
        return Builder.load_file('FPL_kivy.kv')

FPL_sys().run()
