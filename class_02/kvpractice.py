from kivy.app import App
from kivy.logger import Logger
from kivy.properties import NumericProperty
from kivy.uix.button import Button


class AddButton(Button):

    button_count = NumericProperty(0)

    def clicked(self):
        Logger.info('parent: {}'.format(self.parent.size))
        Logger.info('parent parent: {}'.format(self.parent.parent.size))
        self.button_count += 1
        self.parent.add_widget(AddButton(text="hi der {}".format(self.button_count)))


class KvPracticeApp(App):
    pass


if __name__ == '__main__':
    KvPracticeApp().run()
