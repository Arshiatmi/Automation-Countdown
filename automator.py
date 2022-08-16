import enum
import datetime
import sys
import os
from typing import Callable
import pyfiglet
import time

# Commands For Clear Your Screen


class CommandsToClearScreen(enum.Enum):
    win32 = "cls"
    linux = "clear"
    mac = "clear"
    aix = "cls"
    cygwin = "clear"
    darwin = "clear"


class AutomatorCountdown:
    USER_OS = sys.platform  # User Platform ( Auto Detect )

    def __init__(self, func: Callable, target_time: datetime.datetime, args: list = [], kwargs: dict = {}, print_func: Callable = None) -> None:
        self.func = func  # Function That Runs After Finishing Countdown
        self.target_time = target_time  # The Target Time That Countdown Is Depends On This
        self.func_args = args  # Argument Of User Function
        self.func_kwargs = kwargs  # Keyword Arguments Of User Function
        self.print_func = print_func  # The Print Function That User Can Change It

    def run(self, font: str = 'univers', width: int = 120):
        """ Runs The Countdown And Do The Process """
        while True:
            self.clear_screen()

            now = datetime.datetime.now()  # Get Current Time

            # Check If Target Time Arrived Or Not. If Its Arrived A Link Will Be Opened.
            if now.hour == self.target_time.hour:
                if now.minute == self.target_time.minute:
                    self.func(*self.func_args, **self.func_kwargs)
                    exit(0)

            target_time = datetime.datetime.combine(
                now, self.target_time)
            now_time = datetime.datetime.combine(now, now.time())
            ans = target_time - now_time

            # Tries To Calculate Hour,Minute And Seconds Of Countdown.
            answer_to_print = f"{str(ans.seconds // 3600).zfill(2)} : {str((ans.seconds // 60) % 60).zfill(2)} : {str(ans.seconds % 60).zfill(2)}"
            if self.print_func:
                self.print_func(answer_to_print)
            else:
                self.write_nice(answer_to_print, font, width)

            # Wait For 1 Seconds.
            time.sleep(1)

    def write_nice(self, text: str, font: str = 'univers', width: int = 120):
        """ Pretty Print For Countdown. """
        print(pyfiglet.figlet_format(text, font, width=width))

    def clear_screen(self):
        """ Clear The Screen Depends On User Operation System """
        try:
            os.system(getattr(CommandsToClearScreen,
                      AutomatorCountdown.USER_OS).value)
        except:
            raise OSError(
                "Your Os Is Not Detected. You Can Add Your Os In Commands Class In Code.")
