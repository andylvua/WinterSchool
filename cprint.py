import time


class Bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


def print_ok(message):
    print(Bcolors.GREEN + message + Bcolors.END)


def print_warning(message):
    print(Bcolors.WARNING + message + Bcolors.END)


def print_error(message):
    print(Bcolors.ERROR + message + Bcolors.END)


def print_quit():
    for x in range(0, 4):
        b = "Quitting" + "." * x
        print("\r", Bcolors.ERROR + b + Bcolors.END, end="")
        time.sleep(0.5)
