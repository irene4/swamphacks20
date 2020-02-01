#!/usr/bin/env python3

import re

class Color:
    """A color container class."""

    def __init__(self, value : 'str or tuple3(int)'):
        if type(value) is str:
            # try to match hex representation
            match_hex = re.match(r'(?:#|0[xX])(?P<r>[0-9a-fA-F]{2})(?P<g>[0-9a-fA-F]{2})(?P<b>[0-9a-fA-F]{2})$', value)
            match_rgb = re.match(r'\((?P<r>\d{1,3}),(?P<g>\d{1,3}),(?P<b>\d{1,3})\)', value)
            if match_hex:
                self.r = int(match_hex.group('r'), 16)
                self.g = int(match_hex.group('g'), 16)
                self.b = int(match_hex.group('b'), 16)
            elif match_rgb:
                for group in match_rgb.groups():
                    if int(group) < 0 or int(group) > 255:
                        raise ValueError("RGB format expects values between 0 and 255.")
                self.r = int(match_hex.group('r'))
                self.g = int(match_hex.group('g'))
                self.b = int(match_hex.group('b'))
            else:
                raise ValueError("Input string parsing failed.")
        elif type(value) is tuple:
            if len(value) != 3:
                raise ValueError("Input tuple should only contain three (3) elements.")
            for val in value:
                if not (type(val) is int):
                    raise ValueError("Input tuple contents should be integers.")
            self.r = value[0]
            self.g = value[1]
            self.b = value[2]
        else:
            raise ValueError("Value must be a hex code passed as a string ",
                            "or an RGB value passed as a tuple.")

    def asTuple(self) -> tuple:
        return (self.r,self.g,self.b)

    def asHex(self) -> str:
        return '{0:#0{1}x}'.format(self.r << 16 | self.g << 8 | self.b, 8)

    def asWebHex(self) -> str:
        return '#{0:0{1}x}'.format(self.r << 16 | self.g << 8 | self.b, 6)

    def __repr__(self):
        return repr(self.asTuple())
