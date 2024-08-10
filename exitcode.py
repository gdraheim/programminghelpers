#! /usr/bin/python3
"""A list of process exit(3) codes. Note that when a signal(7) is the reason for 
the process termination then the exit code in a shell is usually 128+signalnumber. 
Bash defines its own exitcodes slightly below that (127 and 126), 
while Unix sysexits.h defines values starting at 64 (upto EX_MAX == 78 on Linux).
                                                                 ///
in Python the symbols are available as signal.SIGQUIT and os.EX_USAGE ///
in Unix the EX-symbols are from <sysexits.h> and SIG-symbols form <signal.h>
"""

__copyright__ = "(C) 2023-2024 Guido U. Draheim, licensed under the APLv2"
__version__ = "1.0.1325"

from typing import Dict, NamedTuple, Union, cast, List
import os
import signal

def pad(width: int, value: Union[str, int]) -> str:
    n = max(0, width - len(str(value)))
    return cast(str, pad.padding[n]) if n < 9 else (" " * n) # type: ignore[attr-defined]

pad.padding = [ # type: ignore[attr-defined]
    "", " ", "  ", "   ", "    ",  "     ", "      ", "       ", "        "] 


# bash error codes
bash: Dict[str, str] = {}
bash["EXIT_SUCCESS"] = "Success"
bash["EXIT_FAILURE"] = "catchall for general errors"
bash["EXIT_MISUSE"] = "misuse of shell builtins"
bash["EXIT_NOEXEC"] = "invoked command cannot execute"
bash["EXIT_NOTFOUND"] = "command not found"

# POSIX.1 - see linux man signal(7)
posix: Dict[str, str] = {}
posix["EXIT_SIGHUP"] = "Hangup (terminal or death of controlling process)"
posix["EXIT_SIGINT"] = "Interrupt from keyboard (Control-C)"
posix["EXIT_SIGQUIT"] = "Quit from keyboard (Control-D)"
posix["EXIT_SIGILL"] = "Illegal Instruction"
posix["EXIT_SIGABRT"] = "Abort signal from abort(3)"
posix["EXIT_SIGFPE"] = "Floating point exception"
posix["EXIT_SIGKILL"] = "Kill signal (not stoppable)"
posix["EXIT_SIGSEGV"] = "Invalid memory reference"
posix["EXIT_SIGPIPE"] = "Broken pipe (write with no readers)"
posix["EXIT_SIGALRM"] = "Timer signal from alarm(2)"
posix["EXIT_SIGTERM"] = "Termination signal (shutdown)"
posix["EXIT_SIGUSR1"] = "User-defined signal 1"
posix["EXIT_SIGUSR2"] = "User-defined signal 1"
posix["EXIT_SIGCONT"] = "Continue if stopped"
posix["EXIT_SIGSTOP"] = "Stop process (not stoppable)"
posix["EXIT_SIGTSTP"] = "Stop typed terminal (Control-Q)"
posix["EXIT_SIGTTIN"] = "Terminal input for background process"
posix["EXIT_SIGTTOU"] = "Terminal output for background process"

# SUSv2 - see linux man signal(7)
unix: Dict[str, str] = {}
unix["EXIT_SIGBUS"] = "Bus error (bad memory access)"
unix["EXIT_SIGPOLL"] = "Pollable event (alias SIGIO)"
unix["EXIT_SIGSYS"] = "Bad systemcall"
unix["EXIT_SIGTRAP"] = "Trace/breakpoint trap"
unix["EXIT_SIGURG"] = "Urgent condition on socket"
unix["EXIT_SIGVTALRM"] = "Virtual alarm clock"
unix["EXIT_SIGXCPU"] = "CPU time limit exceeded"
unix["EXIT_SIGXFSZ"] = "File size imit exceeded"

# Linux /usr/include/sysexits.h
sysexit: Dict[str, str] = {}
sysexit["EX_OK"] = "Success"
sysexit["EX_USAGE"] = "command line usage error"
sysexit["EX_DATAERR"] = "data format error"
sysexit["EX_NOINPUT"] = "cannot open input"
sysexit["EX_NOUSER"] = "adressee unknown"
sysexit["EX_NOHOST"] = "host name unknown"
sysexit["EX_UNAVAILABLE"] = "service unavailable"
sysexit["EX_SOFTWARE"] = "internal software error"
sysexit["EX_OSERR"] = "system error (perphaps cannot fork)"
sysexit["EX_OSFILE"] = "critical OS file missing"
sysexit["EX_CANTCREAT"] = "can't create (user) output file"
sysexit["EX_IOERR"] = "input/output error"
sysexit["EX_TEMPFAIL"] = "temp failure; user is invited to retry"
sysexit["EX_PROTOCOL"] = "remote error in protocol"
sysexit["EX_NOPERM"] = "permission denied"
sysexit["EX_CONFIG"] = "configuration error"
sysexit["EX_MAX"] = "maximum listed value"



class ExitcodeValues(NamedTuple):
    values: Dict[str, int]
    hints: Dict[str, str]

def exitcode_values(combine: bool = False):
    hint = {}
    vals = {}
    # POSIX.1 - see linux man signal(7)
    for name, value in bash.items():
        hint[name] = value
    # POSIX.1 - see linux man signal(7)
    for name, value in posix.items():
        hint[name] = value
    # SUSv2 - see linux man signal(7)
    for name, value in unix.items():
        hint[name] = value
    # Linux /usr/include/sysexits.h
    for name, value in sysexit.items():
        hint[name] = value

    # bash defined
    vals["EXIT_SUCCESS"] = 0
    vals["EXIT_FAILURE"] = 1
    vals["EXIT_MISUSE"] = 2  
    vals["EXIT_NOEXEC"] = 126  
    vals["EXIT_NOTFOUND"] = 127  
    for name in dir(signal):
        if name.startswith("SIG") and not name.startswith("SIG_"):
            vals["EXIT_"+name] = 128 + getattr(signal, name)

    for name in dir(os):
        if name.startswith("EX_"):
            vals[name] = getattr(os, name)
    if combine:
        if "EX_OK" in vals and "EXIT_SUCCESS" in vals:
            vals["EXIT_SUCCESS EX_OK"] = vals["EXIT_SUCCESS"]
            hint["EXIT_SUCCESS EX_OK"] = hint["EXIT_SUCCESS"]
            del vals["EX_OK"]
            del vals["EXIT_SUCCESS"]
    return ExitcodeValues(vals, hint)

def printall() -> None:
    vals, hint = exitcode_values(True)
    maxname = max(len(name) for name in vals.keys())
    maxvalue = max(len(str(val)) for val in vals.values())
    for name in reversed(sorted(vals, key=lambda x: vals[x])):
        value = vals[name]
        plus = "+" if name in posix else ":" if name in sysexit else " "
        print(pad(maxvalue, value), value, name, pad(
            maxname, name), plus+(hint[name] if name in hint else "-"))


def printposix() -> None:
    vals, hint = exitcode_values()
    maxname = max(len(name) for name in vals.keys())
    maxvalue = max(len(str(val)) for val in vals.values())
    for name in reversed(sorted(vals, key=lambda x: vals[x])):
        value = vals[name]
        if name in posix or name in sysexit:
            print(pad(maxvalue, value), value, name,
                  pad(maxname, name), (hint[name] if name in hint else "-"))

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
