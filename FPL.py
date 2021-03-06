from kivy.lang import Builder
from kivymd.app import MDApp
from FPL_cmd import FPL_compute

class FPL_sys(MDApp):
    # state of the consultation according to the question being asked
    state = 0
    # values from sliders will be stored here
    GUIconsultation = {}

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.accent_palette = 'Gray'
        return Builder.load_file('deps\FPL_kivy.kv')

    def apply_next(self):
        """apply_next (id) button being pushed
            - slider values are being recorded into GUIconsultation dictionary
        """
        if self.state == 0:
            self.state = 1
            self.root.ids.question.text = "Do you need OOP (object oriented programming) support?"
            self.root.ids.question_number.title = "Question number 2:"
            self.GUIconsultation["experience"] = (int(self.root.ids.slider0.value),
                                                  int(self.root.ids.slider1.value))
        elif self.state == 1:
            self.state = 2
            self.root.ids.question.text = "Do you care about the number of programming repositories that the language has?"
            self.root.ids.question_number.title = "Question number 3:"
            self.GUIconsultation["OOP"] = (int(self.root.ids.slider0.value),
                                           int(self.root.ids.slider1.value))
        elif self.state == 2:
            self.state = 3
            self.root.ids.question.text = "Do you need a language with multithread support?"
            self.root.ids.question_number.title = "Question number 4:"
            self.GUIconsultation["repos"] = (int(self.root.ids.slider0.value),
                                             int(self.root.ids.slider1.value))
        elif self.state == 3:
            self.state = 4
            self.root.ids.question.text = "Do you want the language to support pointer arithmetic?"
            self.root.ids.question_number.title = "Question number 5:"
            self.GUIconsultation["multi"] = (int(self.root.ids.slider0.value),
                                             int(self.root.ids.slider1.value))
        elif self.state == 4:
            self.state = 5
            self.root.ids.question.text = "Is it advantageous for this language to be high level?"
            self.root.ids.question_number.title = "Question number 6:"
            self.GUIconsultation["pointer"] = (int(self.root.ids.slider0.value),
                                               int(self.root.ids.slider1.value))
        elif self.state == 5:
            self.state = 6
            self.GUIconsultation["highlev"] = (int(self.root.ids.slider0.value),
                                               int(self.root.ids.slider1.value))

            # here the computation takes place, as the consultation values are known
            self.root.ids.question.text = f"You might consider to start with {FPL_compute(self.GUIconsultation)}"
            self.root.ids.question_number.title = "Result"

            self.root.ids.apply_next.text = "Quit"
            self.root.ids.slider1.disabled = True
            self.root.ids.slider0.disabled = True
            self.root.ids.slider1_name.theme_text_color = "Secondary"
            self.root.ids.slider0_name.theme_text_color = "Secondary"
        else:
            self.stop()

        # resetting slider values after each question is answered
        self.root.ids.slider0.value = 27
        self.root.ids.slider1.value = 27

FPL_sys().run()
