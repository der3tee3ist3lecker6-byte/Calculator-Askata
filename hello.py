from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Calculator_Askata(App):

    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self,instance):
        if self.formula == "0":
            self.formula = ""
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self,instance):
        self.formula += str(instance.text)
        self.update_label()

    def calcult_result(self,instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = self.lbl.text

    def build(self):
        self.formula = "0"
        grlt = GridLayout(cols=4,spacing=3,size_hint = (1,.6))
        bxlt = BoxLayout(orientation="vertical",padding=25)

        self.lbl = Label(text="0",font_size = 40, halign = "right", valign = "center",size_hint = (1,.4),text_size = (350,500 * .4 - 50))
        bxlt.add_widget(self.lbl)
        grlt.add_widget(Button(text="7",on_press=self.add_number))
        grlt.add_widget(Button(text="8", on_press=self.add_number))
        grlt.add_widget(Button(text="9", on_press=self.add_number))
        grlt.add_widget(Button(text="*", on_press=self.add_operation))

        grlt.add_widget(Button(text="4", on_press=self.add_number))
        grlt.add_widget(Button(text="5", on_press=self.add_number))
        grlt.add_widget(Button(text="6", on_press=self.add_number))
        grlt.add_widget(Button(text="-", on_press=self.add_operation))

        grlt.add_widget(Button(text="1", on_press=self.add_number))
        grlt.add_widget(Button(text="2", on_press=self.add_number))
        grlt.add_widget(Button(text="3", on_press=self.add_number))
        grlt.add_widget(Button(text="+", on_press=self.add_operation))

        grlt.add_widget(Button(text="=", on_press=self.calcult_result))
        grlt.add_widget(Button(text="0", on_press=self.add_number))
        grlt.add_widget(Button(text=".", on_press=self.add_number))
        grlt.add_widget(Button(text="/", on_press=self.add_operation))
        bxlt.add_widget(grlt)
        return bxlt

Calculator_Askata().run()