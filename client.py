from scapy import all as scapy
#  https://www.iana.org/assignments/tcp-parameters/tcp-parameters.xhtml

command_password = "dlSmtkQaGTfATveHtjwb"  # MUST BE 20 CHARACTERS
command_port = 666

assert len(command_password) == 20

scapy.sr(scapy.IP(dst="192.168.254.124") / scapy.TCP(sport=command_port, dport=666, seq=1, ack=0, flags="S",
                                               urgptr=0, options=[(19, command_password)]))
