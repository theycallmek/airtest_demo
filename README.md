# airtest_demo
A short demo showing the power of airtest api and poco using cookie clicker as the target game.
I used Bluestacks 5.8.0.1079 N64 for testing but I believe any android device will work.

Required Packages:

airtest - https://airtest.readthedocs.io/en/latest/index.html

pocoui - https://poco.readthedocs.io/en/latest/index.html

Usage:
- Make sure the device is connected over USB and USB debugging is enabled under developer options.
- Open a cmd prompt and make sure you see your device listed when entering the command 'adb devices'. You can 'adb kill-server' then 'adb start-server' if you dont see your device.
- Open Chrome on the Android device.
- Navigate to https://iogames.onl/cookie-clicker.
- Scroll down enough to be able to see the big cookie.
- Run main.py.
- Watch cookies get clicked.

It will work in the background or minimized and the device resolution doesnt matter :)
