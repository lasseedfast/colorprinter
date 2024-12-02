def choose_color(last_color_index):
    """
    Selects the next color in a predefined sequence of colors.

    Args:
        last_color_index (int): The index of the last color used.

    Returns:
        tuple: A tuple containing the ANSI escape code for the selected color (str) 
               and the index of the selected color (int).
    """
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


def print_green(*args):
    """
    Prints the provided arguments in green.
    """
    text = ""
    for arg in args:
        text += str(arg) + " "
    print(f"\033[92m{text}\033[0m")


def print_red(*args):
    """
    Prints the provided arguments in red.
    """
    text = ""
    for arg in args:
        text += str(arg) + " "
    print(f"\033[91m{text}\033[0m")


def print_yellow(*args):
    """
    Prints the provided arguments in yellow.
    """
    text = ""
    for arg in args:
        text += str(arg) + " "
    print(f"\033[93m{text}\033[0m")


def print_blue(*args):
    """
    Prints the provided arguments in blue.
    """
    text = ""
    for arg in args:
        text += str(arg) + " "
    print(f"\033[94m{text}\033[0m")


def print_purple(*args):
    """
    Prints the provided arguments in purple.
    """
    text = ""
    for arg in args:
        text += str(arg) + " "
    print(f"\033[95m{text}\033[0m")


def print_rainbow(*args):
    """
    Prints the provided arguments in a rainbow of colors.

    Args:
        *args: Variable length argument list. Each argument can be a string, list, or dictionary.
               - If the argument is a list, each element in the list will be printed in a different color.
               - If the argument is a dictionary, each key-value pair will be printed in a different color.
               - If the argument is a string or any other type, it will be printed in a different color.

    Returns:
        None
    """
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
