from scapy import all as scapy
#  https://www.iana.org/assignments/tcp-parameters/tcp-parameters.xhtml

command_password = "dlSmtkQaGTfATveHtjwb"
command_port = 666

scapy.sr(scapy.IP(dst="10.0.2.23") / scapy.TCP(sport=command_port, dport=666, seq=1, ack=666, flags="S",
                                               urgptr=0, options=[(19, command_password)]))
