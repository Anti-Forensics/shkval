# shkval

Wipe (shred) a file on a remote file system by forging and sending an TCP/IP packet utilizing the TCP source port as a key and the TCP "options" field as a one-time password.

The server (iptables) will reject the packet and add an entry appended to the "kern.log". This entry is read by server.py. server.py will then begin the file shredding process if the source port and options field are correct for the rejected packet.
