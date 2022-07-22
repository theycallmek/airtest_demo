from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time

total_t0 = time.time()

# Connect to first device listed from 'adb devices'. Specify a device if you want just check the docs.
try:
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    auto_setup(__file__, logdir=False,
               devices=[f'Android:///?cap_method=javacap&touch_method=adb', ])
except IndexError:
    print('Could not connect to device.')
    quit()


# Using this freeze function allows you to snapshot the UI Hierarchy and store it locally.
# This dramatically reduces time between clicks because we arent refreshing and pulling that
# data over adb after every click. It's about a 10x speed increase. If the screen changes you obviously
# would need to refreeze. That's why the first click takes so much longer to execute.
with poco.freeze() as frozen_poco:

    # Create an instance of the frozen_poco class.
    cookie = frozen_poco("cookieAnchor")

    if cookie.exists():

        # If the cookie exists, click it 10 times.
        for i in range(10):
            i_loop_t0 = time.time()
            cookie.click()
            i_loop_t1 = time.time()

            # Print times clicked and time to click.
            print(f'Cookie clicked {i} amount of times')
            print(f'Time to click: {i_loop_t1 - i_loop_t0}')

# Print total execution time.
total_t1 = time.time()
print(f'DONE!\nTotal time to execute: {total_t1 - total_t0}')
print(f'Clicks/second = {(total_t1 - total_t0) / 10}')

# This just fixes a bug I was having where the poco service app was trying to start itself when already running.
stop_app('com.netease.open.pocoservice')