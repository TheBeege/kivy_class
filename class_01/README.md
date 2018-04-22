# Class 1

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


#### Ubuntu
1. Hit the Windows Key, type in Ubuntu Software, and hit enter
2. Search for "PyCharm CE" and install it
3. Restart the VM once PyCharm installs. For some reason, it didn't seem to update the Unity programs index for me
4. Hit the Windows Key, type in PyCharm, and hit enter
5. Accept the terms
6. I recommend the Darcula theme and skipping remaining options to set defaults

## Setting up a Kivy project

### Extra Ubuntu Setup
On Ubuntu, we have to install some extra things before we can actually start with Kivy. If you're using the class VM, this is already done for you. If you setup the VM yourself, you'll need to follow these instructions.


## Base Program
https://kivy.org/docs/guide/basic.html#quickstart