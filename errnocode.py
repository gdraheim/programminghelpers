#! /usr/bin/python3
"""When called without arguments it will print a list
of all errno values that exist in the system (in reverse order to
see the lowest numbers last on screen). Any number or name given
will print the errno value record for it which includes the numeric
value, the symbolic name, and the strerror description. ... This
program is handy for programmers to pick an apropriate errno value
when developing software that returns error codes via errno(3)"""

__copyright__ = "(C) 2023-2024 Guido U. Draheim, licensed under the APLv2"
__version__ = "1.0.1325"

from typing import NamedTuple, Dict, Union, cast, List
import errno  # type: ignore
import os


# according to linux manpage
posix = ["E2BIG", "EACCESS", "EAGAIN", "EBADF", "EBADMSG", "EBUSY",
         "ECANCELED", "ECHILD", "EDEADLK", "EDOM", "EEXIST", "EFAULT",
         "EFBIG", "EINPROGRESS", "EINTR", "EINVAL", "EIO", "EISDIR",
         "EMFILE", "EMLINK", "EMSGSIZE", "ENAMETOOLONG", "ENFILE",
         "ENODEV", "ENOENT", "ENOEXEC", "ENOLCK", "ENOMEM", "ENOSPC",
         "ENOSYS", "ENOTDIR", "ENOTEMPTY", "ENOTSUP", "ENOTTY",
         "ENXIO", "EPERM", "EPIPE", "ERANGE", "EROFS", "ESPIPE",
         "ESRCH", "ETIMEDOUT", "EXDEV"]

class ErrnoValues(NamedTuple):
    values: Dict[str, int]
    maxname: int
    maxvalue: int

def errno_values() -> ErrnoValues:
    maxname = 0
    maxvalue = 0
    vals = {}
    for name in dir(errno):
        if name.startswith("E") and "_" not in name:
            value = getattr(errno, name)
            maxname = max(maxname, len(name))
            maxvalue = max(maxvalue, len(str(value)))
            vals[name] = value
    return ErrnoValues(vals, maxname, maxvalue)


def pad(width: int, value: Union[str, int]) -> str:
    n = max(0, width - len(str(value)))
    return cast(str, pad.padding[n]) if n < 9 else (" " * n) # type: ignore[attr-defined]

pad.padding = [ # type: ignore[attr-defined]
    "", " ", "  ", "   ", "    ",  "     ", "      ", "       ", "        "] 


def printall() -> None:
    vals, maxname, maxvalue = errno_values()
    for name in reversed(sorted(vals, key=lambda x: vals[x])):
        value = vals[name]
        plus = "+" if name in posix else " "
        print(pad(maxvalue, value), value, name, pad(
            maxname, name), plus+os.strerror(value))


def printposix() -> None:
    vals, maxname, maxvalue = errno_values()
    for name in reversed(sorted(vals, key=lambda x: vals[x])):
        value = vals[name]
        if name in posix:
            print(pad(maxvalue, value), value, name,
                  pad(maxname, name), os.strerror(value))


if __name__ == "__main__":
    from optparse import OptionParser
    cmdline = OptionParser("%prog [-options]", epilog=__doc__)
    cmdline.add_option("-p", "--posix", action="count", default=0,
                       help="only show posix defined errno codes")
    opt, args = cmdline.parse_args()
    if opt.posix:
        printposix()
    else:
        printall()
