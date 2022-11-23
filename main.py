from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.recycleview import RecycleView

# The main kv file is loaded autoatically because of naming rules [ call it like your App class less the "App" eg: NavigationApp--> navigation.kv]
Builder.load_file("screen1.kv")
Builder.load_file("screen2.kv")
Builder.load_file("screen3.kv")

class MainScreen(MDScreen):
    pass

# Define the Recycleview class which is created in .kv file
class RecycleViewer(RecycleView):
    def __init__(self, **kwargs):
        super(RecycleViewer, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(20)]

class NavigationApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return MainScreen()


NavigationApp().run()