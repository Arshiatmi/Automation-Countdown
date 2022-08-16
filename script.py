from automator import *
import webbrowser


def test():
    webbrowser.open("https://google.com")


a = AutomatorCountdown(test, datetime.time(hour=20, minute=13))
a.run()
