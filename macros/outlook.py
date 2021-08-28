from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Outlook',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Email', [Keycode.CONTROL, '1']),
        (0x004000, 'Msg', [Keycode.CONTROL,Keycode.SHIFT, 'M']),
        (0x400000, 'RepAll', [Keycode.ALT, 'H', -Keycode.COMMAND, 'R', 'A']),
        # 2nd row ----------
        (0x004000, 'Calendar', [Keycode.CONTROL, '2']),
        (0x004000, 'Apt', [Keycode.CONTROL,Keycode.SHIFT, 'A']),
        (0x400000, 'Mtg', [Keycode.CONTROL,Keycode.SHIFT, 'Q']),
        # 3rd row ----------
        (0x000040, 'Find', [Keycode.CONTROL, 'E']),
        (0x000040, 'Unread', [Keycode.CONTROL, 'U']),
        (0x004000, 'Junk', [Keycode.SHIFT, Keycode.F10, 'J',-Keycode.COMMAND,-Keycode.COMMAND,Keycode.ENTER]),
        # 4th row ----------
        (0x000000, '---', []),
        (0x000000, '---', []),
        (0x000000, '---', []),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w'])
    ]
}
