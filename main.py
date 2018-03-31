# make kivy available
import kivy

# tell our program we need a specific version
kivy.require('1.10.0')

# App represents our entire mobile app
from kivy.app import App
# Label is text that we can put on a screen
from kivy.uix.label import Label


# This is our base app
class MyApp(App):
    # build() is called when the app is setting up
    def build(self):
        return Label(text='Hello world')


# If this is the main program, run the app
if __name__ == '__main__':
    MyApp().run()
