from kivy.lang import Builder
from kivymd.app import MDApp

class FPL_sys(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.accent_palette = 'Gray'
        return Builder.load_file('FPL_kivy.kv')

    def apply_next(self):
        if self.root.ids.question_number.title == "Question number 1:":
            self.root.ids.question.text = "Second one"
            self.root.ids.question_number.title = "Question number 2:"
        elif self.root.ids.question_number.title == "Question number 2:":
            self.root.ids.question.text = "3"
            self.root.ids.question_number.title = "Question number 3:"
        elif self.root.ids.question_number.title == "Question number 3:":
            self.root.ids.question.text = "4"
            self.root.ids.question_number.title = "Question number 4:"
        elif self.root.ids.question_number.title == "Question number 4:":
            self.root.ids.question.text = "5"
            self.root.ids.question_number.title = "Question number 5:"
        elif self.root.ids.question_number.title == "Question number 5:":
            self.root.ids.question.text = "6"
            self.root.ids.question_number.title = "Question number 6:"
        elif self.root.ids.question_number.title == "Question number 6:":
            self.root.ids.question.text = "Language you should learn is:"
            self.root.ids.question_number.title = "Result"

            self.root.ids.apply_next.text = "Quit"
            self.root.ids.slider1.disabled = True
            self.root.ids.slider0.disabled = True
        else:
            self.stop()


FPL_sys().run()
