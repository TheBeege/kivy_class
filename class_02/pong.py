from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
'''
A note on the imports...
Sometimes PyCharm won't recognize the Property imports. To fix this, add `import kivy.properties` and wait a moment. 
These properties use the Cython system, so PyCharm needs this extra nudge to parse and understand the C-based 
properties. If this doesn't make much sense, don't worry about it. Just know how to fix it when it happens.

We'll cover what each of these things we're importing does in the code below. Don't worry about it for now :)
'''


class PongApp(App):
    """
    As explained in the quickstart project, this is our main class that runs our Kivy app.
    In this project, we're also introducing the concept of kv files. Kv files are specific to Kivy and are used to 
    define how things will appear visually. This separates the visual representations of things (in kv files) 
    from their behaviors (in Python files). 
    For kv files, the name of the file must match the name of the app class before the word "App". Since our class
    here is named PongApp, our kv file should be named pong.kv
    """

    def build(self):
        # Also as mentioned in the quickstart project, this is the method run by our Kivy app as soon as it starts
        game = PongGame()
        # This creates the main game widget, which we'll cover below
        game.serve_ball()
        # In our main game widget, we define a serve_ball method, which we use to start the game
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        '''
        This sets up our "game loop". Games run by using an infinite loop to continuously update game objects and keep
        the game running. Usually, the function run by the loop is called "update", and we maintain that convention 
        here, too. On our main game widget, we defined an update function that we'll use here.
        Clock.schedule_interval is a Kivy method that allows us to setup a function to be called on a repeating 
        schedule until the app is closed. We'll use this to setup our game loop.
        The second parameter, `1.0 / 60.0`, sets up our game loop to run 60 times per second. 
        In reality, video is just still images changing really fast. When you see movies, maybe you've noticed many
        things say "motion pictures". Movies are just tons of individual photos changing really quickly. The images
        are swapped so quickly that your eyes see it as continuous movement rather than images being swapped out.
        Movies actually run at 24 images every second. We call these images "frames" and say that moves run at
        24 frames per second, or 24 fps. Most computer videos and games run at either 30 fps or 60 fps. We'll run ours
        at 60 fps because we're cool like that. Doing 1.0 / 60.0 will get us the amount of time that one second 
        divided into 60 parts gives us, and therefore, how much time to wait between running update each time.
        '''
        return game
        # Everything in our game is inside the PongGame widget, so we return that widget for Kivy to display


