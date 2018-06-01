from kivy.app import App
from kivy.properties import NumericProperty, Clock, ObjectProperty
from kivy.uix.label import Label


class PomodoroTimer(Label):

    seconds = NumericProperty(25*60)
    event = ObjectProperty()

    def start(self):
        self.event = Clock.schedule_interval(self.update, 1.0)

    def stop(self):
        self.event.cancel()

    def reset(self):
        self.seconds = 25*60

    def update(self, dt):
        self.seconds -= 1


class ClassPomodoroApp(App):
    pass


if __name__ == '__main__':
    ClassPomodoroApp().run()
