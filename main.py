#!/usr/bin/env python3

import hashlib


def get_registration_key(serial_number: str, key_length: int = 5) -> str:
    serial_number = serial_number.upper()

    trunc = 8 if len(serial_number) > 8 else len(serial_number)
    mangled_serial = serial_number[:trunc] + 'W3#@8F!T' + serial_number[trunc:]
    md5sum = hashlib.md5(mangled_serial.encode('utf-8')).hexdigest()

    return md5sum[-key_length:].upper()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Registration key generator for NETGEAR Smart Managed Pro switches'
    )
    parser.add_argument('serial_number', type=str,
                        help='the serial number of the device to generate the registration key for')
    parser.add_argument('-l', '--length', dest='key_length', type=int, default=5,
                        help='the length of the registration key to return')
    args = parser.parse_args()

    print(get_registration_key(args.serial_number, args.key_length))
