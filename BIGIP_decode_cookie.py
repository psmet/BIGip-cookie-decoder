#!/usr/bin/python

# example string: BIGip<ervername>110536896.20480.0000

import struct
import sys
import re

if len(sys.argv) != 2:
    print "Usage: %s cookie" % sys.argv[0]
    exit(1)

cookie = sys.argv[1]
print "\n[*] Cookie to decode: %s\n" % cookie

(cookie_name, cookie_value) = cookie.split('=')

pool = re.search('^BIGipServer([.\w\.]*)', cookie_name)

(host, port, end) = cookie_value.split('.')

(a, b, c, d) = [ord(i) for i in struct.pack("<I", int(host))]

(e) = [ord(e) for e in struct.pack("<H", int(port))]
port = "0x%02X%02X" % (e[0],e[1])

print "[*] Pool name: %s" % (pool.group(1))
print "[*] Decoded IP and Port: %s.%s.%s.%s:%s\n" % (a,b,c,d, int(port,16))
