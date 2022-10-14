# shkval

Wipe (shred) a file on a remote file system by forging and sending a IP/TCP packet utilizing the TCP source port as a key and the TCP "options" field as a one-time password.

The server (iptables) will reject the packet and an entry appended to the "kern.log". This entry is read by server.py. server.py will then begin the file shredding process.