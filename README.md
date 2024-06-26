# Colorful Print Utility

This Python module provides a simple utility for printing text in various colors to the terminal. It supports printing in green, red, yellow, blue, and purple, as well as a special "rainbow" mode that cycles through colors for each argument.

## Functions

- `print_green(*args)`: Prints the given arguments in green color.
- `print_red(*args)`: Prints the given arguments in red color.
- `print_yellow(*args)`: Prints the given arguments in yellow color.
- `print_blue(*args)`: Prints the given arguments in blue color.
- `print_purple(*args)`: Prints the given arguments in purple color.
- `print_rainbow(*args)`: Prints each argument in a different color, cycling through the available colors. Supports nested lists and dictionaries.

## Usage

To use this module, simply import it and call the desired function with the text you want to print as arguments. Here's an example:

```python
from print_color import print_green, print_rainbow

print_green("This is in green!")
print_rainbow("This", "will", "be", "in", "multiple", "colors!")

Alternatively, you can import all functions at once using from print_color import *. However, be cautious when using this approach as it imports all public names defined in the module, which can lead to conflicts with other modules or variables in your namespace.*

## Customization
The colors are defined using ANSI escape codes. You can modify the choose_color function or the color codes within each print function if you wish to customize the colors.

## Requirements
This module uses standard Python libraries only and should work on any system that supports Python and ANSI escape codes for terminal colors.

## License
This project is open-sourced under the MIT License. Feel free to use, modify, and distribute as you see fit. ```

