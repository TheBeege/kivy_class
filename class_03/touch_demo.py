from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, ListProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


class TouchSpot(Widget):
    ellipse_rgb = ListProperty([0, 0, 1])

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def __init__(self, **kwargs):
        self.ellipse_rgb = [0, 0, 1]
        super(TouchSpot, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            self.ellipse_rgb = [1, 1, 1, 1]
        elif touch.is_triple_tap:
            self.ellipse_rgb = [0, 1, 0, 1]
        else:
            self.ellipse_rgb = [1, 0, 0, 1]

    def on_touch_up(self, touch):
        self.ellipse_rgb = [0, 0, 1, 1]

    def on_touch_move(self, touch):
        self.x_velocity = (touch.x - self.x)*0.1
        self.y_velocity = (touch.y - self.y)*0.1
        self.velocity = self.x_velocity, self.y_velocity

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class RootWidget(Widget):
    touch_spot = ObjectProperty(None)

    def update(self, dt):
        self.touch_spot.move()


class TouchApp(App):

    def build(self):
        root = RootWidget()
        Clock.schedule_interval(root.update, 1.0 / 60.0)
        return root


# We're doing almost everything in the KV file, so we can just pass on the class


if __name__ == '__main__':
    TouchApp().run()
