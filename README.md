# shkval

Wipe (shred) a file on a remote file system by forging and sending an TCP/IP packet utilizing the TCP source port as a key and the TCP "options" field as a one-time password.

Your ISP may re-write the options field. You might have to send the packet from something like a VPS or VPN outside of your network.

The server (iptables) will utilize the "SHKVAL" chain and add an entry which is appended to the "kern.log". This entry is read by server.py. server.py will then begin the file shredding process if the source port and options field are correct for the packet added to the kern.log using iptables (SHKVAL chain).