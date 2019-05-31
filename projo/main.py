from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from login.login import SigninWindow
from landing.landing import LandingWindow
from index.index import IndexWindow
from signup.signup import SignupWindow


class MainWindow(BoxLayout):

    index_widget = IndexWindow()
    landing_widget = LandingWindow()
    login_widget = SigninWindow()
    signup_widget = SignupWindow()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.scr_su.add_widget(self.signup_widget)
        self.ids.scr_si.add_widget(self.login_widget)
        self.ids.scr_index.add_widget(self.index_widget)
        self.ids.scr_la.add_widget(self.landing_widget)


class MainApp(App):
    def build(self):
        return MainWindow()


if __name__ == "__main__":
    MainApp().run()