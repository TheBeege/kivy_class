# Class 1

In this class, we'll cover installing Python and PyCharm, setting up Kivy, and running our first Kivy program.

## Installing everything
### Installing Python

#### OS X
1. Open spotlight by clicking the magnifying class in the top right corner
2. Open Terminal by typing in `terminal` and hitting enter
3. Copy this in and hit enter: `xcode-select --install`. This installs tools for developers on OS X.
4. Type this in and hit enter: `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`. This installs a tool called brew, which makes it easy to install software.
5. Type this in and hit enter: `echo "export PATH=/usr/local/bin:/usr/local/sbin:\$PATH" >> ~/.profile`. This sets up your computer to allow use of brew every time it starts.
6. Type this in and hit enter: `source ~/.profile`. This sets up your computer to allow use of brew now.
7. Type this in and hit enter: `brew install python`. This installs Python. It will take some time.
8. Type this in and hit enter: `python --version`. You should see it output `Python 3.x.x` where `x` is some number we don't care about. If the version starts with a `2`, you probably missed either step 6 or 7.

#### Windows
You should be using the virtual machine for this class. Look at the README in the main folder of this repository.

#### Ubuntu
1. Hit the Windows key to bring up search
2. Type in `terminal`
3. Hit enter
4. Type in `sudo apt install python3`
5. You will be prompted to enter your password. Please enter it. Do be aware that nothing will appear as you type. This is a security measure so someone looking over your shoulder doesn't know how long your password is.
6. Type this to make sure it works and hit enter: `python3 --version`. The version of Python should be output. If it's not working, you'll get a "command not found" error.


### Installing PyCharm

#### OS X
I wrote this from memory, so it may not be exactly perfect. If you find an error, please let me know in Discord.
1. In your browser, go to the [Pycharm download page](https://www.jetbrains.com/pycharm/download/#section=mac)
2. Click the black download button under Community and save it
3. When the download finishes, open it from your download folder
4. A new window should pop up with the PyCharm logo and the Applications folder. Drag the PyCharm logo onto the Applications folder. This may take some time, so be patient and don't repeat it.
5. Double click the Applications folder to open it
6. Scroll down to find PyCharm and double-click it to open it
7. Accept the terms
8. I recommend the Darcula theme and skipping remaining options to set defaults
9. In the dock on the bottom, right-click the PyCharm logo, go to options, and select "Keep in dock"

#### Ubuntu
1. Hit the Windows Key, type in Ubuntu Software, and hit enter
2. Search for "PyCharm CE" and install it
3. Restart the VM once PyCharm installs. For some reason, it didn't seem to update the Unity programs index for me
4. Hit the Windows Key, type in PyCharm, and hit enter
5. Accept the terms
6. I recommend the Darcula theme and skipping remaining options to set defaults
7. On the launcher dock on the left, right click the PyCharm logo and select "Lock to Launcher"

## Setting up a Kivy project
1. Open PyCharm
2. Select "Create New Project"
3. In the location section, change "untitled" to the name of the project, maybe just "kivy_class"
* Note: If there is a space in the location, find a different place to put it. Having a space in the location path will mess things up in all sorts of ways you do not want to deal with. To change the location, click the three dots to the right of the text input and navigate to a folder you want to use.
4. At the top of the screen in the menu, click "View" and navigate to "Tool Windows" and select "Terminal"
5. A panel at the bottom of PyCharm should appear
6. In this panel, type `pip install --upgrade pip` and hit enter. This just gets us the latest version of the Python package manager
7. Type `pip install Cython==0.26` and hit enter. This installs a package called Cython, which is a requirement for Kivy.
8. Type `pip install kivy` and hit enter. This installs Kivy. It will take a long time. Be patient :)

You're ready to go!

