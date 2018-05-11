from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.properties import NumericProperty, Clock, ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager


class AddButton(Button):
    """
    The Button class is a simple button. It looks like a button. It can be clicked.
    We're only defining this Button so that we can create a customized on_press button
    """

    button_count = NumericProperty(0)

    # This doesn't work quite the way I anticipated, but it's useful for demonstrating the AddButton

    def on_press(self):
        """
        Like in Pong, this is an event handler. Unlike Pong, this is for responding to when the Button is pressed
        """
        self.button_count += 1
        self.parent.add_widget(AddButton(text="hi der {}".format(self.button_count)))
        '''
        Whatever the parent object is, add a new AddButton to it.
        All Widgets (a button is also a Widget) have an add_widget method. This method adds the given Widget as a 
        child to the widget the method is beind called on. In this case, it's adding a new widget to the parent widget.
        We create a new AddButton that we use in the add_widget method. 

        A note on the format call. In a string, a set of curly brackets {} acts as a placeholder. If you call the format
        method on the string, you can replace the placeholder with whatever is given to the format function. In this 
        case, the placeholder is being replaced with the button_count object. 
        '''


class TimerVisual(Label):

    seconds = NumericProperty(25*60)
    timer_event = ObjectProperty()

    def start_timer(self):
        if self.seconds > 0:
            self.color = (0, 0, 0, 1)
            self.timer_event = Clock.schedule_interval(self.update_timer, 1.0)

    def update_timer(self, dt):
        self.seconds -= 1
        if self.seconds <= 0:
            self.timer_event.cancel()
            self.color = (1, 0, 0, 1)

    def stop_timer(self):
        self.timer_event.cancel()
        self.color = (0, 0, 0, 1)

    def reset_timer(self):
        self.seconds = 25*60
        self.stop_timer()


class PomodoroApp(App):
    pass


# We're doing almost everything in the KV file, so we can just pass on the class


if __name__ == '__main__':
    PomodoroApp().run()
