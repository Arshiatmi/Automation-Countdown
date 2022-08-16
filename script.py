from automator import *
import webbrowser


def test():
    webbrowser.open("https://google.com")


countdown = AutomatorCountdown(
    test,  # Function Name That Will Be Called After Countdown
    datetime.time(hour=20, minute=13),  # Target Time
    [],  # Your Function Arguments
    {},  # Your Function Keyword arguments
    None  # Print Function That You Can Change It From Default Function
)

countdown.run(
    font='univers',  # This Font Is Default. This Fonts Are Pyfiglet Fonts.
    # The Width That Is Setted For This Font. If You Have Problem With nextline Characters You Can Change It.
    width=120
)
