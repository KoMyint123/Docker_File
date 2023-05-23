from color import Fore, Back, Style, init

# Initialize Colorama (required on Windows)
init()

# Use colorama to print colored text
print(Fore.RED + 'This is red text')
print(Back.GREEN + 'This has a green background')
print(Style.BRIGHT + 'This is bright text')
print(Style.RESET_ALL + 'This resets the text formatting')

# You can combine formatting options
print(Fore.YELLOW + Back.BLUE + 'This is yellow text on a blue background')

# Use Style.RESET_ALL to reset the formatting
print(Style.RESET_ALL + 'This resets all formatting options')

# Colorama also supports RGB values for custom colors
print(Fore.RGB(255, 128, 0) + 'This is orange text')

# You can also use shortcuts for common colors
print(Fore.CYAN + 'This is cyan text')

# Style.DIM reduces the intensity of the color
print(Fore.GREEN + Style.DIM + 'This is dim green text')

# Style.NORMAL restores the normal intensity
print(Style.NORMAL + 'This is normal intensity text')

# Back.RESET resets the background color
print(Back.RESET + 'This resets the background color')

# You can nest formatting options
print(Fore.BLUE + 'This is blue text with ' + Back.YELLOW + 'yellow background' + Style.RESET_ALL)
