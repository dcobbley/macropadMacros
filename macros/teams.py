from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Teams',
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFFFFFF, 'Mute', [Keycode.CONTROL, '1']),
        (0x004000, 'Share', [Keycode.CONTROL,Keycode.SHIFT, 'E']),
        (0x004000, 'Hand', [Keycode.CONTROL,Keycode.SHIFT, 'K']),
        # 2nd row ----------
        (0x000040, 'Join', [Keycode.ALT,Keycode.SHIFT, 'J']),
        (0x000040, 'TglVid', [Keycode.CONTROL,Keycode.SHIFT, 'O']),
        (0x000040, 'End', [Keycode.CONTROL,Keycode.SHIFT, 'B']),
        # 3rd row ----------
        (0x202000, 'Chat', [Keycode.CONTROL, '2']),
        (0x202000, 'Teams', [Keycode.CONTROL, '3']),
        (0x202000, 'Cal', [Keycode.CONTROL, '4']),
        # 4th row ----------
        (0x000000, 'ShtCut', [Keycode.CONTROL, '.']),
        (0x004000, 'ScdMtg', [Keycode.ALT,Keycode.SHIFT, 'N']),
        (0x800000, 'Start', [Keycode.CONTROL,Keycode.SHIFT, 'U']),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w'])
    ]
}