## Our First Kivy Program
This is based on the [Kivy Quickstart](https://kivy.org/docs/guide/basic.html#quickstart).

1. Make sure the Project pane appears on the left. If not, go to View > Tool Windows > Project in the menu at the top of the screen.
2. Right click the project folder and select New > Python File
3. Set the name as quickstart.py and hit enter. The file should open in the main editor pane
4. Copy and paste the below code:
```python
import kivy
kivy.require('1.10.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()
```
5. In the top right corner of PyCharm, you should see a drop-down box. Click that and select Edit Configurations
6. At the top left of the Run/Debug Configurations window, click the + symbol and select Python
7. Set the name as Quickstart
8. To the right of the Script Path text input, click the three dots
9. Navigate to and select quickstart.py
10. Hit OK.
11. Click the green arrow next to the drop-down box.
12. You should see red text in the bottom pane and a black window with the text "Hello world"
13. Congratulations! You've run your first Kivy program! Let's break down what this code is doing

```python
import kivy
```
This tells Python we're going to use Kivy and makes it available for our program to use.

```python
kivy.require('1.10.0')
```
This causes our program to fail if it's not running Kivy version 1.10.0. It's a nice safety measure. Older or newer versions of Kivy may use different things, so we can use this to ensure Kivy has exactly what we expect. It's not a requirement, but it's strongly recommended.

```python
from kivy.app import App
```
This imports the `App` class from Kivy. The `App` class is the basis of a Kivy app. It handles creating the window, shutdown, all that sort of basic stuff that we don't want to worry about. Your main Kivy class should inherit from this `App` class, as you'll see shortly.

```python
from kivy.uix.label import Label
```
This imports the `Label` class from kivy. The `Label` class is a visual element (or `Widget`) that shows text on the screen.

```python
class MyApp(App):
```
This creates a new class called `MyApp` that inherits from `App`. For folks from our Python class, this should be verify familiar.

For folks from our Java class, this is how we define classes in Python. Instead of saying `extends ParentClass`, we simply put the parent class in parenthesis. Additionally, instead of using curly brackets, we use a colon followed by indentation. Python uses indentation to manage scopes instead of curly braces. This enforces easily readable code, whereas Java could fit an entire program on one line and be incredibly difficult to read.

```python
def build(self):
```
The `build` method is used by an `App` to set everything up when the app first starts. Basically, it lays out the first steps Kivy should take when your app starts.

For folks from our Java class, this is how we define a method. Notice there is no return type. Python doesn't require you to explicitly state what types everything is. Python just tries to do things as you tell it to, disregarding type. If a method or property is missing, it simply breaks. While this makes code faster to write, it doesn't protect you from coding mistakes. Java makes things a little safer in this regard. `def` tells Python that this is a method definition. `build` is the name of the method. `self` is a way to give the method the ability to reference the object it's being used on. It's equivalent to Java's `this` and is required for all instance methods. You can think of adding the `self` parameter as making it a non-`static` method. By default, everything in Python is static. This changes that.

```python
return Label(text='Hello world')
```
This tells Kivy to display a `Label` as the main thing in the app. For `Label`s and most other `Widget`s, they take in optional parameters to set things. In this case, the text of the label is being set to "Hello world"

For our Java folks, there's a lot going on here. First off, `Label(...)` is calling `Label`s constructor. Python does not require a `new` keyword like Java does. Second, Python has the idea of optional parameters. In Java, if we wanted a method to accept different parameters, we would need to overload the method by defining multiple versions of the method. In Python, this is avoided. You can define methods with a default value like `my_method(param='default')`. In this case, a parameter called `param` has a default value of the string `default`. If we omit parameter, `param` will be set to `'default'`. Additionally, the order of parameters in Python is not strict. If we specify parameters by name, i.e. `text="Hello world"`, we can call parameters in any order we want. Lastly, Python allows use of both single quotes `''` and double quotes `""` for strings.

```python
if __name__ == '__main__':
    MyApp().run()
```
This is a Python thing that tells Python to run our Kivy app. `MyApp` should match the name of your app class. Aside from this, you can copy and paste this for every Kivy app.

If this all makes sense and everything is running smoothly, great job! If there are issues or you have questions, please get in touch with me on Discord.