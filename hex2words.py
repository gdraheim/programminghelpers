#! /usr/bin/env python3
from typing import Union

__copyright__ = "(C) 2023-2024 Guido U. Draheim, licensed under the APLv2"
__version__ = "1.0.1327"

class HexWords:
    vowels = "oiau"
    consts = "zbcdfghklmnprstw"  # "zyvtsrpnmlkgfdcb"
    @staticmethod
    def encode(n: int) -> str:
        self = HexWords
        s = ""
        while True:
            a = n % 16
            n = n // 16
            b = n % 4
            n = n // 4
            c = n % 16
            n = n // 16
            d = n % 4
            n = n // 4
            e = n % 16
            n = n // 16
            s = self.consts[e] + self.vowels[d] + self.consts[c] + self.vowels[b] + self.consts[a] + s
            if not n: break
            s = ":" + s
            continue
        return s

def hexwords(value: Union[int, str, bytes, bytearray]) -> str:
    return HexWords.encode(int(value, 0))  # type: ignore[arg-type]

if __name__ == "__main__":
    from optparse import OptionParser
    cmdline = OptionParser("%prog [-options] value...")
    cmdline.add_option("-l", "--lengths", action="store_true")
    opt, args = cmdline.parse_args()
    if opt.lengths:
        print(len(HexWords.vowels), len(HexWords.consts))
    else:
        for arg in args:
            print(arg, "=", hexwords(arg))
