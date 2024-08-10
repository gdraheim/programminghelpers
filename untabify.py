#! /usr/bin/env python3
"""Replace tabs with spaces in argument files.  Print names of changed files."""

import os

def process(filename: str, tabsize: int = 8) -> str:
    try:
        f = open(filename)
        text = f.read()
        f.close()
    except IOError as msg:
        print("%r: I/O error: %s" % (filename, msg))
        return "error %s" % msg
    newtext = text.expandtabs(tabsize)
    if newtext == text:
        return "unchanged"
    backup = filename + "~"
    try:
        os.unlink(backup)
    except os.error:
        pass
    try:
        os.rename(filename, backup)
    except os.error:
        pass
    f = open(filename, "w")
    f.write(newtext)
    f.close()
    return "ok"

if __name__ == '__main__':
    from optparse import OptionParser
    cmdline = OptionParser("%prog [-t4] files..")
    cmdline.add_option("-t", "--tab", metavar="8", default=8, help="another tab-width")
    opt, args = cmdline.parse_args()
    tabsize = int(opt.tab)
    for filename in args:
        done = process(filename, tabsize)
        print(filename, done)
