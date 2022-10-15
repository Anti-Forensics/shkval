#!/usr/bin/env python3

import binascii
import subprocess
import re

logname = "/var/log/kern.log"
command_password = "dlSmtkQaGTfATveHtjwb"
command_port = "666"


def tail_kern_log():
    log_file = subprocess.Popen(['tail', '-F', logname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while True:
        line = str(log_file.stdout.readline())

        source_port = re.findall("SPT=.*? ", line)
        if source_port:
            parsed_source_port = str(source_port[0]).strip().split("=")[1]

        options_password = re.findall("OPT .*?\)", line)
        if options_password:
            parsed_options_password = str(options_password[0]).strip().split(" ")[1].strip(")(")[4:-4]
            parsed_command_password = binascii.hexlify(command_password.encode()).upper().decode()

        if source_port and options_password:
            if parsed_options_password == parsed_command_password and parsed_source_port == command_port:
                subprocess.call(["shred", "-f", "-n 1", "-u", "/tmp/secret.db"])


def main():
    tail_kern_log()


if __name__ == '__main__':
    main()
