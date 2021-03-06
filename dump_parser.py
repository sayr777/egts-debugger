#! /usr/bin/env python3.6
# -*- coding: utf-8 -*-

import argparse
import sys
from egtsdebugger.egts import *

if __name__ == "__main__":

  parser = argparse.ArgumentParser()
  parser.add_argument("-f", "--file", help="file with data", required=True)
  args = parser.parse_args()

  f = open(args.file, "rb")
  buff = f.read()

  while len(buff) > 0:
    try:
      egts = Egts(buff)
    except EgtsParsingError as err:
      print("Wrong EGTS package: ", err, file=sys.stderr)
      offset = buff.find(b'\x01')

      if offset < 0:
        print("EGTS packets not found: ", buff, file=sys.stderr)
        buff = b''

      buff = buff[offset+1:]
    else:
      print(egts)
      buff = egts.rest_buff
