# Class 3

## Input
Touch

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
