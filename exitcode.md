## exitcode

| num | name | description
| --: | ---- | -----------
| 192 | EXIT_SIGRTMAX | -
| 162 | EXIT_SIGRTMIN | -
| 159 | EXIT_SIGSYS | Bad systemcall
| 158 | EXIT_SIGPWR | -
| 157 | EXIT_SIGPOLL | Pollable event (alias SIGIO)
| 157 | EXIT_SIGIO | -
| 156 | EXIT_SIGWINCH | -
| 155 | EXIT_SIGPROF | -
| 154 | EXIT_SIGVTALRM | Virtual alarm clock
| 153 | EXIT_SIGXFSZ | File size imit exceeded
| 152 | EXIT_SIGXCPU | CPU time limit exceeded
| 151 | EXIT_SIGURG | Urgent condition on socket
| 150 | EXIT_SIGTTOU | +Terminal output for background process
| 149 | EXIT_SIGTTIN | +Terminal input for background process
| 148 | EXIT_SIGTSTP | +Stop typed terminal (Control-Q)
| 147 | EXIT_SIGSTOP | +Stop process (not stoppable)
| 146 | EXIT_SIGCONT | +Continue if stopped
| 145 | EXIT_SIGCLD | -
| 145 | EXIT_SIGCHLD | -
| 143 | EXIT_SIGTERM | +Termination signal (shutdown)
| 142 | EXIT_SIGALRM | +Timer signal from alarm(2)
| 141 | EXIT_SIGPIPE | +Broken pipe (write with no readers)
| 140 | EXIT_SIGUSR2 | +User-defined signal 1
| 139 | EXIT_SIGSEGV | +Invalid memory reference
| 138 | EXIT_SIGUSR1 | +User-defined signal 1
| 137 | EXIT_SIGKILL | +Kill signal (not stoppable)
| 136 | EXIT_SIGFPE | +Floating point exception
| 135 | EXIT_SIGBUS | Bus error (bad memory access)
| 134 | EXIT_SIGIOT | -
| 134 | EXIT_SIGABRT | +Abort signal from abort(3)
| 133 | EXIT_SIGTRAP | Trace/breakpoint trap
| 132 | EXIT_SIGILL | +Illegal Instruction
| 131 | EXIT_SIGQUIT | +Quit from keyboard (Control-D)
| 130 | EXIT_SIGINT | +Interrupt from keyboard (Control-C)
| 129 | EXIT_SIGHUP | +Hangup (terminal or death of controlling process)
| 127 | EXIT_NOTFOUND | command not found
| 126 | EXIT_NOEXEC | invoked command cannot execute
| 78 | EX_CONFIG | :configuration error
| 77 | EX_NOPERM | :permission denied
| 76 | EX_PROTOCOL | :remote error in protocol
| 75 | EX_TEMPFAIL | :temp failure; user is invited to retry
| 74 | EX_IOERR | :input/output error
| 73 | EX_CANTCREAT | :can't create (user) output file
| 72 | EX_OSFILE | :critical OS file missing
| 71 | EX_OSERR | :system error (perphaps cannot fork)
| 70 | EX_SOFTWARE | :internal software error
| 69 | EX_UNAVAILABLE | :service unavailable
| 68 | EX_NOHOST | :host name unknown
| 67 | EX_NOUSER | :adressee unknown
| 66 | EX_NOINPUT | :cannot open input
| 65 | EX_DATAERR | :data format error
| 64 | EX_USAGE | :command line usage error
| 2 | EXIT_MISUSE | misuse of shell builtins
| 1 | EXIT_FAILURE | catchall for general errors
| 0 | EXIT_SUCCESS | EX_OK   Success
