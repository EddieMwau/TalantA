from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('index/index.kv')


class IndexWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def login_btn_clicked(self):
        self.parent.parent.current = 'scr_si'

    def signup_btn_clicked(self):
        self.parent.parent.current = 'scr_signup'


class IndexApp(App):
    def build(self):
        return IndexWindow()


if __name__ == "__main__":
    IndexApp().run()