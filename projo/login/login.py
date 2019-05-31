from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from collections import OrderedDict

import pymysql

Builder.load_file('login/login.kv')


class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cancel_login(self):
        self.parent.parent.current = 'scr_index'

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text
        #signin_text = self.ids.sp3.text
        #signin_text = '[color=#0000FF]New user? Sign in instead.[/color]'

        db = pymysql.connect('localhost', 'root', 'kidflash', 'talanta')
        cursor = db.cursor()

        sql = "SELECT * FROM USERS WHERE USER_NAME = '%s' AND PASSWORD = '%s' " % (uname, passw)

        cursor.execute(sql)
        users = cursor.fetchall()

        if uname == '' or passw == '':
            info.text = '[color=#FF0000]username and/or password required[/color]'
        else:
            if users:
                info.text = '[color=#00FF00]Logged in successfully[/color]'
                self.parent.parent.current = 'scr_la'
            else:
                info.text = '[color=#FF0000]Invalid username or password[/color]'


class LoginApp(App):
    def build(self):
        return SigninWindow()


if __name__ == "__main__":
    la = LoginApp()
    la.run()