# Stuff

## Install
https://kivy.org/docs/installation/installation-windows.html#installation-windows
1. Setup in PyCharm (virtual environment)
2. `python -m pip install --upgrade pip wheel setuptools`
3. `python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew`
4. `python -m pip install kivy.deps.gstreamer`
5. `python -m pip install kivy`

## Base Program
https://kivy.org/docs/guide/basic.html#quickstart

## Android
https://kivy.org/docs/guide/packaging-android.html#packaging-android
https://python-for-android.readthedocs.io/en/latest/quickstart/
* https://python-for-android.readthedocs.io/en/latest/quickstart/
    * https://developer.android.com/studio/index.html#downloads
        * Get just the command line tools
    * https://developer.android.com/ndk/downloads/index.html
    * Unzip both to some folder, maybe Documents
    * Install SDKs and dependencies
        * Go to the tools directory
        * `$SDK_DIR/tools/bin/sdkmanager "platforms;android-19"`
        * `$SDK_DIR/tools/bin/sdkmanager --list` to list available build tools
        * `$SDK_DIR/tools/bin/sdkmanager "build-tools;27.0.3"
* Setup pip for android
    * `pip install python-for-android`
    * test: `python-for-android recipes`
    *
