# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Web Browser', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x004000, 'Fwd >', [Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x400000, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0x202000, '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x202000, 'Tab >', [Keycode.CONTROL, Keycode.TAB]),
        (0x400000, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Reload', [Keycode.CONTROL, 'r']),
        (0x000040, 'Home', [Keycode.ALT, Keycode.HOME]),
        (0x000040, 'Private', [Keycode.CONTROL, Keycode.SHIFT, 'P']),
        # 4th row ----------
        (0x000000, 'Reddit', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                           'www.reddit.com\n']),
        (0x800000, 'Giz', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                            'www.gizmodo.com\n']),
        (0x101010, 'Hacks', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                             'www.hackaday.com\n']),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close tab
    ]
}
