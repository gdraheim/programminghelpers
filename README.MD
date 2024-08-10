## programming helpers

Instead of looking up some values and boilerplate code in the web or man pages,
it is much easier to just type a little command that possibly takes some
options to filter for some value classes.

### exitcode.py

Values and Constants to be used with Posix exit(3) or with Python sys.exit()

Note that when a signal(7) is the reason for 
the process termination then the exit code in a shell is usually 128+signalnumber. 
Bash defines its own exitcodes slightly below that (127 and 126), 
while Unix sysexits.h defines values starting at 64 (upto EX_MAX == 78 on Linux).
                                                                 
in Python the symbols are available as signal.SIGQUIT and os.EX_USAGE.
In Unix the EX-symbols are from `<sysexits.h` and SIG-symbols form `<signal.h>`

### errnocode.py

Values and Constants to be used with Posix errno(3) or Python os.errno

The description comes from the strerror(3) message. Use "--posix" to only
show the symboles defined in POSIX.1, otherwise it shows all the errno
values that can be found in the system (which Python will re-export).

## History

Back in the days, there was a bin-errno written in C, using ifdef on errno.h values.




