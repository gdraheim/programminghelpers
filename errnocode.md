## errnocode

Usage: errnocode.py [-options]

Options:
  -h, --help     show this help message and exit
  -s, --showref  show the source of the definition
  -p, --posix    only show posix defined errno codes

When called without arguments it will print a list of all errno values that
exist in the system (in reverse order to see the lowest numbers last on
screen). Any number or name given will print the errno value record for it
which includes the numeric value, the symbolic name, and the strerror
description. ... This program is handy for programmers to pick an apropriate
errno value when developing software that returns error codes via errno(3)

| num | name | ref | description
| --: | ---- | --- | -----------
| 132 | ERFKILL | -| Operation not possible due to RF-kill
| 131 | ENOTRECOVERABLE | -| State not recoverable
| 130 | EOWNERDEAD | -| Owner died
| 129 | EKEYREJECTED | -| Key was rejected by service
| 128 | EKEYREVOKED | -| Key has been revoked
| 127 | EKEYEXPIRED | -| Key has expired
| 126 | ENOKEY | -| Required key not available
| 125 | ECANCELED | posix| Operation canceled
| 124 | EMEDIUMTYPE | -| Wrong medium type
| 123 | ENOMEDIUM | -| No medium found
| 122 | EDQUOT | -| Disk quota exceeded
| 121 | EREMOTEIO | -| Remote I/O error
| 120 | EISNAM | -| Is a named type file
| 119 | ENAVAIL | -| No XENIX semaphores available
| 118 | ENOTNAM | -| Not a XENIX named type file
| 117 | EUCLEAN | -| Structure needs cleaning
| 116 | ESTALE | -| Stale file handle
| 115 | EINPROGRESS | posix| Operation now in progress
| 114 | EALREADY | -| Operation already in progress
| 113 | EHOSTUNREACH | -| No route to host
| 112 | EHOSTDOWN | -| Host is down
| 111 | ECONNREFUSED | -| Connection refused
| 110 | ETIMEDOUT | posix| Connection timed out
| 109 | ETOOMANYREFS | -| Too many references: cannot splice
| 108 | ESHUTDOWN | -| Cannot send after transport endpoint shutdown
| 107 | ENOTCONN | -| Transport endpoint is not connected
| 106 | EISCONN | -| Transport endpoint is already connected
| 105 | ENOBUFS | -| No buffer space available
| 104 | ECONNRESET | -| Connection reset by peer
| 103 | ECONNABORTED | -| Software caused connection abort
| 102 | ENETRESET | -| Network dropped connection on reset
| 101 | ENETUNREACH | -| Network is unreachable
| 100 | ENETDOWN | -| Network is down
| 99 | EADDRNOTAVAIL | -| Cannot assign requested address
| 98 | EADDRINUSE | -| Address already in use
| 97 | EAFNOSUPPORT | -| Address family not supported by protocol
| 96 | EPFNOSUPPORT | -| Protocol family not supported
| 95 | EOPNOTSUPP | -| Operation not supported
| 95 | ENOTSUP | posix| Operation not supported
| 94 | ESOCKTNOSUPPORT | -| Socket type not supported
| 93 | EPROTONOSUPPORT | -| Protocol not supported
| 92 | ENOPROTOOPT | -| Protocol not available
| 91 | EPROTOTYPE | -| Protocol wrong type for socket
| 90 | EMSGSIZE | posix| Message too long
| 89 | EDESTADDRREQ | -| Destination address required
| 88 | ENOTSOCK | -| Socket operation on non-socket
| 87 | EUSERS | -| Too many users
| 86 | ESTRPIPE | -| Streams pipe error
| 85 | ERESTART | -| Interrupted system call should be restarted
| 84 | EILSEQ | -| Invalid or incomplete multibyte or wide character
| 83 | ELIBEXEC | -| Cannot exec a shared library directly
| 82 | ELIBMAX | -| Attempting to link in too many shared libraries
| 81 | ELIBSCN | -| .lib section in a.out corrupted
| 80 | ELIBBAD | -| Accessing a corrupted shared library
| 79 | ELIBACC | -| Can not access a needed shared library
| 78 | EREMCHG | -| Remote address changed
| 77 | EBADFD | -| File descriptor in bad state
| 76 | ENOTUNIQ | -| Name not unique on network
| 75 | EOVERFLOW | -| Value too large for defined data type
| 74 | EBADMSG | posix| Bad message
| 73 | EDOTDOT | -| RFS specific error
| 72 | EMULTIHOP | -| Multihop attempted
| 71 | EPROTO | -| Protocol error
| 70 | ECOMM | -| Communication error on send
| 69 | ESRMNT | -| Srmount error
| 68 | EADV | -| Advertise error
| 67 | ENOLINK | -| Link has been severed
| 66 | EREMOTE | -| Object is remote
| 65 | ENOPKG | -| Package not installed
| 64 | ENONET | -| Machine is not on the network
| 63 | ENOSR | -| Out of streams resources
| 62 | ETIME | -| Timer expired
| 61 | ENODATA | -| No data available
| 60 | ENOSTR | -| Device not a stream
| 59 | EBFONT | -| Bad font file format
| 57 | EBADSLT | -| Invalid slot
| 56 | EBADRQC | -| Invalid request code
| 55 | ENOANO | -| No anode
| 54 | EXFULL | -| Exchange full
| 53 | EBADR | -| Invalid request descriptor
| 52 | EBADE | -| Invalid exchange
| 51 | EL2HLT | -| Level 2 halted
| 50 | ENOCSI | -| No CSI structure available
| 49 | EUNATCH | -| Protocol driver not attached
| 48 | ELNRNG | -| Link number out of range
| 47 | EL3RST | -| Level 3 reset
| 46 | EL3HLT | -| Level 3 halted
| 45 | EL2NSYNC | -| Level 2 not synchronized
| 44 | ECHRNG | -| Channel number out of range
| 43 | EIDRM | -| Identifier removed
| 42 | ENOMSG | -| No message of desired type
| 40 | ELOOP | -| Too many levels of symbolic links
| 39 | ENOTEMPTY | posix| Directory not empty
| 38 | ENOSYS | posix| Function not implemented
| 37 | ENOLCK | posix| No locks available
| 36 | ENAMETOOLONG | posix| File name too long
| 35 | EDEADLOCK | -| Resource deadlock avoided
| 35 | EDEADLK | posix| Resource deadlock avoided
| 34 | ERANGE | posix| Numerical result out of range
| 33 | EDOM | posix| Numerical argument out of domain
| 32 | EPIPE | posix| Broken pipe
| 31 | EMLINK | posix| Too many links
| 30 | EROFS | posix| Read-only file system
| 29 | ESPIPE | posix| Illegal seek
| 28 | ENOSPC | posix| No space left on device
| 27 | EFBIG | posix| File too large
| 26 | ETXTBSY | -| Text file busy
| 25 | ENOTTY | posix| Inappropriate ioctl for device
| 24 | EMFILE | posix| Too many open files
| 23 | ENFILE | posix| Too many open files in system
| 22 | EINVAL | posix| Invalid argument
| 21 | EISDIR | posix| Is a directory
| 20 | ENOTDIR | posix| Not a directory
| 19 | ENODEV | posix| No such device
| 18 | EXDEV | posix| Invalid cross-device link
| 17 | EEXIST | posix| File exists
| 16 | EBUSY | posix| Device or resource busy
| 15 | ENOTBLK | -| Block device required
| 14 | EFAULT | posix| Bad address
| 13 | EACCES | -| Permission denied
| 12 | ENOMEM | posix| Cannot allocate memory
| 11 | EWOULDBLOCK | -| Resource temporarily unavailable
| 11 | EAGAIN | posix| Resource temporarily unavailable
| 10 | ECHILD | posix| No child processes
| 9 | EBADF | posix| Bad file descriptor
| 8 | ENOEXEC | posix| Exec format error
| 7 | E2BIG | posix| Argument list too long
| 6 | ENXIO | posix| No such device or address
| 5 | EIO | posix| Input/output error
| 4 | EINTR | posix| Interrupted system call
| 3 | ESRCH | posix| No such process
| 2 | ENOENT | posix| No such file or directory
| 1 | EPERM | posix| Operation not permitted
