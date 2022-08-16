import webbrowser
import datetime
import time
import os
import pyfiglet
import sys
import enum


# Commands For Clear Your Screen
class CommandsToClearScreen(enum.Enum):
    win32 = "cls"
    linux = "clear"
    mac = "clear"
    aix = "cls"
    cygwin = "clear"
    darwin = "clear"


USER_OS = sys.platform  # User Platform ( Auto Detect )

# This Will Be Opened After Countdown.
url_to_go_after_countdown = 'https://google.com'

# Countdown Will Be Depends On This Time
target_time_that_countdown_ends = datetime.time(hour=20, minute=13)

# Make A Loop Until Countdown Ends.
while True:

    # Clear The Screen Depends On User Operation System #
    try:
        os.system(getattr(CommandsToClearScreen, USER_OS).value)
    except:
        raise OSError(
            "Your Os Is Not Detected. You Can Add Your Os In Commands Class In Code.")

    now = datetime.datetime.now()  # Get Current Time

    # Check If Target Time Arrived Or Not. If Its Arrived A Link Will Be Opened.
    if now.hour == target_time_that_countdown_ends.hour:
        if now.minute == target_time_that_countdown_ends.minute:
            # You Can Rewrite This Part That What Happens If Countdown Ends.
            webbrowser.open(url_to_go_after_countdown)
            exit(0)

    # Calculate Remaining Time For Countdown.
    target_time = datetime.datetime.combine(
        now, target_time_that_countdown_ends)
    now_time = datetime.datetime.combine(now, now.time())
    ans = target_time - now_time

    # Tries To Calculate Hour,Minute And Seconds Of Countdown.
    answer_to_print = f"{str(ans.seconds // 3600).zfill(2)} : {str((ans.seconds // 60) % 60).zfill(2)} : {str(ans.seconds % 60).zfill(2)}"

    # Pretty Print For Countdown.
    print(pyfiglet.figlet_format(answer_to_print, 'univers', width=110))

    # Wait For 1 Seconds.
    time.sleep(1)
