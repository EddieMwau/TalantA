from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('landing/landing.kv')


class LandingWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class LandingApp(App):
    def build(self):
        return LandingWindow()


if __name__ == "__main__":
    LandingApp().run()
