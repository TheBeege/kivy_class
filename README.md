# Kivy Class

Need to get in touch? Message me on our [Discord server](https://discord.gg/8SkRUTc).

## Schedule
### First section - 3 weeks
We'll cover how Kivy works and how to use it. We'll cover setting up Kivy, key features, and best practices.
* 2018-04-14 - [Class 1](./class_01)
  * Installing Kivy
    * [Windows](https://kivy.org/docs/installation/installation-windows.html)
      * Beware that you can't currently deploy to Android with Kivy on Windows. I recommend using a virtual machine running Ubuntu. I tried with CentOS with little success. For guidance on how to do this, look for the Virtual Machine for Windows section in this document.
    * [OS X](https://kivy.org/docs/installation/installation-osx.html)
    * [Ubuntu](https://kivy.org/docs/installation/installation-linux.html)
  * Running our first program: [quickstart](https://kivy.org/docs/guide/basic.html#quickstart)
* 2018-04-21 - [Class 2](./class_02)
  * [Creating the Pong game](https://kivy.org/docs/tutorials/pong.html)
  * [Kv Design Language](https://kivy.org/docs/guide/lang.html)
  * [Properties](https://kivy.org/docs/guide/events.html#introduction-to-properties)
* 2018-04-28 - [Class 3](class_03)
  * [Input](https://kivy.org/docs/guide/inputs.html)
  * Android APIs
  * Deploying to Android
### Second section - 3 weeks: Guided project
* 2018-05-12
* 2018-05-19
* 2018-05-26
### Third section - 3 weeks: Group project
* 2018-06-02
* 2018-06-09
* 2018-06-16


## Virtual Machine for Windows
If you want to deploy to Android or OS X, Windows won't work. The tools simply do not support Windows yet. To get around this, we can use Linux. We can setup a virtual machine (VM) to run Linux inside your Windows computer. I setup a VM on USB that I can give you during class, but I recommend you follow the setting up instructions below to save class time. If you can't setup the VM yourself successfully, we'll set you up in class.

### Using the class VM?
Use the below login info. Kivy and PyCharm are already setup for you.
```
Username: student
Password: pr0grammingisHARDbutyoucandoit!
```

### Setting up a Virtual Machine for yourself?
We're not going to go into why we do each of these steps. This is a one-time setup, unless you plan on becoming a major Linux user. If that is something you're interested in, let me know in Discord, and I can explain things to you.
1. [Download and install VirtualBox](https://www.virtualbox.org/wiki/Downloads) for Windows Hosts (assuming you're on Windows)
2. [Download the Ubuntu ISO](https://www.ubuntu.com/download/desktop) for version 16.04.4 LTS (or similar number)
3. In VirtualBox, click the blue New button on the top left
4. Set the name as Ubuntu, and it will automatically set the other things
5. I usually set memory to 4096 MB, as most of the laptops I use have 8 GB of memory or more. Set this to something reasonable for your hardware.
6. Create a virtual hard disk now
7. Stick with VDI, it's simplest
8. Go with Dynamically allocated
9. For hard disk size, 10 GB _should_ be enough, but I usually set it to 30 GB for good measure
10. Select the VM in the list on the left and hit the green Start arrow at the top
11. Click the folder icon with the green up arrow and navigate to and select the Ubuntu ISO you downloaded
12. Go through the setup. It should be pretty self-explanatory
13. Restart as requested
14. Login
15. After a moment, the software updater will appear and ask if you want to update. Say yes. You'll be asked to restart the virtual machine. Please do it.
16. After restarting, hit the Windows Key, type in Terminal, and hit enter
17. Copy `sudo add-apt-repository ppa:kivy-team/kivy`, hit enter, enter your password, and hit enter again when prompted
18. Copy the below, hit enter, hit `y` when prompted, and do a little dance. You have Kivy installed
```bash
sudo apt-get install -y \
    python-pip \
    build-essential \
    git \
    vim \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev \
    libgstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    openjdk-8-jdk
```
19. Good job! Now, you're ready to start on class 1


## Other Notes
We want Cython 0.26

[KV File highlighting in PyCharm](https://stackoverflow.com/questions/38002630/how-to-get-syntax-highlighting-on-kivy-kv-file-in-pycharm-on-osx?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)

[Buildozer install instructions for Python3](https://pypi.python.org/pypi/buildozer/0.34)