
def print_green(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    print(f"\033[92m{text}\033[0m")


def print_red(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    print(f"\033[91m{text}\033[0m")


def print_yellow(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    print(f"\033[93m{text}\033[0m")


def print_blue(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    print(f"\033[94m{text}\033[0m")


def print_purple(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    print(f"\033[95m{text}\033[0m")


def choose_color(last_color_index):
    colors = {
        "blue": "\033[94m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "red": "\033[91m",
        "purple": "\033[95m",
    }
    color_keys = list(colors.keys())
    color_index = (last_color_index + 1) % len(color_keys)
    color = color_keys[color_index]
    return colors[color], color_index

def print_rainbow(*args):
    color_index = -1
    text = ""
    for arg in args:
        if isinstance(arg, list):
            for i in arg:
                color_code, color_index = choose_color(color_index)
                text += f"{color_code}{i}\033[0m "
        elif isinstance(arg, dict):
            for k, v in arg.items():
                color_code, color_index = choose_color(color_index)
                text += f"{color_code}{k}: {v}\033[0m "
        else:
            color_code, color_index = choose_color(color_index)
            text += f"{color_code}{arg}\033[0m "
    print(text)