class PongGame(Widget):
    """
    This is the main widget that will contain everything we display in the game. It will also manage critical things
    like starting the game and updating the game.
    It inherits from Widget because it is a visual element in the game. We'll draw its visual representation in the
    kv file.
    """
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    '''
    ObjectProperty variables are how we associate other Kivy objects with this one. In this case, our game needs
    to manage the ball and the player paddles. This sets up placeholders that we can use to tie everything together
    in the kv file. 
    '''

    '''
    We need to cover what "velocity", or "vel" for short, is. You'll need to understand these for the following parts.
    You're familiar with speed. Speed describes the rate at which something is moving over time. Speed and velocity 
    are similar except for one key difference: velocity includes direction, while speed does not. You can say 
    something is moving 10 kph, but that tells you nothing about the direction that thing is moving. With velocity, we 
    can say something is moving at 4 along the X axis and 0 along the Y axis, and it gives both speed and direction. 
    
    What are these axis things I'm talking about? We often represent the physical world using directions. An axis
    acts as a marker to label each direction so that we know which directions we're talking about. In programming,
    we call the horizontal axis X and the vertical axis Y. Moving something only left and only right means it's
    moving along the X axis. Moving something only up and down means it's moving along the Y axis. Moving something
    diagonally means it's moving along both the X and Y axes (the plural of axis is axes, pronounced AK-sees).  
    
    In Kivy, the middle of the screen is at 0 X and 0 Y. The X axis is more positive in the right direction and more 
    negative in the left direction. This means that things on the left side of the screen have a negative X value,
    and things on the right side of the screen have a positive value. The Y axis is more positive going up and
    more negative going down. This means that things towards the top of the screen have a positive value, and things
    towards the bottom of the screen have a negative value.
    When talking about X and Y, we usually write them in parenthesis with the X first and the Y second with a comma 
    separating them. For example, a position at an X value of 4 and a Y value of 0 would be written as (4, 0).
    
    Let's try some examples:
    Something at position (0,0) is at the center of the screen. It's X is 0, and it's Y is 0.
    Something at position (4, 0) is to the right of the middle of the screen, but it's in the middle vertically.
    Something at position (-2, -1) is to the bottom left of the screen. It's farther left than it is down.
    Something at (-3, 10) is to the top left of the screen. It is much higher up than it is left.
    
    Lastly, we should talk about how we represent velocity and position. We represent both using parenthesis as 
    mentioned above. We'll use call this a "vector", which is a term borrowed from math. Vectors can represent
    either a position or velocity. These are very useful vocabulary terms, and you should take note to remember them.
    Here, we'll represent vectors either as Python tuples, Kivy Vector objects, or Kivy ReferencyListProperty objects. 
    '''

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel
    '''
    The serve_ball method is used to start the game and reset the game every time someone scores.
    
    By default, we set the velocity parameter to (4,0), but this allows the game to change the starting velocity as 
    desired.
    
    We set the center of the ball to be the center of the screen. 
    
    We then set the ball's velocity to the velocity given to serve_ball
    '''

    def update(self, dt):
        """
        The update function is our main game loop function, as described above. The dt parameter is unused. It's simply
        something the Clock provides to the scheduled function. In more advanced cases where we deal with potential
        slowdowns, we could use dt (short for datetime) to account for if we missed a frame... but don't worry about
        that for now :)
        """
        self.ball.move()
        # Tell the ball to move. The ball has its own function to move

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
        # Each player paddle also knows how to bounce the ball, so we let them handle that. Check out the Paddle classes

        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1
        '''
        If the bottom of the ball is less than the bottom of the screen or if the top of the ball is higher than the
        top of the screen, then multiply the balls' Y velocity by -1.
        
        Why negative 1? 
        When multiplying by a negative number, it changes the sign (read as, positive or negative) of the number. If
        a number is positive, multiplying by negative one makes it negative. If a number is negative, multiplying 
        by negative one makes it positive. 
        Since the sign of a velocity controls its direction, this is a fast and easy way to change direction.
        
        Effectively, this bounces the ball up or down when it hits the edge of the screen. 
        '''

        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))
        '''
        If the ball goes past the left edge of the screen, player 2's score should increase by 1, and the game should 
        reset with the ball heading to the right towards player 2.
        
        If the ball goes past the right edge of the screen, player 1's score should increase by 1, and the game should
        reset with the ball heading to the left towards player 1. 
        '''

    def on_touch_move(self, touch):
        """
        In programming, often when you see a method starting with "on", it's something called an event handler. 
        An event handler is a method that responds to some event happening. In this case, this method responds to 
        a touch and move event. Remember that Kivy is designed for mobile apps, so a touch and move event is like
        a click and drag on a computer. 
        The touch parameter is a position on the screen, with an x value and a y value. 
        """
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y
        '''
        If the touch and drag is on the left third of the screen, move the center of player 1's paddle to the touch
        location.
        
        If the touch and drag is on the right third of the screen, move the center of player 2's paddle to the touch
        location.
        '''


class PongBall(Widget):
    """
    The PongBall Widget represents the ball that bounces back and forth across the screen.
    """
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    '''
    The X and Y velocity components are represented as numeric properties, allowing us to do Kivy things with them.
    Velocity is a ReferenceListProperty, which is really just a Kivy version of a Python list. Here, it contains 
    both the x and y components of the total velocity.
    '''

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
    '''
    The move method is used by the update function to move the ball. It sets the ball's current position to its new
    position based on its velocity. 
    
    Position is a Kivy vector, so we have to turn the velocity property into a Vector before adding it to the 
    position. If we don't do this, Kivy would get confused and explode.
    '''


class PongPaddle(Widget):
    """
    PongPaddle represents the paddles controlled by the players in the game.
    """
    score = NumericProperty(0)
    '''
    By now, score should be easy to you :)
    '''

    def bounce_ball(self, ball):
        """
        bounce_ball is used by the update function to bounce the ball off the paddle if necessary.
        
        The ball is given as a parameter because otherwise, the paddle would have no way to reach the ball in code
        to change things about it, like its velocity. 
        """
        if self.collide_widget(ball):
            '''
            collide_widget is a nifty function provided by Kivy Widgets to let us know if the current widget and the
            widget given in the parameter have collided
            ''' 
            vx, vy = ball.velocity
            # Split out the velocity vector into its components for easy use
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            '''
            The offset is for a nifty game behavior. It makes the paddles bounce the ball as if the paddles were 
            rounded. If the ball is closer to the edge of the paddle, the ball will go more in the direction of 
            that edge. If we didn't do this, the ball would just bounce horizontally forever, since nothing else
            would be changing the direction of its velocity.
            ''' 
            bounced = Vector(-1 * vx, vy)
            # Create a Vector for the ball velocity, and change the direction of the X component, since it's bouncing
            vel = bounced * 1.1
            # Every time it bounces, increase its velocity by 10% or 1/10 or 1.1. This makes it progressively faster
            ball.velocity = vel.x, vel.y + offset
            # Set the ball's velocity to the velocity components we just calculated plus the offset 


if __name__ == '__main__':
    PongApp().run()
# You should know what this is by now
