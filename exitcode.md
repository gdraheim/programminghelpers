## exitcode

Usage: exitcode.py [-options]

Options:
  -h, --help     show this help message and exit
  -s, --showref  show the source of the definition
  -p, --posix    only show posix defined errno codes

A list of process exit(3) codes. Note that when a signal(7) is the reason for
the process termination then the exit code in a shell is usually
128+signalnumber.  Bash defines its own exitcodes slightly below that (127 and
126),  while Unix sysexits.h defines values starting at 64 (upto EX_MAX == 78
on Linux).
/// in Python the symbols are available as signal.SIGQUIT and os.EX_USAGE ///
in Unix the EX-symbols are from <sysexits.h> and SIG-symbols form <signal.h>

| num | name | ref | description
| --: | ---- | --- | -----------
| 192 | EXIT_SIGRTMAX | - | -
| 162 | EXIT_SIGRTMIN | - | -
| 159 | EXIT_SIGSYS | - | Bad systemcall
| 158 | EXIT_SIGPWR | - | -
| 157 | EXIT_SIGPOLL | - | Pollable event (alias SIGIO)
| 157 | EXIT_SIGIO | - | -
| 156 | EXIT_SIGWINCH | - | -
| 155 | EXIT_SIGPROF | - | -
| 154 | EXIT_SIGVTALRM | - | Virtual alarm clock
| 153 | EXIT_SIGXFSZ | - | File size imit exceeded
| 152 | EXIT_SIGXCPU | - | CPU time limit exceeded
| 151 | EXIT_SIGURG | - | Urgent condition on socket
| 150 | EXIT_SIGTTOU | posix | Terminal output for background process
| 149 | EXIT_SIGTTIN | posix | Terminal input for background process
| 148 | EXIT_SIGTSTP | posix | Stop typed terminal (Control-Q)
| 147 | EXIT_SIGSTOP | posix | Stop process (not stoppable)
| 146 | EXIT_SIGCONT | posix | Continue if stopped
| 145 | EXIT_SIGCLD | - | -
| 145 | EXIT_SIGCHLD | - | -
| 143 | EXIT_SIGTERM | posix | Termination signal (shutdown)
| 142 | EXIT_SIGALRM | posix | Timer signal from alarm(2)
| 141 | EXIT_SIGPIPE | posix | Broken pipe (write with no readers)
| 140 | EXIT_SIGUSR2 | posix | User-defined signal 1
| 139 | EXIT_SIGSEGV | posix | Invalid memory reference
| 138 | EXIT_SIGUSR1 | posix | User-defined signal 1
| 137 | EXIT_SIGKILL | posix | Kill signal (not stoppable)
| 136 | EXIT_SIGFPE | posix | Floating point exception
| 135 | EXIT_SIGBUS | - | Bus error (bad memory access)
| 134 | EXIT_SIGIOT | - | -
| 134 | EXIT_SIGABRT | posix | Abort signal from abort(3)
| 133 | EXIT_SIGTRAP | - | Trace/breakpoint trap
| 132 | EXIT_SIGILL | posix | Illegal Instruction
| 131 | EXIT_SIGQUIT | posix | Quit from keyboard (Control-D)
| 130 | EXIT_SIGINT | posix | Interrupt from keyboard (Control-C)
| 129 | EXIT_SIGHUP | posix | Hangup (terminal or death of controlling process)
| 127 | EXIT_NOTFOUND | bash | command not found
| 126 | EXIT_NOEXEC | bash | invoked command cannot execute
| 78 | EX_CONFIG | sysexit | configuration error
| 77 | EX_NOPERM | sysexit | permission denied
| 76 | EX_PROTOCOL | sysexit | remote error in protocol
| 75 | EX_TEMPFAIL | sysexit | temp failure; user is invited to retry
| 74 | EX_IOERR | sysexit | input/output error
| 73 | EX_CANTCREAT | sysexit | can't create (user) output file
| 72 | EX_OSFILE | sysexit | critical OS file missing
| 71 | EX_OSERR | sysexit | system error (perphaps cannot fork)
| 70 | EX_SOFTWARE | sysexit | internal software error
| 69 | EX_UNAVAILABLE | sysexit | service unavailable
| 68 | EX_NOHOST | sysexit | host name unknown
| 67 | EX_NOUSER | sysexit | adressee unknown
| 66 | EX_NOINPUT | sysexit | cannot open input
| 65 | EX_DATAERR | sysexit | data format error
| 64 | EX_USAGE | sysexit | command line usage error
| 2 | EXIT_MISUSE | bash | misuse of shell builtins
| 1 | EXIT_FAILURE | bash | catchall for general errors
| 0 | EXIT_SUCCESS | EX_OK | - Success
