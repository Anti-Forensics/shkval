#!/usr/bin/env python3

import binascii
import subprocess
import re
import sys

file_to_delete_full_path = "/tmp/secrets.db"
command_password = "dlSmtkQaGTfATveHtjwb"
command_port = "666"


def tail_kern_log():
    parsed_options_password = ''
    parsed_command_password = ''
    parsed_source_port = ''

    while True:
        dmesg_log = subprocess.Popen(['dmesg'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        for line in dmesg_log.stdout.readlines():
            line = line.decode()

            source_port = re.findall("SPT=.*? ", line)
            if source_port:
                parsed_source_port = str(source_port[0]).strip().split("=")[1]

            options_password = re.findall("OPT .*?\)", line)
            if options_password:
                parsed_options_password = str(options_password[0]).strip().split(" ")[1].strip(")(")[4:-4]
                parsed_command_password = binascii.hexlify(command_password.encode()).upper().decode()

            if source_port and options_password:
                try:
                    if parsed_options_password == parsed_command_password and parsed_source_port == command_port:
                        shred_response = subprocess.Popen(["shred", "-f", "-n 1", "-u", file_to_delete_full_path],
                                                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        if shred_response.stdout.readline().decode() in "failed to open":
                            sys.exit(0)
                except Exception as e:
                    print(e)


def main():
    assert len(command_password) == 20
    tail_kern_log()


if __name__ == '__main__':
    main()
