from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.button import Button


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


class KvPracticeApp(App):
    pass
# We're doing almost everything in the KV file, so we can just pass on the class


if __name__ == '__main__':
    KvPracticeApp().run()
